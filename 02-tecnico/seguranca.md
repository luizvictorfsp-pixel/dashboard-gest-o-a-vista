# Diretrizes de Segurança da Informação e LGPD
## Plataforma de Business Intelligence para Facilities (DNA Facilities)

---

## 1. Princípios de Segurança

A proteção do sistema é orientada pela abordagem de **Defesa em Profundidade (Defense-in-Depth)**:
1. **Identidade e Autenticação**: Validação criptográfica com tokens JWT emitidos pelo Supabase Auth.
2. **Autorização em Camada de Banco**: Row Level Security (RLS) no PostgreSQL, impedindo que clientes web acessem dados de contratos não autorizados, mesmo em caso de requisição forjada.
3. **Autorização na Interface**: Componentes, menus e rotas condicionadas aos perfis do usuário logado.
4. **Proteção de Segredos**: Segredos de infraestrutura restritos a variáveis de ambiente de backend.

---

## 2. Row Level Security (RLS) e Políticas de Banco

### 2.1. Funções de Apoio de Segurança (Security Definer)
O banco de dados utiliza funções estáveis com permissões `SECURITY DEFINER` e `SET search_path = public`:
- `has_role(_user_id uuid, _role app_role)`: Valida se o usuário autenticado possui determinado perfil formal.
- `is_user_manager_or_admin(_user_id uuid)`: Retorna `true` se o usuário pertence ao escalão de gestão ou administração.

### 2.2. Políticas de Acesso RLS por Módulo

```sql
-- Exemplo de política de leitura por contrato vinculado
CREATE POLICY "Usuarios visualizam dados apenas dos seus contratos vinculados"
ON public.contratos_indicadores
FOR SELECT
USING (
  is_user_manager_or_admin(auth.uid()) 
  OR EXISTS (
    SELECT 1 FROM public.usuarios_contratos uc
    WHERE uc.contrato_id = public.contratos_indicadores.contrato_id
      AND uc.user_id = auth.uid()
  )
);

-- Exemplo de proteção estrita para dados de saúde e acidentes (SMA)
CREATE POLICY "Apenas perfil SMA ou Administrador visualiza acidentes detalhados"
ON public.sma_acidentes
FOR SELECT
USING (
  has_role(auth.uid(), 'admin') 
  OR has_role(auth.uid(), 'manager')
);
```

---

## 3. Conformidade com a LGPD (Lei 13.709/2018)

| Requisito LGPD | Implementação Técnica na Plataforma |
|---|---|
| **Minimização de Dados (Art. 6º, III)** | O sistema não armazena CPF, RG, endereço residencial, telefones pessoais ou histórico salarial na camada de BI. A identificação operacional utiliza matrícula interna (`employee_id`). |
| **Proteção de Dados Sensíveis (Art. 11)** | Informações médicas decorrentes de acidentes e atestados de afastamento são segregadas em tabela específica (`sma_ocorrencias_saude`) com RLS restrito a profissionais de SMA. |
| **Mascaramento e Anonimização** | Relatórios executivos e gráficos de tendências agregam métricas por função ou unidade, sem expor dados nominativos. |
| **Trilha de Auditoria (Art. 37)** | Todas as visualizações e exportações de relatórios que contenham listas nominais de colaboradores são registradas na tabela `audit_logs`. |

---

## 4. Gerenciamento de Segredos e Variáveis de Ambiente

- **Client-Side (Público)**:
  - `VITE_SUPABASE_URL`: URL pública da instância do Supabase.
  - `VITE_SUPABASE_PUBLISHABLE_KEY`: Chave anônima pública (restrita pelas políticas de RLS).
- **Server-Side / Infraestrutura (Privado)**:
  - `SUPABASE_SERVICE_ROLE_KEY`: Utilizada **apenas** nas Edge Functions e no n8n.
  - `GOOGLE_SERVICE_ACCOUNT_KEY`: Armazenada com segurança no cofre de credenciais do n8n / Supabase Secrets.
  - **PROIBIDO**: Comitar arquivos `.env` contendo segredos em repositórios Git.
