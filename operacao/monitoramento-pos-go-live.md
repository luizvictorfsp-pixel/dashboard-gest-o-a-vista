# Monitoramento e Observabilidade — Pós Go-Live

Referência: docs/operacao/monitoramento.md

## Logs Ativados
- Erros de autenticação (Supabase Auth)
- Falhas de ingestão (parsers Zod)
- Performance de cálculos (indicators)

## Alertas
- Falha no webhook de ingestão (n8n / Edge Function)
- Valores de indicadores fora das tolerâncias definidas na Fase 7
