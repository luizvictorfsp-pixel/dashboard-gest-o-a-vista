# Gestão a Vista — Facilities BI Platform
## Documentação Técnica, de Produto e Arquitetura

Bem-vindo à documentação oficial da plataforma de Business Intelligence e Gestão de Contratos de Facilities da **DNA Facilities** (codinome de repositório: `accessguard-pro` / `dashboard-gestaoavista`).

Este repositório centraliza o conhecimento funcional, arquitetural, operacional e de governança do sistema, servindo como a **Single Source of Truth (SSOT)** para engenharia, produto, operações e diretoria.

---

## 🗂️ Estrutura da Documentação

A documentação está organizada em **6 Pilares Fundamentais** e guias complementares:

```text
docs/
├── README.md                                  # Visão geral e guia de navegação da documentação
├── 01-produto/                                # Pilar 1 — Requisitos de Negócio e Produto
│   ├── PRD.md                                 # Product Requirements Document mestre
│   ├── requisitos-funcionais.md               # RF-001 a RF-015 com critérios e dependências
│   ├── requisitos-nao-funcionais.md           # RNF-001 a RNF-012 (segurança, LGPD, performance)
│   ├── catalogo-indicadores.md                # Catálogo unificado de fórmulas, fontes e regras
│   └── criterios-de-aceitacao.md              # Critérios de aceitação BDD/Gherkin
├── 02-tecnico/                                # Pilar 2 — Engenharia e Arquitetura de Software
│   ├── TRD.md                                 # Technical Requirements Document mestre
│   ├── arquitetura.md                         # Diagnóstico atual vs Arquitetura Alvo corporativa
│   ├── estrutura-do-projeto.md                # Mapeamento do código-fonte e modularização
│   ├── integracoes.md                         # Google Sheets, Drive, n8n, Supabase e REST APIs
│   ├── seguranca.md                           # RBAC granular, RLS policies, LGPD e segredos
│   └── decisoes-arquiteturais.md              # Architecture Decision Records (ADRs)
├── 03-fluxos/                                 # Pilar 3 — Processos e Experiência do Usuário
│   ├── jornadas-usuario.md                    # Jornadas dos 8 perfis de usuário
│   ├── fluxo-atualizacao-dados.md             # Pipeline de ingestão, validação e resiliência
│   └── diagramas.md                           # Diagramas de arquitetura, sequência e estados
├── 04-design-system/                          # Pilar 4 — UX/UI e Design System
│   ├── design-system.md                       # Princípios visuais e diretrizes de usabilidade
│   ├── tokens.md                              # Paleta HSL, tipografia, espaçamentos e status
│   └── componentes.md                         # Catálogo de componentes tipados reutilizáveis
├── 05-dados/                                  # Pilar 5 — Banco de Dados e Modelagem
│   ├── modelo-dados.md                        # Modelagem relacional PostgreSQL (Supabase)
│   ├── dicionario-dados.md                    # Dicionário de tabelas, campos e restrições
│   ├── modelo-entidade-relacionamento.md      # Diagrama ER e integridade referencial
│   └── governanca-dados.md                    # Idempotência, versionamento e conformidade LGPD
├── 06-plano/                                  # Pilar 6 — Planejamento e Execução
│   ├── roadmap.md                             # Cronograma macro em 8 fases estruturadas
│   ├── backlog.md                             # Backlog priorizado (MoSCoW) com DoR e DoD
│   ├── plano-testes.md                        # Estratégia de testes unitários, integração e E2E
│   ├── implantacao.md                         # CI/CD, publicação, monitoramento e rollback
│   └── riscos-e-dependencias.md               # Matriz de riscos operacionais e contingências
├── operacao/                                  # Guias de Operação e Suporte
│   ├── instalacao.md                          # Guia de instalação e execução local
│   ├── configuracao-ambiente.md               # Gerenciamento de variáveis (.env) e permissões
│   ├── monitoramento.md                       # Logs, auditoria, observabilidade e telemetria
│   └── solucao-problemas.md                   # Guia de resolução de problemas (Troubleshooting)
└── templates/                                 # Padrões de Entrada Operacional (Planilhas)
    ├── README.md                              # Guia de preenchimento dos templates
    ├── rh/                                    # Template para registros de RH e efetivo
    ├── sma/                                   # Template para segurança, acidentes e inspeções
    ├── orcamento/                             # Template para custos, orçado x realizado
    └── boletim-medicao/                       # Template para faturamento, glosas e medições
```

---

## 🎯 Regras de Governança da Documentação

1. **Documentação Viva**: Toda alteração no modelo de dados, regra de negócio ou arquitetura de componentes deve ser refletida primeiro ou concomitantemente nestes documentos.
2. **Rastreabilidade**: Nenhum componente ou tela deve ser codificado sem referência explícita a um requisito funcional (`RF-xxx`) ou indicador do catálogo (`IND-xxx`).
3. **Não-duplicação**: Fórmulas e regras de cálculo não devem ser reescritas de formas divergentes; referencie sempre o [Catálogo de Indicadores](./01-produto/catalogo-indicadores.md).

---

## ✅ Status de Implementação (Roadmap — 8 Fases)
- **Fase 1-2**: Diagnóstico, Documentação e Arquitetura (Concluída)
- **Fase 3**: Fundação Técnica — Cálculos puros (`indicators.ts`), testes (`11/11`), SQL migrations (`20261016120000...`), seletor global (`ContractCompetenceSelector`) (Concluída)
- **Fase 4**: Fontes de Dados — Parsers Zod (`4/4` testes), webhook (`drive-webhook.ts`), upload múltiplo (`FileUpload.tsx`) (Concluída)
- **Fase 5**: Dashboards Especializados — Módulos A-G (`cockpit`, `rh`, `sma`, `orcamento`, `medicao`, `relatorios`, `configuracoes`) (Concluída)
- **Fase 6**: Testes Integrados — Regras de negócio (`integration.test.ts`), RBAC/RLS (`rbac.test.ts`) (Concluída)
- **Fase 7**: Homologação Operacional — Plano de carga de dados, metas contratuais, tolerâncias (`homologacao-fase7.md`) (Concluída)
- **Fase 8**: Implantação e Go-Live — Check-list de produção, migrações finais, monitoramento (`implantacao.md`, `monitoramento-pos-go-live.md`) (Concluída)

**Todas as fases implementadas com: testes executados, erros corrigidos, documentação atualizada.**
