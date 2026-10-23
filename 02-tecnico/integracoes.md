# Especificação Técnica de Integrações e APIs
## Plataforma de Business Intelligence para Facilities (DNA Facilities)

---

## 1. Visão Geral das Integrações

A plataforma suporta duas modalidades de entrada de dados:
1. **Pipeline Automatizado**: Integração periódica com Google Sheets / Google Drive via automação no **n8n** ou Supabase Edge Functions.
2. **Ingestão Manual de Contingência**: Upload de arquivos `.xlsx` e `.csv` diretamente pela interface do usuário (com sanitização e validação no navegador/servidor).

---

## 2. Integração com Google Sheets e Google Drive

### 2.1. Arquitetura de Segurança da Integração
- **Princípio Fundamental**: Credenciais de API (Service Accounts, tokens OAuth) **nunca** devem trafegar até o navegador do usuário final.
- **Mecanismo Recomendado**:
  - Uma Service Account no Google Cloud Platform (GCP) com permissão estrita de leitura (`https://www.googleapis.com/auth/spreadsheets.readonly`) nas pastas de contratos do Google Drive.
  - O serviço intermediário (**n8n** ou Supabase Edge Function) realiza a leitura programada das planilhas, executa a transformação de schema e dispara a inserção via upsert no banco relacional.

### 2.2. Contrato de Comunicação do Webhook de Sincronização (n8n / Edge Function)

- **Endpoint**: `POST /api/v1/sync/contract-data` (ou Edge Function `sync-sheet-data`)
- **Autenticação**: Bearer Token (JWT com role `service_role` ou chave de API de integração segura).
- **Payload de Entrada (Request Body)**:
```json
{
  "contractId": "b1a2c3d4-0000-0000-0000-000000000001",
  "competence": "2026-10",
  "module": "rh",
  "sourceType": "google_sheets",
  "sourceFileId": "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms",
  "records": [
    {
      "employeeId": "EMP-00123",
      "role": "Auxiliar de Serviços Gerais",
      "department": "Limpeza Predial",
      "unit": "Hospital Central - Ala Norte",
      "status": "ativo",
      "scheduledHours": 180,
      "workedHours": 180,
      "absenceHours": 0
    }
  ]
}
```

- **Resposta de Sucesso (Response 200 OK)**:
```json
{
  "success": true,
  "syncId": "sync-987654321",
  "contractId": "b1a2c3d4-0000-0000-0000-000000000001",
  "competence": "2026-10",
  "recordsProcessed": 120,
  "recordsInserted": 120,
  "errorsCount": 0,
  "executionTimeMs": 340,
  "timestamp": "2026-10-16T11:45:00.000Z"
}
```

- **Tratamento de Falhas (Response 422 Unprocessable Entity)**:
```json
{
  "success": false,
  "error": "VALIDATION_FAILED",
  "message": "Falha na validação dos campos obrigatórios da planilha de RH",
  "details": [
    {
      "line": 14,
      "field": "scheduledHours",
      "value": "invalid_number",
      "message": "O campo Horas Previstas deve ser um número positivo"
    }
  ]
}
```

---

## 3. Idempotência e Política de Repetição (Retry Policy)

1. **Garantia de Idempotência**:
   - Cada operação de sincronização é atômica e utiliza a chave composta `(contrato_id, competencia, chave_registro)`.
   - Se a execução for repetida 5 vezes consecutivas com os mesmos dados, o estado do banco e os indicadores calculados permanecem idênticos, sem gerar duplicidade de registros.
2. **Política de Backoff Exponencial**:
   - Falhas temporárias de conexão com a API do Google Sheets devem efetuar no máximo 3 tentativas com intervalos de 2s, 4s e 8s.
3. **Isolamento de Falha**:
   - Se uma planilha de uma unidade falhar, a sincronização das demais unidades do contrato não deve ser interrompida.
   - Os dados anteriores da unidade com falha são preservados intactos no banco de dados.
