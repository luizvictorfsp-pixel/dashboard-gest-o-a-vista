# Requisitos Funcionais do Sistema (RF)
## Plataforma de Business Intelligence para Facilities (DNA Facilities)

A especificação de requisitos utiliza convenções rastreáveis e priorização MoSCoW (**Must have**, **Should have**, **Could have**, **Won't have**).

---

### Tabela de Rastreabilidade Resumida

| ID | Título | Prioridade | Módulo Relacionado |
|---|---|---|---|
| **RF-001** | Autenticação e Controle de Sessão | Must | Segurança / Auth |
| **RF-002** | Seleção de Contrato e Competência | Must | Global / Header |
| **RF-003** | Exibição de Cards de KPIs Principais | Must | Visão Geral / Módulos |
| **RF-004** | Filtros Globais Unificados | Must | Navegação Global |
| **RF-005** | Filtros Específicos por Módulo | Should | RH / SMA / Fin / BM |
| **RF-006** | Integração com Google Sheets e Drive | Must | Integrações / Ingestão |
| **RF-007** | Pipeline de Atualização e Sincronização | Must | Ingestão de Dados |
| **RF-008** | Navegação em Histórico Mensal e Tendências | Must | Relatórios / Gráficos |
| **RF-009** | Exportação de Dados e Relatórios | Should | Relatórios Gerenciais |
| **RF-010** | Administração de Metas e Parâmetros | Should | Configurações |
| **RF-011** | Gestão e Resolução de Desvios Operacionais | Should | SMA / Operações |
| **RF-012** | Acompanhamento do Boletim de Medição | Must | Financeiro / Medição |
| **RF-013** | Controle de Acesso Baseado em Perfis (RBAC) | Must | Governança / Admin |
| **RF-014** | Registro de Falhas de Integração e Resiliência | Must | Observabilidade |
| **RF-015** | Trilha de Auditoria de Operações Críticas | Should | Governança / Compliance |

---

### Detalhamento dos Requisitos Funcionais

#### RF-001 — Autenticação e Controle de Sessão
- **Descrição**: O sistema deve permitir que usuários autentiquem-se por meio de e-mail e senha com suporte a tokens JWT (Supabase Auth). A sessão deve expirar por inatividade e suportar renovação automática (refresh token).
- **Prioridade**: Must Have.
- **Dependências**: Nenhuma.
- **Critérios de Aceitação**:
  - Usuário com credenciais válidas acessa o sistema de acordo com suas permissões.
  - Credenciais inválidas exibem mensagem amigável sem revelar detalhes técnicos.
  - Tentativas sucessivas de erro devem acionar bloqueio temporário por rate limiting.
- **Estratégia de Teste**: Testes unitários com mocks de autenticação; testes E2E simulando login correto, senha inválida e expiração de token.

#### RF-002 — Seleção de Contrato e Competência
- **Descrição**: O usuário deve poder alternar entre contratos autorizados e selecionar o mês/ano de referência (competência) em um seletor permanente no topo da interface.
- **Prioridade**: Must Have.
- **Dependências**: RF-001, RF-013.
- **Critérios de Aceitação**:
  - A troca de contrato ou competência atualiza reativamente todos os KPIs e gráficos da tela sem recarregar a página inteira.
  - Usuários com acesso a apenas 1 contrato têm o seletor travado ou pré-selecionado automaticamente.
  - Persistência da última seleção do usuário na sessão ativa.
- **Estratégia de Teste**: Testes de componente verificando disparos de atualização de estado global e reatividade dos gráficos.

#### RF-003 — Exibição de Cards de KPIs Principais
- **Descrição**: Renderizar cards executivos com valor numérico/monetário formatado, ícone representativo, meta associada e indicador de tendência comparativo com a competência anterior.
- **Prioridade**: Must Have.
- **Dependências**: RF-002.
- **Critérios de Aceitação**:
  - Valores monetários em padrão BRL (`R$ #.##0,00`).
  - Percentuais formatados com uma casa decimal e sinal indicativo (+ / -).
  - Regra semântica de cores: valores desfavoráveis em vermelho/laranja e favoráveis em verde (ex: turnover baixo = verde; consumo excessivo de orçamento = vermelho).
- **Estratégia de Teste**: Testes unitários de renderização com diferentes mocks de dados (positivos, nulos, zeros, negativos).

#### RF-004 — Filtros Globais Unificados
- **Descrição**: Disponibilizar filtro unificado de Unidade Operacional, Linha de Serviço e Período no cabeçalho ou barra superior persistente.
- **Prioridade**: Must Have.
- **Dependências**: RF-002.
- **Critérios de Aceitação**:
  - Ao aplicar um filtro global, todas as abas e componentes da tela atual respeitam a seleção.
  - Possibilidade de limpar todos os filtros com um único clique.
- **Estratégia de Teste**: Testes de integração simulando múltiplos filtros concomitantes.

#### RF-005 — Filtros Específicos por Módulo
- **Descrição**: Prover filtros secundários contextuais em cada módulo (ex: por Cargo no RH, por Tipo de Evento no SMA, por Centro de Custo no Orçamento).
- **Prioridade**: Should Have.
- **Dependências**: RF-004.
- **Critérios de Aceitação**:
  - O filtro específico afeta somente os gráficos e tabelas do módulo correspondente, mantendo o contexto global preservado.
- **Estratégia de Teste**: Testes de componente isolados para cada página.

#### RF-006 — Integração com Google Sheets e Google Drive
- **Descrição**: O sistema deve permitir a ingestão de dados oriundos de planilhas padronizadas hospedadas no Google Drive ou Google Sheets, bem como upload manual de contingência (.xlsx / .csv).
- **Prioridade**: Must Have.
- **Dependências**: Nenhuma.
- **Critérios de Aceitação**:
  - Autenticação com Google Cloud via Service Account ou Webhook intermediário (n8n).
  - Nenhuma credencial privada de API deve estar exposta no client frontend.
  - Suporte a upload manual de arquivos com validação rigorosa de cabeçalhos e tipos de dados.
- **Estratégia de Teste**: Testes unitários com fixtures de planilhas bem formatadas e corrompidas; teste de contrato de integração.

#### RF-007 — Pipeline de Atualização e Sincronização
- **Descrição**: O processo de atualização deve extrair, validar, sanitizar e persistir os registros de forma idempotente.
- **Prioridade**: Must Have.
- **Dependências**: RF-006.
- **Critérios de Aceitação**:
  - Repetir a importação da mesma competência atualiza os dados sem duplicar linhas.
  - Falhas parciais de leitura não devem apagar os dados válidos anteriores da competência (rollback ou isolamento de versão).
  - Notificação visual do status de sincronização e timestamp da última carga com sucesso.
- **Estratégia de Teste**: Testes de integração simulando falhas de rede no meio da carga e verificando consistência do banco de dados.

#### RF-008 — Histórico Mensal e Análise de Tendências
- **Descrição**: Exibir séries temporais de até 12 a 24 competências retroativas para identificação de tendências sazonais e curvas de consumo.
- **Prioridade**: Must Have.
- **Dependências**: RF-002, RF-007.
- **Critérios de Aceitação**:
  - Gráficos de linha e barra ordenados cronologicamente.
  - Tooltip customizado com detalhamento de variação em relação ao mês anterior.
- **Estratégia de Teste**: Teste de ordenação de datas e tratamento de meses faltantes na série.

#### RF-009 — Exportação de Relatórios
- **Descrição**: Exportar os dados visualizados em tela e tabelas completas para arquivos em formato Excel (.xlsx), CSV estruturado e impressão/PDF.
- **Prioridade**: Should Have.
- **Dependências**: RF-003, RF-008.
- **Critérios de Aceitação**:
  - O arquivo exportado deve conter cabeçalhos explicativos e respeitar os filtros atualmente aplicados pelo usuário.
  - Não exportar campos restritos por perfil (LGPD).
- **Estratégia de Teste**: Teste de geração e validação de schema do binário exportado.

#### RF-010 — Administração de Metas e Parâmetros
- **Descrição**: Usuários com permissão administrativa ou de gestão devem poder cadastrar e atualizar metas contratuais por competência (ex: teto de absenteísmo, meta de HHT, verba orçamentária aprovada).
- **Prioridade**: Should Have.
- **Dependências**: RF-013.
- **Critérios de Aceitação**:
  - Formulário com validação de limites (valores não negativos, percentuais entre 0 e 100).
  - Histórico de versões das metas salvas com identificação do autor e timestamp.
- **Estratégia de Teste**: Validação com React Hook Form + Zod e testes de mutação.

#### RF-011 — Gestão e Resolução de Desvios Operacionais
- **Descrição**: Permitir registrar, acompanhar e encerrar apontamentos de desvios operacionais e de segurança, com classificação de severidade (Baixa, Média, Alta, Crítica) e plano de ação.
- **Prioridade**: Should Have.
- **Dependências**: RF-002.
- **Critérios de Aceitação**:
  - Cada desvio possui ID único, data de abertura, responsável, prazo acordado e status (Aberto, Em Tratamento, Concluído, Vencido).
  - Alerta visual no cockpit para desvios críticos ou com prazo expirado.
- **Estratégia de Teste**: Teste de fluxo de transição de estados da entidade Desvio.

#### RF-012 — Acompanhamento do Boletim de Medição
- **Descrição**: Acompanhar o fluxo financeiro de cada competência segregando Valor Medido, Valor Submetido, Glosas Aplicadas, Valor Aprovado, Faturado e Recebido.
- **Prioridade**: Must Have.
- **Dependências**: RF-002.
- **Critérios de Aceitação**:
  - Campo obrigatório de justificativa técnica e categoria ao lançar qualquer glosa.
  - Cálculo automático de saldo remanescente a receber e dias de atraso na aprovação ou pagamento.
- **Estratégia de Teste**: Testes matemáticos de consistência: `Valor Líquido = Valor Medido - Glosas`.

#### RF-013 — Controle de Acesso Baseado em Perfis (RBAC)
- **Descrição**: O sistema deve restringir o acesso a módulos, telas, botões de ação (Upload, Exportar, Deletar) e dados conforme o perfil atribuído ao usuário autenticado.
- **Prioridade**: Must Have.
- **Dependências**: RF-001.
- **Critérios de Aceitação**:
  - Componentes e rotas bloqueadas não devem ser renderizados nem acessíveis via URL direta.
  - Políticas RLS no banco de dados garantem proteção contra manipulação via chamadas diretas de API.
- **Estratégia de Teste**: Testes com matriz de perfis executando chamadas autenticadas como cada um dos 8 perfis.

#### RF-014 — Registro de Falhas de Integração e Resiliência
- **Descrição**: Toda inconsistência em arquivos de planilha (colunas ausentes, valores corrompidos, linhas em branco) deve ser logada detalhadamente em painel de administração.
- **Prioridade**: Must Have.
- **Dependências**: RF-006, RF-007.
- **Critérios de Aceitação**:
  - Relatório de erros indicando linha exata, coluna e motivo da rejeição do registro.
  - O restante dos registros válidos da planilha deve ser aproveitado se configurada a importação tolerante.
- **Estratégia de Teste**: Ingestão de arquivos de teste contendo deliberadamente erros de tipagem e linhas corrompidas.

#### RF-015 — Trilha de Auditoria de Operações Críticas
- **Descrição**: Registrar no banco de dados todas as ações que impactem dados operacionais ou financeiros (criação de usuário, alteração de permissão, upload de planilhas, alteração de metas, lançamento de glosas).
- **Prioridade**: Should Have.
- **Dependências**: RF-001, RF-013.
- **Critérios de Aceitação**:
  - Log contendo: `user_id`, `ação`, `tabela_afetada`, `dados_anteriores`, `dados_novos`, `ip_address`, `timestamp`.
  - Imutabilidade da tabela de logs de auditoria (apenas INSERT autorizado via RLS).
- **Estratégia de Teste**: Execução de ações críticas e verificação de inserção correspondente na tabela de auditoria.
