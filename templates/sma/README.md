# Guia de Preenchimento — Template de SMA
## Plataforma de Business Intelligence para Facilities (DNA Facilities)

### Colunas Obrigatórias:
1. `MES`: Mês de competência (ex: `Jan/26` ou `2026-01`).
2. `HHT`: Horas-Homem Trabalhadas acumuladas no contrato no período.
3. `ACIDENTES_COM_AFASTAMENTO`: Número de acidentes com afastamento (meta: 0).
4. `ACIDENTES_SEM_AFASTAMENTO`: Número de acidentes de trabalho leves sem perda de dia.
5. `ACIDENTES_TRAJETO`: Acidentes ocorridos no trajeto residência-trabalho.
6. `TFCA`: Taxa de frequência com afastamento (calculada automaticamente: `Acidentes * 1M / HHT`).
7. `TFSA`: Taxa de frequência sem afastamento (`Acidentes * 1M / HHT`).
8. `INSPECOES_PLANEJADAS`: Meta mensal de Inspeções Planejadas de Segurança (IPS).
9. `INSPECOES_REALIZADAS`: Inspeções preventivas efetivamente executadas.
10. `DESVIOS_REGISTRADOS`: Total de desvios e condições inseguras reportadas.
11. `DESVIOS_TRATADOS`: Total de desvios corrigidos com plano de ação finalizado.
