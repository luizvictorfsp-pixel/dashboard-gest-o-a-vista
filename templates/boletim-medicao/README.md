# Guia de Preenchimento — Template de Boletim de Medição
## Plataforma de Business Intelligence para Facilities (DNA Facilities)

### Colunas Obrigatórias:
1. `COMPETENCIA`: Mês e ano de referência no formato `AAAA-MM` (ex: `2026-10`).
2. `CONTRATO_CODIGO`: Código único de identificação do contrato.
3. `VALOR_CONTRATUAL`: Valor bruto acordado no contrato comercial.
4. `VALOR_MEDIDO`: Valor total apurado pela operação.
5. `VALOR_SUBMETIDO`: Valor submetido formalmente para aprovação do cliente.
6. `VALOR_APROVADO`: Valor final aceito pelo cliente após análise.
7. `VALOR_GLOSAS`: Somatório de deduções e penalidades aplicadas.
8. `MOTIVO_GLOSA`: Justificativa técnica circunstanciada das glosas.
9. `VALOR_FATURADO`: Valor nominal emitido na Nota Fiscal de Serviços (NFS-e).
10. `VALOR_RECEBIDO`: Valor efetivamente compensado na conta bancária da empresa.
11. `STATUS`: Situação atual no pipeline (`elaboracao`, `submetido`, `aprovado`, `faturado`, `recebido`).
12. `NUMERO_NF`: Número de identificação da Nota Fiscal emitida.
13. `DATA_SUBMISSAO`: Data de protocolo de envio do Boletim.
14. `DATA_APROVACAO`: Data do aceite formal emitido pelo cliente.
15. `DATA_RECEBIMENTO`: Data da efetiva liquidação financeira.
