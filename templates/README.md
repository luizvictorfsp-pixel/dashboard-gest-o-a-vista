# Modelos Oficiais de Planilhas de Entrada (Templates)
## Plataforma de Business Intelligence para Facilities (DNA Facilities)

Para garantir a ingestão segura, sem falhas de parsing e 100% automatizada, os arquivos de dados operacionais devem seguir rigorosamente a estrutura de colunas e tipos definidos nesta pasta.

---

## 📁 Estrutura dos Templates

1. **[Recursos Humanos (RH)](./rh/)**:
   - `template_rh.csv`: Registro de efetivo, admissões, desligamentos, férias, afastamentos, absenteísmo e turnover.
2. **[Segurança, Meio Ambiente e Saúde (SMA)](./sma/)**:
   - `template_sma.csv`: Apontamento de HHT, acidentes típicos/trajeto, inspeções planejadas (IPS) e desvios.
3. **[Orçamento e Custos](./orcamento/)**:
   - `template_orcamento.csv`: Valores orçados vs. realizados por categoria de despesa, UF e centro de custo.
4. **[Boletim de Medição e Faturamento](./boletim-medicao/)**:
   - `template_boletim_medicao.csv`: Ciclo de vida da medição, valores submetidos, glosas, faturados e recebidos.

---

## ⚠️ Regras Mandatórias de Preenchimento

- **Linha 1 (Cabeçalhos)**: Os nomes das colunas são sensíveis a maiúsculas/minúsculas e acentuação. Nunca altere a primeira linha do template.
- **Formato de Datas**: Sempre utilizar o padrão ISO `AAAA-MM-DD` ou `DD/MM/AAAA`.
- **Formato Numérico**: Valores monetários devem utilizar vírgula para decimais e ponto para milhares (ex: `15.450,00` ou `15450.00`).
- **Valores Percentuais**: Informar com símbolo `%` ou como número decimal puro (ex: `2,5%` ou `2.5`).
