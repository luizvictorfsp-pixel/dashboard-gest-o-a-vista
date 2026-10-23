# Requisitos Não Funcionais (RNF)
## Plataforma de Business Intelligence para Facilities (DNA Facilities)

Os requisitos não funcionais definem os atributos de qualidade, segurança, governança, desempenho e conformidade normativa do sistema.

---

### Resumo dos Requisitos Não Funcionais

| ID | Categoria | Descrição Síntese |
|---|---|---|
| **RNF-001** | Segurança da Informação | Autenticação via JWT, HTTPS obrigatório e proteção de credenciais |
| **RNF-002** | Privacidade e LGPD | Minimização de dados, proteção de registros de saúde e segregação |
| **RNF-003** | Desempenho e Latência | Carregamento inicial em até 2,0s; renderização de gráficos em até 500ms |
| **RNF-004** | Disponibilidade e Confiabilidade | SLA proposto de 99,5% com fallback para armazenamento local |
| **RNF-005** | Escalabilidade | Suporte a dezenas de contratos, milhares de colaboradores e histórico de 3 anos |
| **RNF-006** | Acessibilidade Digital | Conformidade com WCAG 2.1 nível AA e contraste de cores |
| **RNF-007** | Responsividade | Suporte pleno a desktops, notebooks e tablets (resolução >= 768px) |
| **RNF-008** | Manutenibilidade e Arquitetura | Separação estrita em camadas, TypeScript estrito e modularidade |
| **RNF-009** | Observabilidade e Telemetria | Logs estruturados, monitoramento de erros e métricas de sincronização |
| **RNF-010** | Integridade dos Dados | Validação via schemas Zod, idempotência e integridade referencial relacional |
| **RNF-011** | Compatibilidade de Plataformas | Navegadores modernos Chromium (Chrome/Edge), Firefox e Safari |
| **RNF-012** | Testabilidade e Qualidade | Cobertura de testes unitários para regras de cálculo de KPIs |

---

### Detalhamento dos Requisitos Não Funcionais

#### RNF-001 — Segurança da Informação
- **Descrição**: O tráfego de dados deve ser 100% criptografado em trânsito (TLS 1.3 / HTTPS) e em repouso (AES-256 no Supabase PostgreSQL).
- **Diretrizes Técnicas**:
  - Credenciais de serviço (ex: chaves do Google Cloud Service Account, segredos do Supabase Service Role) **nunca** devem ser entregues ao cliente frontend web.
  - Implementação de Row Level Security (RLS) mandatória em todas as tabelas públicas do Supabase.
  - Mitigação de vulnerabilidades OWASP Top 10: proteção contra Cross-Site Scripting (XSS), Cross-Site Request Forgery (CSRF) e injeção de SQL (via ORM/consultas parametrizadas).

#### RNF-002 — Privacidade e Proteção de Dados (LGPD — Lei 13.709/2018)
- **Descrição**: O sistema opera dados funcionais de prestação de serviços, exigindo conformidade rigorosa com os princípios de finalidade, necessidade e segurança da LGPD.
- **Diretrizes Técnicas**:
  - **Minimização**: Não armazenar números de documentos pessoais (CPF, RG, CNH) nem dados bancários a menos que estritamente justificável.
  - **Dados Sensíveis de Saúde/SMA**: Registros médicos de acidentes e laudos de afastamento são visíveis exclusivamente aos perfis de SMA e RH com auditoria de acesso.
  - **Exibição Agregada**: Para usuários de perfil diretivo e de consulta, indicadores de turnover e absenteísmo são exibidos agregados por função/setor, sem identificar nomes individuais desnecessariamente.

#### RNF-003 — Desempenho e Latência
- **Descrição**: A plataforma deve propiciar uma experiência fluida de análise de dados, mesmo sob grandes volumes de registros.
- **Metas Propostas (a serem validadas em homologação)**:
  - First Contentful Paint (FCP) <= 1,5 segundos em conexões 4G/banda larga padrão.
  - Tempo de resposta para consultas agregadas do dashboard <= 600ms via Supabase.
  - Transição de abas e filtragem interativa em memória <= 200ms.
  - Limite de processamento de planilhas locais: até 20.000 linhas processadas no browser ou backend em menos de 5 segundos.

#### RNF-004 — Disponibilidade e Recuperação de Falhas
- **Descrição**: O sistema deve operar com alta disponibilidade (proposta de 99,5% em horário comercial).
- **Mecanismos de Resiliência**:
  - Em caso de indisponibilidade temporária da nuvem Supabase, a interface deve permitir operação em modo somente-leitura com os dados persistidos no cache local (`localStorage` / `IndexedDB`).
  - Sincronização automática em background assim que a conectividade for restabelecida.

#### RNF-005 — Escalabilidade
- **Descrição**: A arquitetura de dados deve suportar o crescimento do volume de contratos sem degradação perceptível.
- **Capacidade Projetada**:
  - Até 100 contratos ativos simultâneos.
  - Até 15.000 colaboradores registrados na base.
  - Histórico transacional de até 36 competências consecutivas (3 anos).

#### RNF-006 — Acessibilidade Digital
- **Descrição**: A interface deve ser acessível e compreensível conforme os padrões WCAG 2.1 nível AA.
- **Critérios**:
  - Razão de contraste mínima de 4.5:1 para texto normal e 3:1 para textos grandes e elementos gráficos funcionais sobre o fundo escuro do tema DNA Facilities.
  - Não depender exclusivamente de cores para transmitir informações (ex: ícones de seta com indicação explícita além da cor verde/vermelha em variações de KPIs).
  - Suporte a navegação por teclado (foco visível) em botões, abas e modais.

#### RNF-007 — Responsividade
- **Descrição**: Layout fluido e adaptável a múltiplas resoluções corporativas.
- **Breakpoints Oficiais**:
  - Desktop Ultra-wide e Full HD: `>= 1440px` (Grid completa de 6 cards de KPIs lado a lado).
  - Notebook padrão: `1024px a 1439px` (Grid de 3 colunas de cards).
  - Tablets / Notebooks compactos: `768px a 1023px` (Grid de 2 colunas, navegação colapsável).
  - *Observação*: A operação administrativa principal é projetada prioritariamente para telas `>= 1024px`.

#### RNF-008 — Manutenibilidade e Arquitetura do Código
- **Descrição**: O código-fonte deve aderir a princípios Clean Code, modularidade e tipagem estrita.
- **Diretrizes**:
  - TypeScript em modo estrito (`strict: true`), proibindo o uso arbitrário de tipo `any` nas funções de cálculo de negócio.
  - Separação clara de responsabilidades: componentes de visualização não devem conter cálculos complexos de negócio nem chamadas de rede diretas.
  - Padronização de nomenclatura em português corporativo para o domínio de facilities e inglês para código técnico.

#### RNF-009 — Observabilidade e Monitoramento
- **Descrição**: A plataforma deve emitir logs estruturados e registrar telemetria de erros para diagnóstico rápido.
- **Requisitos**:
  - Erros em chamadas assíncronas capturados por Error Boundaries do React e exibição de mensagens claras ao usuário.
  - Registro de exceções de sincronização na tabela de auditoria com stack trace controlado (sem dados sensíveis).

#### RNF-010 — Integridade dos Dados e Idempotência
- **Descrição**: Nenhuma ingestão de dados pode corromper ou duplicar registros na base de dados.
- **Regras**:
  - Schemas de validação Zod aplicados antes de qualquer inserção no banco de dados.
  - Restrição de unicidade composta nas tabelas relacionais (ex: `UNIQUE(contrato_id, competencia, categoria)`).
  - Execuções de sincronização repetidas para o mesmo arquivo devem resultar no mesmo estado final estável (idempotência garantida).

#### RNF-011 — Compatibilidade de Plataformas
- **Navegadores Suportados**:
  - Google Chrome (últimas 3 versões maiores).
  - Microsoft Edge (últimas 3 versões maiores).
  - Mozilla Firefox (últimas 3 versões maiores).
  - Apple Safari (versão 16+).

#### RNF-012 — Testabilidade e Garantia de Qualidade
- **Descrição**: Os componentes essenciais de cálculo devem ser cobertos por testes automatizados executáveis em pipelines de CI.
- **Meta**: 100% de cobertura de testes unitários para a camada de cálculo de indicadores (`lib/calculations/`).
