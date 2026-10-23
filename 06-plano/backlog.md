# Backlog Priorizado de Tarefas de Engenharia
## Plataforma de Business Intelligence para Facilities (DNA Facilities)

Todas as tarefas seguem o padrão com ID, Descrição, Prioridade MoSCoW, Dependências, Módulos Afetados, Critérios de Conclusão (DoD) e Status.

---

### Tabela de Tarefas Priorizadas

| Task ID | Descrição da Tarefa | Prioridade | Módulo | Dependências | Status |
|---|---|---|---|---|---|
| **TSK-001** | Diagnóstico do código e mapeamento do repositório | Must | Geral | Nenhuma | Concluído ✅ |
| **TSK-002** | Criação da documentação viva dos 6 Pilares na pasta `docs/` | Must | Docs | TSK-001 | Concluído ✅ |
| **TSK-003** | Módulo de domínio: cálculos puros (`src/lib/calculations/`) | Must | Domínio | TSK-002 | Pronto p/ Iniciar |
| **TSK-004** | Testes unitários para cálculos de turnover, absenteísmo e SMA | Must | Testes | TSK-003 | Pendente |
| **TSK-005** | Migração SQL das tabelas relacionais no Supabase | Must | Banco | TSK-002 | Pendente |
| **TSK-006** | Seletor Global permanente de Contrato e Competência | Must | UI / Header | TSK-005 | Concluída |
| **TSK-007** | Templates CSV padronizados para RH, SMA, Custos e BM | Must | Templates | TSK-002 | Pronto p/ Iniciar |
| **TSK-008** | Validador Zod e parser de arquivos no upload | Must | Ingestão | TSK-007 | Pendente |
| **TSK-009** | Implementação do Dashboard de SMA (Página C) | Must | SMA | TSK-003, TSK-005 | Pendente |
| **TSK-010** | Implementação do Dashboard de Boletim de Medição (Página E) | Must | Medição | TSK-003, TSK-005 | Pendente |
| **TSK-011** | Refatoração e aprimoramento do Painel de RH (Página B) | Should | RH | TSK-003 | Pendente |
| **TSK-012** | Refatoração do Painel de Orçamento e Custos (Página D) | Should | Orçamento | TSK-003 | Pendente |
| **TSK-013** | Painel de Relatórios Gerenciais e Exportação Excel (Página F)| Should | Relatórios | TSK-009, TSK-010 | **Concluído ✅** |
| **TSK-014** | Tela de Configuração de Metas Contratuais (Página G) | Should | Configurações | TSK-005 | **Concluído ✅** |
| **TSK-015** | Integração programada com Google Sheets via webhook | Could | Ingestão | TSK-008 | Pendente |
| **TSK-016** | Homologação com dados piloto e validação com gestores | Must | QA | TSK-009, TSK-010 | Pendente |
| **TSK-017** | Validação de produção e publicação oficial na Vercel | Must | DevOps | TSK-016 | Pendente |

---

### Definição de Conclusão (Definition of Done — DoD)
Uma tarefa só é marcada como **Concluída** quando:
1. O código estiver escrito em TypeScript estrito sem erros de compilação ou linting (`npm run lint`).
2. Os critérios de aceitação específicos do requisito foram verificados.
3. Testes unitários ou de integração aplicáveis foram executados com sucesso.
4. A documentação em `docs/` foi atualizada se houver impacto arquitetural ou de modelo de dados.
5. A alteração não causou regressão nas funcionalidades pré-existentes.
