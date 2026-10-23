# Estrutura do Projeto e Organização Modular
## Plataforma de Business Intelligence para Facilities (DNA Facilities)

---

## 1. Mapeamento da Raiz do Repositório

```text
c:\Antigravity\
├── dashboard-gestaoavista-main/   # APLICAÇÃO PRINCIPAL FUNCIONAL (Vite + React + TS)
│   ├── public/                   # Arquivos estáticos e ícones públicos
│   ├── src/                      # Código-fonte da aplicação React
│   │   ├── components/           # Componentes visuais
│   │   │   ├── dashboard/        # Componentes analíticos (Cards, Gráficos, Upload)
│   │   │   ├── ui/               # Primitivas shadcn/ui (Button, Dialog, Card, etc.)
│   │   │   ├── AccessControl.tsx # Gestão de usuários e permissões RBAC
│   │   │   └── ProtectedRoute.tsx# Guardião de rotas autenticadas
│   │   ├── hooks/                # Custom React Hooks (useAuth, useToast)
│   │   ├── integrations/         # Integração com Supabase (client e types)
│   │   ├── lib/                  # Utilitários, constantes e helpers
│   │   │   ├── accessFlags.ts    # Flags e labels de permissão em PT-BR
│   │   │   ├── supabase.ts       # Serviços de leitura e gravação no Supabase
│   │   │   └── utils.ts          # Utilitários gerais (cn para Tailwind)
│   │   ├── pages/                # Páginas de roteamento (Index, Auth, NotFound)
│   │   ├── App.tsx               # Configuração de rotas e providers
│   │   ├── index.css             # Design tokens e variáveis HSL do tema escuro
│   │   └── main.tsx              # Ponto de entrada React DOM
│   ├── supabase/                 # Infraestrutura de banco de dados
│   │   ├── functions/            # Supabase Edge Functions (Deno)
│   │   └── migrations/           # Histórico de scripts SQL migratórios
│   ├── package.json              # Dependências e scripts npm
│   ├── tailwind.config.ts        # Configurações do Tailwind CSS
│   └── vite.config.ts            # Configurações do Vite e plugins
├── docs/                         # DOCUMENTAÇÃO OFICIAL DO PROJETO (6 Pilares)
├── n8n/                          # Workflows de ingestão e automação (a expandir)
├── CODIGOS.txt                   # Instruções de setup e chaves operacionais
└── CHANGELOG.md                  # Histórico de mudanças da plataforma
```

> [!NOTE]
> A pasta `c:\Antigravity\src` na raiz contém uma estrutura esqueleto inicial. Para evitar confusão e garantir integridade, todo o desenvolvimento de código ativo deve concentrar-se dentro de `c:\Antigravity\dashboard-gestaoavista-main`.

---

## 2. Organização Proposta para a Pasta `src/`

Para acomodar os 6 novos módulos funcionais (SMA, Boletim de Medição, etc.) com separação rigorosa de responsabilidades, propõe-se a seguinte estrutura interna:

```text
src/
├── components/
│   ├── common/                  # Componentes compartilhados (Header, Sidebar, Filtros)
│   ├── dashboard/               # Cockpit executivo (Página A)
│   ├── rh/                      # Componentes especializados de RH (Página B)
│   ├── sma/                     # Componentes de SMA e Segurança (Página C)
│   ├── orcamento/               # Componentes de Orçamento e Custos (Página D)
│   ├── medicao/                 # Componentes de Boletim de Medição (Página E)
│   ├── relatorios/              # Componentes de Relatórios e Exportação (Página F)
│   ├── configuracoes/           # Gestão de Metas e Cadastros (Página G)
│   └── ui/                      # Biblioteca de primitivas de UI (shadcn)
├── domain/                      # Lógica pura de negócio e cálculos
│   ├── calculations/
│   │   ├── rh.ts                # turnover, absenteismo, atendimento_efetivo
│   │   ├── sma.ts               # tfca, tfsa, hht, cumprimento_ips
│   │   ├── financial.ts         # desvio_orcamentario, consumo_orcamento
│   │   └── measurement.ts       # valor_liquido, indice_glosa, lead_time
│   └── models/                  # Interfaces e tipos de domínio TypeScript
├── hooks/                       # Custom hooks para consumo de queries e filtros
│   ├── useAuth.tsx              # Autenticação e permissões
│   ├── useContracts.ts          # Seleção de contratos e competências
│   └── useDashboardMetrics.ts   # Carga e cálculo de métricas agregadas
├── integrations/
│   └── supabase/                # Cliente tipado do Supabase
├── services/                    # Camada de comunicação de rede
│   ├── contractService.ts
│   ├── ingestionService.ts
│   └── auditService.ts
└── pages/                       # Componentes de tela mapeados nas rotas
```
