# Governança de Dados, Retenção e Idempotência
## Plataforma de Business Intelligence para Facilities (DNA Facilities)

---

## 1. Princípios de Governança e Qualidade dos Dados

Para que o sistema BI seja aceito como fonte auditável para a Diretoria e clientes da **DNA Facilities**, os dados devem cumprir 5 pilares de qualidade:
1. **Acurácia**: Números calculados refletem a realidade dos postos e das medições sem truncamentos errôneos.
2. **Completude**: Ausência de campos obrigatórios bloqueia a homologação da competência.
3. **Consistência**: O total orçado na Visão Geral deve ser rigorosamente idêntico à soma das categorias no Painel de Orçamento.
4. **Temporalidade (Timeliness)**: Atualizações de competência concluídas em até 2 dias úteis após o fechamento do mês.
5. **Rastreabilidade (Lineage)**: Capacidade de auditar qual usuário, qual arquivo e em qual data foi gerado cada registro.

---

## 2. Idempotência e Atualização Atômica

- **Regra Fundamental**: Toda operação de carga deve ser um **Upsert** (`INSERT ... ON CONFLICT (contrato_id, competencia) DO UPDATE`).
- **Garantia**:
  - Reprocessar o mesmo arquivo não duplica custos nem distorce médias.
  - Se um gestor corrigir uma planilha e reenviá-la, os registros anteriores daquela competência específica são atualizados atomicamente em uma única transação SQL.
  - Histórico de versões: dados anteriores relevantes são salvos na tabela `audit_logs` antes da atualização.

---

## 3. Política de Retenção e Descarte de Dados

| Categoria de Dado | Período de Retenção Ativo | Armazenamento de Arquivamento (Cold Storage) | Descarte / Anonimização |
|---|---|---|---|
| **Métricas Agregadas de KPIs** | 5 anos | Indefinido (para séries históricas plurianuais) | Não aplicável |
| **Registros de Pessoal (RH)** | 5 anos (prazo prescricional trabalhista) | Backup seguro criptografado | Anonimização de nomes após término do contrato |
| **Registros de Acidentes (SMA)** | 20 anos (requisito de medicina ocupacional NR-7) | Backup imutável | Conforme normas previdenciárias e regulatórias |
| **Boletins de Medição e Glosas** | 5 anos (exigência fiscal e contratual) | Arquivo contábil | Conforme política corporativa |
| **Logs de Auditoria e Acessos** | 2 anos em banco ativo | 5 anos em log compactado | Eliminação segura |

---

## 4. Política de Backups e Continuidade

1. **Backups Diários Automatizados**: Executados pelo Supabase com retenção contínua (PITR - Point-in-Time Recovery).
2. **Exportação Semanal de Segurança**: Dump estruturado dos dados armazenado em bucket seguro de nuvem da DNA Facilities.
3. **Recovery Time Objective (RTO)**: Menor que 2 horas para restauração de base.
4. **Recovery Point Objective (RPO)**: Menor que 24 horas (máxima perda aceitável em caso de desastre catastrófico).
