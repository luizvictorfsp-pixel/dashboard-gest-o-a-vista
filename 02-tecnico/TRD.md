# TRD — Technical Requirements Document
## Plataforma de Business Intelligence para Facilities (DNA Facilities)

---

## 1. Visão Geral da Arquitetura Técnica

A plataforma **Gestão a Vista** é uma aplicação web moderna do tipo Single Page Application (SPA) desacoplada, integrando-se a serviços de nuvem gerenciados (Backend-as-a-Service — BaaS) com o **Supabase** (PostgreSQL, Auth, Storage, Edge Functions) e orquestração de dados com **Google Drive, Google Sheets e n8n**.

```text
┌──────────────────────────────────────────────────────────────────────────┐
│                             CLIENTE (FRONTEND)                           │
│  React 18 + TypeScript + Vite + Tailwind CSS + shadcn/ui + Recharts     │
└──────────────┬─────────────────────────────┬─────────────────────────────┘
               │ HTTPS / WSS                 │ HTTPS (REST)
               ▼                             ▼
┌──────────────────────────────┐  ┌────────────────────────────────────────┐
│     SUPABASE (POSTGRESQL)    │  │       SERVIÇO DE INGESTÃO (N8N)        │
│  - Autenticação (JWT)        │  │  - Webhook de Sincronização            │
│  - Row Level Security (RLS)  │  │  - Leitor do Google Sheets API         │
│  - Tabelas Relacionais       │  │  - Sanitizador e Validador             │
│  - Edge Functions (Deno)     │  │  - Carregador Idempotente (Upsert)     │
└──────────────────────────────┘  └──────────────────┬─────────────────────┘
                                                     │ Google Drive API
                                                     ▼
                                  ┌────────────────────────────────────────┐
                                  │   GOOGLE WORKSPACE (DRIVE / SHEETS)    │
                                  │  - Planilhas Operacionais dos Contratos│
                                  └────────────────────────────────────────┘
```

---

## 2. Stack Tecnológica Atual vs. Proposta Alvo

| Componente | Stack Atual Encontrada | Stack Alvo Proposta | Justificativa Técnica |
|---|---|---|---|
| **Linguagem Frontend** | TypeScript 5.5.3 | TypeScript 5.5.3 (Estrito) | Manter segurança de tipos em contratos de dados. |
| **Biblioteca UI** | React 18.3.1 | React 18.3.1 | Estabilidade, ecossistema e suporte a concorrência. |
| **Bundler & Build** | Vite 5.4.1 (SWC) | Vite 5.4.1 | Build ultra-rápido (HMR) e otimização de bundle. |
| **Estilização** | Tailwind CSS 3.4.11 | Tailwind CSS 3.4.11 + Design Tokens | Consistência com o tema escuro DNA Facilities. |
| **Componentes Base** | Radix UI (shadcn/ui) | Radix UI (shadcn/ui) | Acessibilidade nativa (a11y) e customização total. |
| **Visualização de Dados** | Recharts 3.1.0 | Recharts 3.1.0 | Componentes declarativos com suporte a SVG responsivo. |
| **Gerenciamento de Estado** | TanStack Query 5.56.2 + Context | TanStack Query 5.56.2 + Context | Cache assíncrono robusto, invalidação e revalidação. |
| **Persistência de Dados** | Supabase `dashboard_data` (JSONB) | PostgreSQL Relacional Normalizado | Sair de JSON genérico para tabelas tipadas e relacionais. |
| **Autenticação e RLS** | Supabase Auth + RLS | Supabase Auth + RBAC Granular | Suporte nativo aos 8 perfis e auditoria rigorosa. |
| **Ingestão de Dados** | Upload manual de planilha no client | Híbrido: n8n automático + Upload client | Automação via Google Sheets mantendo fallback manual. |

---

## 3. Padrões de Engenharia de Software

### 3.1. Clean Architecture e Separação em Camadas
1. **Camada de Apresentação (`src/components/`, `src/pages/`)**: Focada exclusivamente em renderização visual, acessibilidade e interatividade. Nenhum cálculo de fórmula ou chamada direta de banco deve residir nesta camada.
2. **Camada de Aplicação / Hooks (`src/hooks/`)**: Gerenciamento de estado de tela, orquestração de queries (TanStack Query) e gatilhos de eventos.
3. **Camada de Domínio / Regras de Negócio (`src/lib/calculations/`)**: Funções puras em TypeScript, sem efeitos colaterais, responsáveis pelas fórmulas dos indicadores (turnover, absenteísmo, TFCA, orçado x realizado). Testabilidade de 100%.
4. **Camada de Infraestrutura / Dados (`src/integrations/`, `src/services/`)**: Comunicação com APIs, clientes Supabase e adaptadores de planilhas.

### 3.2. Tratamento Consistente de Erros
- Utilização de `Result<T, E>` ou blocos `try/catch` tipados com emissão de notificações unificadas via `sonner` / `toaster`.
- Estados explícitos de UI: `isLoading`, `isError`, `isEmpty` e `isSuccess`.
- Proteção contra dados corrompidos: todos os inputs de planilhas e formulários passam por validação com schemas **Zod**.
