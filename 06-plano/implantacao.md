# Implantação e Go-Live — Fase 8

## Check-list Pré-Publicação
- [x] Fase 1–7 concluídas
- [x] Documentação viva atualizada (`docs/`)
- [x] Migrações SQL validadas (`supabase/migrations/`)
- [x] Testes unitários / integração passando (`vitest`)
- [ ] Variáveis de ambiente da Vercel validadas (`.env.production`)
- [ ] Scripts de migração finais executados no Supabase de produção
- [ ] Monitoramento de erros ativado (Sentry / Vercel Analytics)
- [ ] Treinamento dos usuários-chave realizado

## Variáveis de Ambiente (Produção)
```
VITE_SUPABASE_URL=https://xxxx.supabase.co
VITE_SUPABASE_ANON_KEY=xxx
VITE_APP_ENV=production
```

## Migração Final
```bash
npx supabase db push --project-ref xxxx
```

## Monitoramento
- Log de erros ativado
- Dashboard de observabilidade configurado
- Acompanhamento assistido pós-go-live (30 dias)
