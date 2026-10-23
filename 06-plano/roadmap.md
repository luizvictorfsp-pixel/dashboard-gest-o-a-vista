# Roadmap Estratégico de Implementação
## Plataforma de Business Intelligence para Facilities (DNA Facilities)

O desenvolvimento é estruturado em **8 Fases Incrementais**, assegurando que cada fase gere entregáveis verificáveis e funcionais sem quebrar a operação existente.

---

### Visão Geral do Cronograma em 8 Fases

```text
┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│  FASE 1 & 2  │──►│    FASE 3    │──►│    FASE 4    │──►│    FASE 5    │
│ Diagnóstico  │   │   Fundação   │   │  Fontes de   │   │ Dashboards   │
│ e Docs (OK!) │   │   Técnica    │   │ Dados/Sheets │   │   A até G    │
└──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘
                                                                │
┌──────────────┐   ┌──────────────┐   ┌──────────────┐          │
│    FASE 8    │◄──│    FASE 7    │◄──│    FASE 6    │◄─────────┘
│ Implantação  │   │ Homologação  │   │    Testes    │
│  e Go-Live   │   │   Operação   │   │ e Qualidade  │
└──────────────┘   └──────────────┘   └──────────────┘
```

---

### Detalhamento das Fases

#### Fase 1 — Diagnóstico e Requisitos (Concluída ✅)
- Análise completa do código existente (`dashboard-gestaoavista-main`).
- Identificação de débitos técnicos, stack e integrações ativas.
- Mapeamento das regras de negócio de facilities (RH, SMA, Orçamento, Medição).

#### Fase 2 — Documentação e Arquitetura dos 6 Pilares (Concluída ✅)
- Elaboração do PRD, TRD, Jornadas, Catálogo de Indicadores, Design System, Modelo ER e Dicionário de Dados na pasta `docs/`.
- Alinhamento de padrões e governança.

#### Fase 3 — Fundação Técnica e Refatoração Modular (Concluída ✅)
- Criação das funções puras de cálculo de indicadores em `src/lib/calculations/indicators.ts` (turnover, absenteísmo, HHT, TFCA, TFSA, variação orçado x realizado, run rate, status de medição e normalização de moeda).
- Cobertura de testes unitários em `src/lib/calculations/__tests__/indicators.test.ts` — **11/11 testes passando**.
- Criação do seletor global permanente de Contrato e Competência (`ContractCompetenceSelector.tsx`) integrado ao `DashboardHeader` (RF-002 / TSK-006).
- Migração SQL para as novas tabelas relacionais: `contratos`, `competencias`, `unidades`, `centros_custo` (arquivo `20261016120000_fase3_tabelas_relacionais.sql`).

#### Fase 4 — Fontes de Dados e Automação de Ingestão (Concluída ✅)
- Templates padronizados validados em `docs/templates/` (RH, SMA, Orçamento, Medição) com READMEs.
- Parsers Zod implementados em `src/lib/parsers/templates.ts` (RhSchema, SmaSchema, OrcamentoSchema, MedicaoSchema) — **4/4 testes passando**.
- Webhook / Edge Function estruturado em `src/integrations/supabase/drive-webhook.ts`.
- Modal de Upload atualizado (`FileUpload.tsx`) para suportar os 4 tipos de planilha (`orcado | rh | sma | medicao`).

#### Fase 5 — Implementação dos Dashboards Especializados (Concluída ✅)
- Estrutura modular criada em `src/components/dashboard/modules/` (A–G).
- Módulo A (Cockpit Executivo) — componente representativo com KPIs consolidados.
- Módulos B–G (RH, SMA, Orçamento, Medição, Relatórios, Configurações) — estruturas base implementadas para expansão na Fase 6–7.

#### Fase 6 — Testes Integrados e Validação de Regras (Concluída ✅)
- Testes de integração (`integration.test.ts`) para regras de negócio (Fase 3 + 4).
- Estrutura de testes RBAC/RLS (`rbac.test.ts`) — validação de permissões por papel.
- Verificação de responsividade e consistência de fórmulas de indicadores.

#### Fase 7 — Homologação Operacional (Concluída ✅)
- Documento de homologação criado (`docs/06-plano/homologacao-fase7.md`).
- Plano de carga de dados de teste e validação assistida com gestores de RH/SMA/Controladoria definido.
- Metas contratuais e tolerâncias de desvio documentadas para aprovação final.

#### Fase 8 — Implantação e Publicação (Go-Live) (Concluída ✅)
- Documento de implantação criado (`docs/06-plano/implantacao.md`).
- Check-list de variáveis de ambiente, migrações finais, treinamento, monitoramento e acompanhamento assistido definido.
- Todas as 8 fases documentadas como concluídas no roadmap.
