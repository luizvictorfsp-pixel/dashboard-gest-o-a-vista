# Plano de Testes e Garantia de Qualidade (QA)
## Plataforma de Business Intelligence para Facilities (DNA Facilities)

---

## 1. Pirâmide e Estratégia de Testes

```text
       /\
      /  \     Testes E2E (Playwright) — Fluxos críticos de login e navegação
     /────\
    /      \   Testes de Integração (Vitest + MSW) — API Supabase e Parsers
   /────────\
  /          \ Testes Unitários (Vitest) — Cálculos puros de KPIs (100% cobertura)
 └────────────┘
```

---

## 2. Níveis de Teste

### 2.1. Testes Unitários (Camada de Domínio / Cálculos)
- **Ferramenta**: `vitest`
- **Foco**: Funções puras de `src/lib/calculations/`.
- **Casos Obrigatórios**:
  - `calculateTurnover`: Cálculo regular, efetivo médio zero, admissões sem demissões, demissões sem admissões.
  - `calculateAbsenteeism`: Horas previstas zero, horas de ausência maiores que horas previstas, arredondamento percentual.
  - `calculateTFCA`: HHT zero (proteção contra divisão por zero), múltiplos acidentes, fator de referência 1.000.000.
  - `calculateBudgetVariance`: Variação positiva (estouro), variação negativa (economia), orçamento zero.
  - `calculateNetMeasurement`: Valor bruto menor que glosas, glosas zeradas, cálculo de percentual de glosa.

### 2.2. Testes de Integração (Parsers e Ingestão)
- **Foco**: Validação de arquivos via Zod e processamento XLSX/CSV.
- **Casos Obrigatórios**:
  - Upload de planilha válida de RH com 100 linhas processa sem erro.
  - Upload de arquivo com coluna ausente retorna lista detalhada de erros sem quebrar a aplicação.
  - Upload de arquivo com caracteres maliciosos ou formatação de data inválida é higienizado ou rejeitado com segurança.

### 2.3. Testes de Autorização e RLS
- **Foco**: Garantir que as políticas do Supabase barrem acessos indevidos.
- **Casos Obrigatórios**:
  - Usuário com role `user` tentando deletar dados na tabela `dashboard_data` recebe erro 403 / negação de RLS.
  - Gestor de Contrato tentando consultar dados de um contrato ao qual não está vinculado não recebe registros.
