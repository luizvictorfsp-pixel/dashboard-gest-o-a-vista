# Pipeline de Atualização e Governança de Dados
## Plataforma de Business Intelligence para Facilities (DNA Facilities)

---

## 1. Visão Geral do Pipeline de Dados

O ciclo de vida da ingestão de dados garante integridade, rastreabilidade e disponibilidade contínua:

```text
[1. Fonte de Dados] ──► Google Sheets / Drive ou Upload Local (.xlsx / .csv)
         │
[2. Autenticação]   ──► Validação de Token de Integração / Sessão do Usuário
         │
[3. Extração]       ──► Leitura das abas estruturadas e parse binário/textual
         │
[4. Validação]      ──► Validação de cabeçalhos, tipos de dados e limites via Zod
         │
[5. Higienização]   ──► Sanitização de caracteres, conversão monetária BRL e datas
         │
[6. Persistência]   ──► Upsert atômico idempotente no PostgreSQL (Supabase)
         │
[7. Cálculo]        ──► Processamento das fórmulas oficiais de KPIs (lib/calculations)
         │
[8. Renderização]   ──► Atualização reativa da interface via React Query
         │
[9. Auditoria]      ──► Registro do evento na tabela de auditoria com timestamp
```

---

## 2. Tratamento de Exceções e Resiliência

### 2.1. Planilhas com Linhas Incompletas ou Inválidas
- O validador não interrompe toda a ingestão se houver apenas linhas em branco no final do arquivo.
- Se linhas com preenchimento parcial forem detectadas (ex: valor monetário ausente), a linha é registrada em uma lista de rejeições com o número exato da linha e o campo faltante.
- O sistema permite aprovar a carga parcial informando um resumo: *"118 linhas importadas com sucesso, 2 linhas rejeitadas"*.

### 2.2. Prevenção de Duplicidades (Idempotência)
- O identificador único de negócio é composto pela tupla: `(contrato_id, competencia, chave_entidade)`.
- Se o usuário realizar o upload do mesmo arquivo mais de uma vez, os registros existentes são atualizados (`ON CONFLICT DO UPDATE`), sem duplicar linhas nem inflar somatórios de HHT, custos ou efetivo.

### 2.3. Indisponibilidade de Rede e Modo Offline
- Se a requisição de salvamento no Supabase falhar por oscilação de conexão:
  1. O sistema armazena uma cópia local criptografada em cache (`localStorage` ou `IndexedDB`);
  2. Um aviso visual informa: *"Operando temporariamente em cache local. Os dados serão sincronizados com a nuvem assim que a conexão for restabelecida"*;
  3. Tentativas de reconexão automática ocorrem a cada 30 segundos;
  4. Nenhuma informação anterior válida é sobrescrita no banco até confirmação formal de sucesso da carga.
