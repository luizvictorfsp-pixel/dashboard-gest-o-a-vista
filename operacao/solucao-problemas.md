# Guia de Solução de Problemas (Troubleshooting)
## Plataforma de Business Intelligence para Facilities (DNA Facilities)

---

## 1. Problemas Comuns e Soluções Rápidas

### 1.1. Erro: "Perfil não encontrado" ao fazer login
- **Sintoma**: Usuário autentica-se com sucesso, mas visualiza um toast de erro vermelho: *"Perfil não encontrado. Verifique se há um registro na tabela profiles para este usuário"*.
- **Causa**: O usuário existe na tabela `auth.users`, porém o gatilho (trigger) de criação automática na tabela `public.profiles` ou `public.user_roles` falhou ou não foi disparado.
- **Solução**:
  1. Acessar o Supabase SQL Editor;
  2. Verificar se o registro existe em `public.profiles`:
     ```sql
     SELECT * FROM public.profiles WHERE user_id = '<ID_DO_USUARIO>';
     ```
  3. Caso ausente, inserir o registro manualmente ou acionar a Edge Function `create-user`.

---

### 1.2. Erro: "Arquivo com formato não suportado ou colunas ausentes" no Upload
- **Sintoma**: Ao submeter a planilha de custos ou RH, o upload é cancelado com erro de validação.
- **Causa**: O arquivo enviado não possui os nomes exatos de cabeçalhos esperados (ex: `ORÇADO` em maiúsculas com cedilha) ou contém linhas de totais no meio dos dados.
- **Solução**:
  1. Baixar o template padrão correspondente na pasta [docs/templates/](file:///c:/Antigravity/docs/templates/);
  2. Copiar os dados para o template oficial sem alterar a linha 1 (cabeçalhos);
  3. Reenviar o arquivo.

---

### 1.3. Erro: Gráficos em branco ou valores "NaN / Infinity"
- **Sintoma**: Cards de KPIs exibem valores zerados ou variação `NaN%`.
- **Causa**: A competência anterior não possui dados cadastrados para cálculo de variação comparativa ou o denominador é zero (ex: Orçado = 0).
- **Solução**: O sistema trata automaticamente divisões por zero com a refatoração do módulo `lib/calculations/`. Verifique se a competência selecionada possui dados válidos importados.
