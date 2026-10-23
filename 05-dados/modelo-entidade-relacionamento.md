# Modelo Entidade-Relacionamento (MER / DER)
## Plataforma de Business Intelligence para Facilities (DNA Facilities)

---

## 1. Diagrama Entidade-Relacionamento (Mermaid ER)

```mermaid
erDiagram
    CLIENTES ||--o{ CONTRATOS : "possui"
    CONTRATOS ||--o{ UNIDADES_OPERACIONAIS : "possui"
    CONTRATOS ||--o{ RH_REGISTROS : "registra mensalmente"
    CONTRATOS ||--o{ SMA_INDICADORES : "registra mensalmente"
    CONTRATOS ||--o{ ORCAMENTOS : "possui"
    CONTRATOS ||--o{ BOLETINS_MEDICAO : "gera"
    BOLETINS_MEDICAO ||--o{ BOLETIM_GLOSAS : "sofre"

    USERS ||--o{ USER_ROLES : "possui papel"
    USERS ||--o{ PROFILES : "tem perfil"
    USERS ||--o{ AUDIT_LOGS : "executa acoes"

    CONTRATOS {
        uuid id PK
        uuid cliente_id FK
        varchar codigo_contrato
        varchar nome_contrato
        numeric valor_mensal_contratual
        integer headcount_contratual
        boolean ativo
    }

    RH_REGISTROS {
        uuid id PK
        uuid contrato_id FK
        varchar competencia
        integer headcount_realizado
        integer admissoes
        integer desligamentos
        integer afastamentos
        integer ferias
        numeric taxa_turnover
        numeric taxa_absenteismo
    }

    SMA_INDICADORES {
        uuid id PK
        uuid contrato_id FK
        varchar competencia
        numeric hht
        integer acidentes_com_afastamento
        integer acidentes_sem_afastamento
        numeric tfca
        numeric tfsa
        integer inspecoes_planejadas
        integer inspecoes_realizadas
    }

    ORCAMENTOS {
        uuid id PK
        uuid contrato_id FK
        varchar competencia
        varchar categoria_despesa
        numeric valor_orcado
        numeric valor_realizado
        numeric variacao_percentual
    }

    BOLETINS_MEDICAO {
        uuid id PK
        uuid contrato_id FK
        varchar competencia
        varchar status
        numeric valor_contratual
        numeric valor_medido_bruto
        numeric total_glosas
        numeric valor_liquido_aprovado
        numeric valor_faturado
        numeric valor_recebido
    }

    BOLETIM_GLOSAS {
        uuid id PK
        uuid boletim_id FK
        varchar motivo_glosa
        varchar categoria_glosa
        numeric valor_glosa
    }

    AUDIT_LOGS {
        uuid id PK
        uuid user_id FK
        varchar action
        varchar entity_name
        uuid entity_id
        jsonb previous_state
        jsonb new_state
        timestamptz created_at
    }
```

---

## 2. Índices de Alta Performance Recomendados

Para manter tempo de resposta inferior a 200ms nas consultas do dashboard:

```sql
-- Índices para buscas rápidas por contrato e competência
CREATE INDEX IF NOT EXISTS idx_rh_contrato_comp ON public.rh_registros_competencia (contrato_id, competencia);
CREATE INDEX IF NOT EXISTS idx_sma_contrato_comp ON public.sma_indicadores (contrato_id, competencia);
CREATE INDEX IF NOT EXISTS idx_orc_contrato_comp ON public.orcamentos_competencia (contrato_id, competencia);
CREATE INDEX IF NOT EXISTS idx_bm_contrato_comp ON public.boletins_medicao (contrato_id, competencia);

-- Índice para trilha de auditoria cronológica
CREATE INDEX IF NOT EXISTS idx_audit_created ON public.audit_logs (created_at DESC);
```
