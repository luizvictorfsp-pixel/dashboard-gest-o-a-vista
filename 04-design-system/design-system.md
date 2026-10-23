# Design System — Princípios Visuais e Experiência do Usuário (UX/UI)
## Plataforma de Business Intelligence para Facilities (DNA Facilities)

---

## 1. Identidade Visual e Filosofia de Design

O sistema **Gestão a Vista** foi projetado para transmitir autoridade corporativa, precisão analítica e sofisticação visual, posicionando a **DNA Facilities** no mais alto patamar de gestão de facilities no Brasil.

### Princípios Norteadores:
1. **Clareza Informacional acima de Ornamento**: Cada elemento visual deve ter uma finalidade semântica. Gráficos e números devem responder a dúvidas operacionais sem ruído cognitivo.
2. **Tema Dark Corporativo Sofisticado**: Tons escuros profundos (baseados em HSL azul-marinho profundo: `222 25% 8%`) reduzem a fadiga ocular em salas de controle e operações diárias, destacando dados de alto contraste.
3. **Cores com Função Semântica Rígida**: O uso de cores primárias e de status é restrito e intencional. Cores não devem ser usadas como decoração arbitrária.
4. **Hierarquia Visual Escaneável**: O usuário deve conseguir entender a situação do contrato em menos de 5 segundos de observação (visão de cockpit).

---

## 2. Padrão Estrutural de Telas (Layout Architecture)

Todas as telas da plataforma seguem um grid padronizado:

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ [LOGO] GESTÃO A VISTA — DNA FACILITIES    [Usuário / Perfil] [Ações Globais]│
├─────────────────────────────────────────────────────────────────────────────┤
│ FILTROS: [Seletor de Contrato] | [Competência: Out/2026] | [Unidade: Todas] │
├─────────────────────────────────────────────────────────────────────────────┤
│ KPI CARDS (Até 6 cards horizontais com valor, meta e indicador de tendência)│
│ [Total Orçado] [Realizado] [Variação] [Efetivo] [Absenteísmo] [Turnover]   │
├─────────────────────────────────────────────────────────────────────────────┤
│ ABAS DO MÓDULO: [Visão Geral] [RH] [SMA] [Orçamento] [Medição] [Relatórios] │
├─────────────────────────────────────────────────────────────────────────────┤
│ CONTEÚDO ANALÍTICO:                                                         │
│ ┌──────────────────────────────────┐ ┌──────────────────────────────────┐   │
│ │ Gráfico Principal (ex: Evolução) │ │ Gráfico Composição / Pizza       │   │
│ └──────────────────────────────────┘ └──────────────────────────────────┘   │
│ ┌───────────────────────────────────────────────────────────────────────┐   │
│ │ Tabela de Detalhamento / Registros com Paginação e Ordenação          │   │
│ └───────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Estados Visuais de Interface

Todo componente que lida com requisições assíncronas deve contemplar 4 estados visuais explícitos:
1. **Carregando (Loading)**: Esqueletos animados de layout (`Skeleton`) ou spinner elegante; nunca deixar telas em branco durante a busca de dados.
2. **Dados Ausentes (Empty State)**: Ilustração ou ícone minimalista com mensagem instrutiva e botão de ação direta (ex: *"Nenhum dado importado para esta competência. [Importar Planilha]"*).
3. **Erro (Error State)**: Card com borda vermelha suave, ícone de alerta, descrição legível do problema e botão de *"Tentar Novamente"*.
4. **Sucesso (Populated State)**: Gráficos e cards renderizados com animações suaves de transição (`framer-motion` ou CSS transitions).
