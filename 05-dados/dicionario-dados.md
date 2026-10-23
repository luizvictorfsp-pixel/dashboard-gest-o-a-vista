# Dicionário de Dados Oficial
## Plataforma de Business Intelligence para Facilities (DNA Facilities)

---

### Tabela 1: `public.contratos`
Armazena os contratos de prestação de serviços de facilities gerenciados pela DNA Facilities.

| Coluna | Tipo de Dado | Nulo? | Padrão | Descrição |
|---|---|---|---|---|
| `id` | `uuid` | Não | `gen_random_uuid()` | Chave primária |
| `cliente_id` | `uuid` | Não | — | Chave estrangeira -> `clientes(id)` |
| `codigo_contrato` | `varchar(50)` | Não | — | Código interno único do contrato |
| `nome_contrato` | `varchar(150)` | Não | — | Nome descritivo (ex: "Hospital Regional - Bloco Cirúrgico") |
| `data_inicio` | `date` | Não | — | Data de início da vigência contratual |
| `data_termino` | `date` | Sim | `null` | Data prevista de encerramento |
| `valor_mensal_contratual` | `numeric(15,2)` | Não | `0.00` | Valor nominal fixo mensal do contrato |
| `headcount_contratual` | `integer` | Não | `0` | Número total de postos acordados |
| `ativo` | `boolean` | Não | `true` | Indicador se o contrato está vigente |
| `created_at` | `timestamptz` | Não | `now()` | Timestamp de criação |

---

### Tabela 2: `public.rh_registros_competencia`
Consolida os indicadores de movimentação de pessoal e jornada por contrato e competência.

| Coluna | Tipo de Dado | Nulo? | Padrão | Descrição |
|---|---|---|---|---|
| `id` | `uuid` | Não | `gen_random_uuid()` | Chave primária |
| `contrato_id` | `uuid` | Não | — | FK -> `contratos(id)` |
| `competencia` | `varchar(7)` | Não | — | Mês de referência no formato "YYYY-MM" |
| `headcount_realizado` | `integer` | Não | `0` | Efetivo médio ativo prestando serviço |
| `admissoes` | `integer` | Não | `0` | Número de colaboradores admitidos no mês |
| `desligamentos` | `integer` | Não | `0` | Número de desligamentos no mês |
| `afastamentos` | `integer` | Não | `0` | Colaboradores afastados (INSS/doença) |
| `ferias` | `integer` | Não | `0` | Colaboradores em gozo de férias |
| `horas_previstas` | `numeric(10,2)` | Não | `0.00` | Horas programadas de trabalho na escala |
| `horas_ausencia` | `numeric(10,2)` | Não | `0.00` | Horas perdidas não planejadas (absenteísmo) |
| `taxa_turnover` | `numeric(5,2)` | Não | `0.00` | Turnover calculado (%) |
| `taxa_absenteismo` | `numeric(5,2)` | Não | `0.00` | Absenteísmo calculado (%) |
| `created_at` | `timestamptz` | Não | `now()` | Timestamp de criação |
| `updated_at` | `timestamptz` | Não | `now()` | Timestamp de atualização |

- **Restrição de Unicidade**: `UNIQUE (contrato_id, competencia)` para garantir idempotência.

---

### Tabela 3: `public.sma_indicadores`
Armazena métricas de Segurança, Meio Ambiente e Saúde do Trabalho.

| Coluna | Tipo de Dado | Nulo? | Padrão | Descrição |
|---|---|---|---|---|
| `id` | `uuid` | Não | `gen_random_uuid()` | Chave primária |
| `contrato_id` | `uuid` | Não | — | FK -> `contratos(id)` |
| `competencia` | `varchar(7)` | Não | — | Formato "YYYY-MM" |
| `hht` | `numeric(12,2)` | Não | `0.00` | Horas-Homem Trabalhadas no mês |
| `acidentes_com_afastamento` | `integer` | Não | `0` | Total de acidentes com perda de tempo |
| `acidentes_sem_afastamento` | `integer` | Não | `0` | Total de acidentes sem afastamento |
| `acidentes_trajeto` | `integer` | Não | `0` | Acidentes de deslocamento |
| `tfca` | `numeric(8,2)` | Não | `0.00` | Taxa de Frequência de Acidentes c/ Afastamento |
| `tfsa` | `numeric(8,2)` | Não | `0.00` | Taxa de Frequência s/ Afastamento |
| `inspecoes_planejadas` | `integer` | Não | `0` | Meta de inspeções (IPS) |
| `inspecoes_realizadas` | `integer` | Não | `0` | Inspeções executadas |
| `desvios_identificados` | `integer` | Não | `0` | Total de desvios registrados |
| `desvios_tratados` | `integer` | Não | `0` | Total de desvios concluídos |

- **Restrição de Unicidade**: `UNIQUE (contrato_id, competencia)`

---

### Tabela 4: `public.boletins_medicao`
Controla o ciclo de faturamento e medição de facilities.

| Coluna | Tipo de Dado | Nulo? | Padrão | Descrição |
|---|---|---|---|---|
| `id` | `uuid` | Não | `gen_random_uuid()` | Chave primária |
| `contrato_id` | `uuid` | Não | — | FK -> `contratos(id)` |
| `competencia` | `varchar(7)` | Não | — | Formato "YYYY-MM" |
| `status` | `varchar(30)` | Não | `'elaboracao'` | Enum: elaboracao, submetido, aprovado, faturado, recebido |
| `valor_contratual` | `numeric(15,2)` | Não | `0.00` | Valor base do contrato para o mês |
| `valor_medido_bruto` | `numeric(15,2)` | Não | `0.00` | Valor submetido à fiscalização |
| `total_glosas` | `numeric(15,2)` | Não | `0.00` | Somatório de glosas aplicadas |
| `valor_liquido_aprovado` | `numeric(15,2)` | Não | `0.00` | Valor aceito para faturamento |
| `valor_faturado` | `numeric(15,2)` | Não | `0.00` | Valor da NFS-e emitida |
| `valor_recebido` | `numeric(15,2)` | Não | `0.00` | Valor liquidado em conta |
| `numero_nf` | `varchar(50)` | Sim | `null` | Número da Nota Fiscal emitida |
| `data_submissao` | `date` | Sim | `null` | Data do envio do BM |
| `data_aprovacao` | `date` | Sim | `null` | Data do aceite formal do cliente |
| `data_recebimento` | `date` | Sim | `null` | Data do pagamento pelo cliente |
