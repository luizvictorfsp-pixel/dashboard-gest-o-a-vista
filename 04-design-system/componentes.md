# Catálogo de Componentes Reutilizáveis
## Plataforma de Business Intelligence para Facilities (DNA Facilities)

Todos os componentes são fortemente tipados em TypeScript, modulares e construídos sobre primitivas do **Radix UI** estilizadas com Tailwind CSS.

---

## 1. Componente: `KPICard`

### 1.1. Finalidade
Renderizar um indicador de alto nível com ícone semântico, valor formatado, meta e indicador de tendência comparativo com a competência anterior.

### 1.2. Interface TypeScript
```typescript
export interface KPICardProps {
  id: string;
  title: string;
  value: string | number;
  unit?: string;
  target?: string | number;
  trend?: {
    value: number; // Percentual de variação (+3.5% ou -1.2%)
    direction: 'up' | 'down' | 'neutral';
    isFavorable: boolean; // Define se a direção é positiva para o negócio
  };
  status?: 'success' | 'warning' | 'error' | 'info' | 'neutral';
  icon: React.ComponentType<{ className?: string }>;
  tooltipDescription?: string;
  onClick?: () => void;
  className?: string;
}
```

---

## 2. Componente: `AnalyticalBarChart` (Gráfico de Barras)

### 2.1. Finalidade
Exibição de comparativos entre grandezas (ex: Orçado versus Realizado por categoria ou mês) utilizando a biblioteca **Recharts**.

### 2.2. Interface TypeScript
```typescript
export interface BarSeriesConfig {
  key: string;
  name: string;
  color: string;
  radius?: [number, number, number, number];
}

export interface AnalyticalBarChartProps {
  title: string;
  subtitle?: string;
  data: Array<Record<string, any>>;
  xAxisKey: string;
  series: BarSeriesConfig[];
  valueFormatter?: (value: number) => string;
  height?: number | string;
  enableLegend?: boolean;
  enableGrid?: boolean;
}
```

---

## 3. Componente: `AnalyticalLineChart` (Gráfico de Tendências Temporais)

### 3.1. Finalidade
Visualização da evolução histórica de taxas mensais (Turnover, Absenteísmo, HHT, TFCA) ao longo de 6 a 24 competências.

### 3.2. Interface TypeScript
```typescript
export interface LineSeriesConfig {
  key: string;
  name: string;
  strokeColor: string;
  strokeWidth?: number;
  strokeDasharray?: string;
  dot?: boolean;
}

export interface AnalyticalLineChartProps {
  title: string;
  subtitle?: string;
  data: Array<Record<string, any>>;
  xAxisKey: string;
  series: LineSeriesConfig[];
  targetLine?: {
    value: number;
    label: string;
    strokeColor: string;
  };
  valueFormatter?: (value: number) => string;
  height?: number | string;
}
```

---

## 4. Componente: `CompetenceSelector` (Seletor de Competência)

### 4.1. Finalidade
Barra de seleção mensal permanente no topo da aplicação, permitindo navegar pelo histórico de meses apurados.

### 4.2. Interface TypeScript
```typescript
export interface CompetenceOption {
  value: string; // Formato ISO "YYYY-MM" (ex: "2026-10")
  label: string; // Rótulo em PT-BR (ex: "Outubro / 2026")
  hasData: boolean; // Indica se existem dados importados para a competência
}

export interface CompetenceSelectorProps {
  selectedCompetence: string;
  availableCompetences: CompetenceOption[];
  onSelectCompetence: (competence: string) => void;
  isLoading?: boolean;
}
```

---

## 5. Componente: `StatusBadge` (Badge Semântico)

### 5.1. Finalidade
Etiqueta compacta para exibição imediata do status de aprovação de medições, desvios ou perfil de usuário.

```typescript
export interface StatusBadgeProps {
  variant: 'success' | 'warning' | 'error' | 'info' | 'neutral';
  label: string;
  icon?: React.ComponentType<{ className?: string }>;
  size?: 'sm' | 'md' | 'lg';
}
```
