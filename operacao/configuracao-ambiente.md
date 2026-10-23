# Configuração de Ambientes e Variáveis
## Plataforma de Business Intelligence para Facilities (DNA Facilities)

---

## 1. Dicionário de Variáveis de Ambiente (.env)

| Variável | Escopo | Obrigatória? | Descrição |
|---|---|---|---|
| `VITE_SUPABASE_URL` | Frontend (Client) | Sim | URL da instância do Supabase BaaS (ex: `https://brihkumeqocjqhcfdlfi.supabase.co`) |
| `VITE_SUPABASE_PUBLISHABLE_KEY` | Frontend (Client) | Sim | Chave de API anônima (`anon key`) do Supabase protegida por RLS |
| `VITE_SUPABASE_PROJECT_ID` | Frontend (Client) | Sim | Identificador do projeto no Supabase |
| `SUPABASE_SERVICE_ROLE_KEY` | Backend / n8n | Apenas Backend | Chave com privilégios administrativos (bypassa RLS) para automações |
| `GOOGLE_SERVICE_ACCOUNT_EMAIL`| n8n / Integração | Opcional | E-mail da conta de serviço para leitura de Google Sheets |
| `GOOGLE_PRIVATE_KEY` | n8n / Integração | Opcional | Chave RSA privada para assinatura de tokens OAuth do Google |

---

## 2. Boas Práticas e Regras de Segurança

1. **Nunca versione credenciais privadas**: Arquivos `.env` locais estão listados no `.gitignore` e não devem ser enviados para repositórios públicos ou compartilhados.
2. **Separação de Chaves**: A chave `anon` pública do frontend possui apenas as permissões autorizadas pelo Row Level Security (RLS). A chave `service_role` **jamais** deve ser prefixada com `VITE_` ou exposta ao navegador.
