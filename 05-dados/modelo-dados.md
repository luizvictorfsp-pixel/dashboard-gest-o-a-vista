# Modelagem Conceitual e Lógica do Banco de Dados
## Plataforma de Business Intelligence para Facilities (DNA Facilities)

O banco de dados oficial é o **PostgreSQL 15+** hospedado e gerenciado pelo **Supabase**, utilizando recursos avançados de integridade referencial, tipos enumerados (ENUM), índices compostos e Row Level Security (RLS).

---

## 1. Visão Geral das Entidades

O modelo relacional organiza-se em 6 grupos funcionais:

```text
1. NÚCLEO E ACESSO:
   - auth.users (gerenciado pelo Supabase Auth)
   - public.profiles (dados complementares de perfil)
   - public.user_roles (perfis formais: admin, manager, user)
   - public.audit_logs (trilha de auditoria imutável)

2. CADASTROS CORPORATIVOS:
   - public.clientes (empresas contratantes)
   - public.contratos (contratos de prestação de facilities)
   - public.unidades_operacionais (postos de trabalho / sites)
   - public.competencias (calendário de apuração YYYY-MM)

3. MÓDULO RECURSOS HUMANOS (RH):
   - public.rh_registros_competencia (admissões, demissões, efetivo, horas)
   - public.rh_afastamentos (detalhamento de afastamentos e faltas)

4. MÓDULO SEGURANÇA E SAÚDE (SMA):
   - public.sma_indicadores (HHT, acidentes típicos, trajeto, inspeções)
   - public.sma_desvios (registro, severidade e tratamento de desvios)

5. MÓDULO ORÇAMENTO E CONTROLADORIA:
   - public.orcamentos_competencia (orçado, realizado e saldo por categoria)
   - public.lancamentos_despesas (detalhamento por centro de custo e UF)

6. MÓDULO BOLETIM DE MEDIÇÃO:
   - public.boletins_medicao (ciclo de vida: medido, submetido, aprovado)
   - public.boletim_glosas (apontamentos de glosas com justificativa)
   - public.boletim_faturamentos (dados da NFS-e e liquidação financeira)
```

---

## 2. Estratégia de Migração e Compatibilidade

A tabela legada `public.dashboard_data` (que armazena dados em JSON) será preservada intacta durante a transição, funcionando como:
1. **Camada de Staging temporária**: onde arquivos importados são armazenados em raw JSON para auditoria técnica.
2. **Fallback**: assegurando que nenhuma visualização atual seja interrompida enquanto as novas tabelas relacionais são povoadas pelas rotinas de carga.
