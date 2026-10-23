# Monitoramento, Logs e Observabilidade
## Plataforma de Business Intelligence para Facilities (DNA Facilities)

---

## 1. Monitoramento de Aplicação e Telemetria

O sistema utiliza monitoramento em 3 níveis:
1. **Frontend (Browser)**:
   - React Error Boundary para captura de erros de renderização em tela.
   - Notificações de toast (`sonner` / `useToast`) exibindo alertas claros ao usuário em falhas de rede.
2. **Backend e Banco de Dados (Supabase)**:
   - Monitoramento de uso de CPU, conexões de banco e latência no painel do Supabase.
   - Logs de execução de Edge Functions (`create-user`, `update-user-password`).
3. **Trilha de Auditoria (`public.audit_logs`)**:
   - Registro permanente de modificações em permissões, inclusões e exclusões de registros.

---

## 2. Estrutura dos Logs de Auditoria

```json
{
  "timestamp": "2026-10-16T11:55:00.000Z",
  "userId": "usr-12345678-0000-0000-0000-000000000001",
  "userEmail": "gestor@dnafacilities.com.br",
  "action": "UPLOAD_COMPETENCIA",
  "module": "rh",
  "contractId": "ct-9999",
  "competence": "2026-10",
  "recordsCount": 120,
  "status": "SUCCESS",
  "ipAddress": "177.136.240.10"
}
```
