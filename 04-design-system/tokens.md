# Tokens de Design (Design Tokens)
## Plataforma de Business Intelligence para Facilities (DNA Facilities)

Todas as cores e variáveis do sistema são definidas estritamente em **HSL (Hue, Saturation, Lightness)** para assegurar flexibilidade dinâmica, controle de contraste e harmonia com a biblioteca Tailwind CSS.

---

## 1. Paleta de Cores e Tokens HSL

### 1.1. Cores de Superfície e Fundo (DNA Facilities Theme)

```css
/* Definidas em src/index.css */
--background: 222 25% 8%;              /* Fundo principal escuro profundo (#0f141c) */
--foreground: 210 15% 95%;             /* Texto principal de alto contraste (#f0f3f6) */

--card: 222 20% 10%;                   /* Superfície de cards analíticos (#141923) */
--card-foreground: 210 15% 95%;

--popover: 222 20% 10%;                /* Superfície de modais e menus suspensos */
--popover-foreground: 210 15% 95%;

--border: 222 15% 25%;                 /* Bordas sutis de delimitação (#353e4f) */
--input: 222 15% 20%;                  /* Fundo de inputs e formulários */
--ring: 218 100% 60%;                  /* Anel de foco para acessibilidade */
```

### 1.2. Cores da Marca e Destaque (Brand Colors)

```css
--primary: 218 100% 65%;               /* Azul vibrante DNA Facilities (#4d8eff) */
--primary-foreground: 0 0% 100%;       /* Branco absoluto */

--secondary: 222 15% 15%;              /* Superfície secundária para tags e badges */
--secondary-foreground: 210 15% 85%;

--accent: 218 80% 25%;                 /* Realce profundo para itens selecionados */
--accent-foreground: 210 15% 95%;
```

### 1.3. Cores Semânticas de Status Operacional

| Status | Variável HSL | Valor Hex Aprox. | Aplicação / Regra de Negócio |
|---|---|---|---|
| **Sucesso (Verde)** | `--dashboard-success: 142 76% 45%` | `#1bb55c` | Metas atingidas, zero acidente, variação favorável de custo, aprovação de BM |
| **Atenção (Amarelo)** | `--dashboard-warning: 38 92% 55%` | `#f5a724` | Alerta de desvio, turnover acima do teto de aviso, inspeção próxima do prazo |
| **Crítico (Vermelho)** | `--dashboard-error: 0 72% 50%` | `#dc2626` | Ocorrência de acidente de trabalho, estouro orçamentário, glosas, falta de efetivo |
| **Informativo (Azul)**| `--dashboard-info: 218 100% 60%` | `#337eff` | Métricas de referência neutras, HHT acumulado, orçamento aprovado base |
| **Neutro (Cinza)**   | `--muted-foreground: 210 10% 60%`| `#929aa5` | Dados indisponíveis, períodos futuros não apurados, rótulos secundários |

---

## 2. Tipografia

- **Família Tipográfica Primária**: `Inter`, `Roboto`, `-apple-system`, `BlinkMacSystemFont`, `sans-serif`.
- **Escala de Tamanhos e Pesos**:
  - `H1 (Título de Página)`: `1.875rem (30px)` | Peso: `700 (Bold)`
  - `H2 (Títulos de Seção)`: `1.5rem (24px)` | Peso: `700 (Bold)`
  - `H3 (Títulos de Cards)`: `1.25rem (20px)` | Peso: `600 (Semi-bold)`
  - `KPI Numbers`: `1.75rem a 2.25rem` | Peso: `800 (Extra-bold)`
  - `Body Text (Corpo)`: `0.875rem (14px)` | Peso: `400 (Regular)`
  - `Caption / Rótulos`: `0.75rem (12px)` | Peso: `500 (Medium)`

---

## 3. Sombras, Elevação e Raios de Borda

```css
--radius: 0.75rem; /* 12px de raio para cards e modais modernos */

--shadow-card: 0 8px 32px -8px hsl(0 0% 0% / 0.3), 0 0 0 1px hsl(222 15% 18%);
--shadow-elevated: 0 16px 64px -12px hsl(0 0% 0% / 0.4), 0 0 0 1px hsl(218 100% 60% / 0.1);
--shadow-glow: 0 0 0 1px hsl(218 100% 60% / 0.15), 0 8px 32px hsl(218 100% 60% / 0.2);
```
