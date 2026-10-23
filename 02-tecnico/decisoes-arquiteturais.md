# Registros de Decisões Arquiteturais (ADR)
## Plataforma de Business Intelligence para Facilities (DNA Facilities)

---

### ADR-001: Manutenção da Stack React + TypeScript + Vite + Tailwind CSS
- **Status**: Aprovado.
- **Contexto**: O projeto existente possui uma base sólida construída em Vite, React 18, TypeScript, Tailwind CSS e componentes shadcn/ui.
- **Decisão**: Manter a stack tecnológica base atual, sem reescrever ou migrar para outro framework (como Next.js).
- **Justificativa**: O sistema opera como um painel autenticado (B2B SaaS / Intranet corporativa), onde Server-Side Rendering (SSR) não é necessário para SEO. A agilidade de desenvolvimento, performance do bundle e compatibilidade com o código atual maximizam o retorno do investimento.
- **Consequências**: Manter a estrutura SPA hospedada em CDN (Vercel) consumindo APIs Supabase.

---

### ADR-002: Evolução do Modelo de Dados de JSON Blob para PostgreSQL Relacional
- **Status**: Proposto / Em Planejamento.
- **Contexto**: Atualmente, a tabela `dashboard_data` armazena planilhas inteiras em formato JSON dentro de uma única coluna `data`. Isso prejudica agregações, impede integridade referencial e limita filtros dinâmicos de múltiplos contratos.
- **Decisão**: Estruturar tabelas relacionais dedicadas (`contratos`, `competencias`, `rh_registros`, `sma_indicadores`, `orcamentos`, `boletins_medicao`) mantendo a tabela `dashboard_data` temporariamente como camada de transição e staging.
- **Justificativa**: Permite consultas analíticas em SQL de alta velocidade, validação de tipos a nível de banco de dados e aplicação de Row Level Security (RLS) granular por contrato e perfil.
- **Consequências**: Criação de migrações SQL sem perda dos dados históricos já cadastrados.

---

### ADR-003: Centralização das Fórmulas de Indicadores em Módulo de Domínio Puro
- **Status**: Aprovado.
- **Contexto**: Fórmulas de cálculo de turnover, absenteísmo e variações orçamentárias encontravam-se dispersas diretamente dentro dos componentes visuais de renderização (`KPICards.tsx`, `RHIndicators.tsx`).
- **Decisão**: Isolar 100% das fórmulas matemáticas e regras de cálculo em funções puras TypeScript dentro de `src/lib/calculations/` (ou `src/domain/calculations/`).
- **Justificativa**: Garante que o mesmo cálculo seja reutilizado na Visão Geral, nas páginas especializadas e nas rotinas de exportação, facilitando cobertura de testes automatizados unitários em 100%.
- **Consequências**: Componentes visuais apenas recebem dados já processados ou invocam a função pura centralizada.

---

### ADR-004: Ingestão Híbrida (Google Sheets via n8n + Upload Manual no Client)
- **Status**: Aprovado.
- **Contexto**: As operações corporativas de facilities utilizam planilhas compartilhadas no Google Drive mantidas pelos supervisores de campo, mas demandam também a capacidade de carregar arquivos avulsos imediatamente em reuniões ou contingências.
- **Decisão**: Adotar ingestão híbrida: suporte a sincronização programada/webhook via Google Sheets/n8n para operação contínua e manutenção do modal de Upload para envio manual de planilhas locais (.xlsx/.csv).
- **Justificativa**: Dá autonomia imediata ao gestor sem depender de agendamentos e estabelece a esteira de automação definitiva.
- **Consequências**: Ambos os canais de entrada devem utilizar o mesmo schema de validação para garantir consistência.
