# Matriz de Riscos, Dependências e Mitigações
## Plataforma de Business Intelligence para Facilities (DNA Facilities)

---

## 1. Matriz de Riscos

| ID | Risco Identificado | Severidade | Probabilidade | Plano de Mitigação |
|---|---|---|---|---|
| **RSK-001** | Planilhas com formatos divergentes enviadas por supervisores de campo | Alta | Alta | Validador Zod rígido no frontend com fornecimento de templates oficiais pré-formatados e bloqueio de cargas inconsistentes. |
| **RSK-002** | Divergência de critérios de cálculo de turnover ou absenteísmo entre contratos | Média | Alta | Catálogo centralizado de indicadores (`catalogo-indicadores.md`) e parâmetros customizáveis por contrato nas configurações. |
| **RSK-003** | Vazamento de dados de acidentes de trabalho ou atestados (LGPD) | Alta | Baixa | Isolamento em tabela restrita com Row Level Security (RLS) limitando visualização a perfis de SMA e Administrador. |
| **RSK-004** | Queda de conexão com a API do Google Sheets ou Supabase durante reuniões | Média | Média | Fallback automático para persistência local (`localStorage`) exibindo os últimos dados válidos com aviso de contingência. |
| **RSK-005** | Perda de integridade histórica por substituição indevida de competência | Alta | Baixa | Idempotência com chave composta única `(contrato_id, competencia)` e registro imutável em `audit_logs` antes de qualquer alteração. |

---

## 2. Dependências Críticas do Projeto

1. **Validação das Fórmulas Oficiais**: Aprovação formal pela Diretoria e Coordenação de Contratos das fórmulas de Turnover e Absenteísmo estabelecidas no Catálogo.
2. **Definição dos Contratos e Centros de Custo Iniciais**: Lista oficial de contratos ativos que serão cadastrados no piloto da Fase 7.
3. **Conta de Serviço Google Cloud (GCP)**: Criação de Service Account para leitura programada do Google Drive quando ativado o n8n.
4. **Instância Supabase Ativa**: Manutenção das chaves e cotas da instância `https://brihkumeqocjqhcfdlfi.supabase.co`.
