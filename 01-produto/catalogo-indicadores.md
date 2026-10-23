# Catálogo Centralizado de Indicadores (KPIs)
## Plataforma de Business Intelligence para Gestão de Facilities

Este catálogo é a referência matemática, metodológica e corporativa oficial para todos os cálculos do sistema. Nenhuma fórmula deve ser calculada de forma divergente das regras aqui estipuladas.

---

### Resumo do Catálogo

| Código | Nome do Indicador | Módulo | Unidade | Meta Padrão | Sentido Favorável |
|---|---|---|---|---|---|
| **IND-001** | Head Count — Atendimento do Efetivo | RH | % | 100,0% | Quanto mais próximo de 100%, melhor |
| **IND-002** | Taxa de Turnover (Rotatividade) | RH | % | <= 2,0% ao mês | Menor é melhor |
| **IND-003** | Taxa de Absenteísmo | RH | % | <= 3,5% ao mês | Menor é melhor |
| **IND-004** | HHT — Horas-Homem Trabalhadas | SMA | Horas (h) | Variável por escala | Informativo |
| **IND-005** | TFCA — Frequência de Acidentes c/ Afastamento | SMA | Taxa (por 1M h) | 0,00 | Menor é melhor (Zero Acidente) |
| **IND-006** | TFSA — Frequência de Acidentes s/ Afastamento | SMA | Taxa (por 1M h) | <= 2,00 | Menor é melhor |
| **IND-007** | Cumprimento de Inspeções Planejadas (IPS) | SMA | % | >= 95,0% | Maior é melhor |
| **IND-008** | Desvio Orçamentário Nominal | Orçamento | R$ | <= R$ 0,00 | Menor ou igual a zero (sem estouro) |
| **IND-009** | Consumo Percentual do Orçamento | Orçamento | % | 100,0% | Próximo a 100% (dentro do orçado) |
| **IND-010** | Saldo Orçamentário Disponível | Orçamento | R$ | >= R$ 0,00 | Maior ou igual a zero |
| **IND-011** | Valor Líquido Medido | Medição | R$ | = Valor Contratual | Maior é melhor |
| **IND-012** | Índice de Glosas Contratuais | Medição | % | <= 0,5% | Menor é melhor |
| **IND-013** | Lead Time do Ciclo de Medição | Medição | Dias | <= 15 dias | Menor é melhor |

---

### Fichas Técnicas Detalhadas

---

#### IND-001 — Atendimento do Efetivo (Head Count)
- **Código**: `IND-001`
- **Área Responsável**: Recursos Humanos / Operações
- **Descrição**: Relação percentual entre o número de colaboradores ativos prestando serviços e o quantitativo contratualmente acordado com o cliente.
- **Fórmula**:
  $$\text{Atendimento do Efetivo (\%)} = \left( \frac{\text{Head Count Realizado}}{\text{Head Count Contratual}} \right) \times 100$$
- **Unidade de Medida**: Percentual (`%`) com 1 casa decimal.
- **Periodicidade**: Mensal (apurado por competência ou diário por escala).
- **Fonte Primária**: Folha de pagamento / espelho de ponto / planilha de RH.
- **Tratamento de Exceções**:
  - Se $\text{Head Count Contratual} = 0$, retornar `0,0%` e registrar alerta de inconsistência cadastral.
  - Se $\text{Head Count Realizado} > \text{Head Count Contratual}$, indicar superávit operacional (> 100%).
- **Classificação de Status**:
  - 🟢 **Favorável**: $\ge 98,0\%$
  - 🟡 **Atenção**: $95,0\% \text{ a } 97,9\%$
  - 🔴 **Crítico**: $< 95,0\%$ (risco imediato de glosa contratual por falta de posto)

---

#### IND-002 — Taxa de Turnover (Rotatividade de Pessoal)
- **Código**: `IND-002`
- **Área Responsável**: Recursos Humanos
- **Descrição**: Percentual de movimentação de pessoal (entradas e saídas) em relação ao quadro médio de colaboradores no mês.
- **Fórmula Padrão de Facilities**:
  $$\text{Turnover (\%)} = \frac{\left( \frac{\text{Admissões} + \text{Desligamentos}}{2} \right)}{\text{Head Count Médio da Competência}} \times 100$$
  *Onde $\text{Head Count Médio} = \frac{\text{Efetivo Início do Mês} + \text{Efetivo Fim do Mês}}{2}$*.
- **Unidade de Medida**: Percentual (`%`) com 2 casas decimais.
- **Periodicidade**: Mensal.
- **Fonte Primária**: Relatório de movimentação de pessoal (admissões e demissões).
- **Tratamento de Exceções**:
  - Se $\text{Head Count Médio} = 0$, retornar `0,00%`.
  - Diferenciar desligamentos voluntários (iniciativa do colaborador) de involuntários (iniciativa da empresa) quando disponível na planilha.
- **Classificação de Status**:
  - 🟢 **Favorável**: $\le 2,50\%$
  - 🟡 **Atenção**: $2,51\% \text{ a } 4,00\%$
  - 🔴 **Crítico**: $> 4,00\%$ (alerta de custos de rescisão e risco de postos descobertos)

---

#### IND-003 — Taxa de Absenteísmo
- **Código**: `IND-003`
- **Área Responsável**: Recursos Humanos / Operações
- **Descrição**: Relação percentual entre o total de horas perdidas por ausências não planejadas e as horas totais planejadas de trabalho na escala.
- **Fórmula**:
  $$\text{Absenteísmo (\%)} = \left( \frac{\text{Horas de Ausência Não Previstas}}{\text{Horas Previstas de Trabalho}} \right) \times 100$$
  *Horas de Ausência consideradas: Faltas injustificadas + atestados médicos de curta duração + suspensões disciplinares + atrasos relevantes.*
- **Unidade de Medida**: Percentual (`%`) com 2 casas decimais.
- **Periodicidade**: Mensal.
- **Tratamento de Exceções**:
  - Férias regulamentares e licenças maternidade/paternidade **não** devem ser contabilizadas como absenteísmo não previsto, devendo ser computadas no contingente de afastamentos planejados.
- **Classificação de Status**:
  - 🟢 **Favorável**: $\le 3,00\%$
  - 🟡 **Atenção**: $3,01\% \text{ a } 5,00\%$
  - 🔴 **Crítico**: $> 5,00\%$

---

#### IND-004 — Horas-Homem Trabalhadas (HHT)
- **Código**: `IND-004`
- **Área Responsável**: Segurança, Meio Ambiente e Saúde (SMA)
- **Descrição**: Somatório total de horas efetivamente trabalhadas por todos os colaboradores sob o contrato no período, utilizado como base de exposição ao risco para os indicadores de acidentes.
- **Fórmula**:
  $$\text{HHT} = \sum (\text{Dias Efetivamente Trabalhados} \times \text{Jornada Diária de cada Colaborador}) + \text{Horas Extras Realizadas}$$
- **Unidade de Medida**: Horas inteiras (`h`).
- **Periodicidade**: Mensal e Acumulada (12 meses).
- **Classificação**: Indicador de base volumétrica (sem status de cor isolado).

---

#### IND-005 — Taxa de Frequência de Acidentes com Afastamento (TFCA)
- **Código**: `IND-005`
- **Área Responsável**: Segurança, Meio Ambiente e Saúde (SMA)
- **Descrição**: Mede o número de acidentes de trabalho com afastamento por milhão de horas-homem de exposição ao risco, em conformidade com a NBR 14280.
- **Fórmula**:
  $$\text{TFCA} = \frac{\text{Número de Acidentes com Afastamento} \times 1.000.000}{\text{HHT}}$$
- **Fator de Referência**: $1.000.000$ (padrão NBR 14280 / OIT).
- **Unidade de Medida**: Coeficiente numérico com 2 casas decimais.
- **Tratamento de Exceções**:
  - Se $\text{HHT} = 0$, retornar `0,00` e alertar a ausência de registro de horas.
  - Acidentes de trajeto devem ser contabilizados separadamente conforme exigência de contratos específicos.
- **Classificação de Status**:
  - 🟢 **Favorável**: $= 0,00$ (Zero Acidente)
  - 🔴 **Crítico**: $> 0,00$ (Qualquer acidente com afastamento é imediatamente crítico)

---

#### IND-006 — Taxa de Frequência de Acidentes sem Afastamento (TFSA)
- **Código**: `IND-006`
- **Área Responsável**: Segurança, Meio Ambiente e Saúde (SMA)
- **Descrição**: Mede o número de acidentes de trabalho sem perda de jornada por milhão de horas de exposição.
- **Fórmula**:
  $$\text{TFSA} = \frac{\text{Número de Acidentes sem Afastamento} \times 1.000.000}{\text{HHT}}$$
- **Classificação de Status**:
  - 🟢 **Favorável**: $\le 1,00$
  - 🟡 **Atenção**: $1,01 \text{ a } 2,50$
  - 🔴 **Crítico**: $> 2,50$

---

#### IND-007 — Cumprimento de Inspeções Planejadas de Segurança (IPS)
- **Código**: `IND-007`
- **Área Responsável**: Segurança, Meio Ambiente e Saúde (SMA)
- **Descrição**: Percentual de inspeções preventivas de segurança realizadas pelos supervisores em relação ao plano mensal pactuado.
- **Fórmula**:
  $$\text{Cumprimento IPS (\%)} = \left( \frac{\text{Inspeções Realizadas}}{\text{Inspeções Planejadas}} \right) \times 100$$
- **Classificação de Status**:
  - 🟢 **Favorável**: $\ge 95,0\%$
  - 🟡 **Atenção**: $85,0\% \text{ a } 94,9\%$
  - 🔴 **Crítico**: $< 85,0\%$

---

#### IND-008 e IND-009 — Desvio Orçamentário e Consumo Orçamentário
- **Códigos**: `IND-008` (Nominal R$) e `IND-009` (Percentual %)
- **Área Responsável**: Controladoria / Financeiro
- **Fórmulas**:
  $$\text{Desvio Nominal (R\$)} = \text{Valor Realizado} - \text{Valor Orçado}$$
  $$\text{Consumo Orçamentário (\%)} = \left( \frac{\text{Valor Realizado}}{\text{Valor Orçado}} \right) \times 100$$
  $$\text{Saldo Orçamentário (R\$)} = \text{Valor Orçado} - \text{Valor Realizado}$$
- **Interpretação**:
  - Desvio positivo indica estouro orçamentário (custo maior que o previsto);
  - Desvio negativo indica economia em relação ao orçamento planejado.
- **Classificação de Status**:
  - 🟢 **Favorável**: Consumo $\le 100,0\%$ (sem estouro)
  - 🟡 **Atenção**: Consumo entre $100,1\% \text{ e } 105,0\%$
  - 🔴 **Crítico**: Consumo $> 105,0\%$

---

#### IND-011 e IND-012 — Valor Líquido Medido e Índice de Glosas
- **Códigos**: `IND-011` e `IND-012`
- **Área Responsável**: Gestão de Contratos / Faturamento
- **Fórmulas**:
  $$\text{Valor Líquido Medido (R\$)} = \text{Valor Medido Bruto} - \text{Glosas Aplicadas} - \text{Descontos Pactuados}$$
  $$\text{Índice de Glosa (\%)} = \left( \frac{\text{Total de Glosas Aplicadas}}{\text{Valor Medido Bruto}} \right) \times 100$$
- **Classificação de Status**:
  - 🟢 **Favorável**: Glosa $\le 0,5\%$
  - 🟡 **Atenção**: Glosa entre $0,6\% \text{ e } 2,0\%$
  - 🔴 **Crítico**: Glosa $> 2,0\%$
