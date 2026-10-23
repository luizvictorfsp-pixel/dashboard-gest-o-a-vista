# PRD — Product Requirements Document
## Plataforma de Business Intelligence para Gestão de Contratos de Facilities (DNA Facilities)

---

## 1. Visão Geral e Objetivo do Produto

### 1.1. Contexto de Negócio
A gestão corporativa de contratos de facilities (prestação de serviços de limpeza, portaria, manutenção predial, apoio administrativo e logística) lida com alta rotatividade operacional, múltiplos postos de trabalho distribuídos geograficamente, rígidas exigências legais trabalhistas e previdenciárias, além de requisitos críticos de Segurança, Meio Ambiente e Saúde (SMA).

Atualmente, dados operacionais e financeiros encontram-se dispersos em planilhas locais, e-mails e sistemas isolados, gerando:
- Atrasos na tomada de decisão gerencial;
- Dificuldade em comparar metas contratuais versus execução real;
- Risco de glosas contratuais por não atingimento de efetivo ou cumprimento de obrigações;
- Falta de rastreabilidade no ciclo de faturamento e medição.

### 1.2. Proposta de Valor
Desenvolver uma **plataforma integrada de Business Intelligence (BI)** em tempo quase real que consolida dados operacionais, financeiros, de recursos humanos e de segurança do trabalho em uma interface analítica premium, auditável e acessível conforme o perfil de atuação corporativa.

### 1.3. Objetivos Estratégicos (OKRs)
1. **Consolidação Unificada**: Centralizar 100% dos indicadores dos contratos atendidos em uma interface única.
2. **Eficiência no Faturamento**: Reduzir em pelo menos 30% o tempo médio de apuração e aprovação do Boletim de Medição.
3. **Mitigação de Glosas**: Identificar em até 24 horas desvios no Head Count e absenteísmo antes do fechamento da competência.
4. **Governança e Segurança**: Cumprir integralmente a LGPD no tratamento de dados de colaboradores e registros de ocorrências de SMA.

---

## 2. Perfis de Usuários e Matriz de Permissões (RBAC)

O sistema define 8 perfis de acesso, cada qual com permissões de Leitura (R), Inclusão (C), Edição (U), Exclusão (D) e Exportação (E):

| ID | Perfil | Descrição e Escopo | Escopo de Visualização | Permissões Típicas |
|---|---|---|---|---|
| **P-01** | **Administrador do Sistema** | Controle irrestrito de usuários, permissões, auditoria e configurações globais. | Global | C, R, U, D, E |
| **P-02** | **Diretoria** | Visão executiva consolidada de todos os contratos, rentabilidade global e riscos. | Global (Multi-contrato) | R, E |
| **P-03** | **Gestor / Coordenador do Contrato** | Visão operacional completa dos seus contratos específicos, metas e desvios. | Por Contrato atribuído | C, R, U, E |
| **P-04** | **RH (Recursos Humanos)** | Gestão de efetivo, admissões, demissões, afastamentos, férias e absenteísmo. | RH e Efetivo | C, R, U, E |
| **P-05** | **SMA (Segurança do Trabalho)** | Gestão de HHT, acidentes, inspeções planejadas, desvios e boas práticas. | SMA e Acidentes | C, R, U, E |
| **P-06** | **Financeiro / Orçamento** | Acompanhamento orçado x realizado, saldo orçamentário e custos por centro. | Financeiro | C, R, U, E |
| **P-07** | **Responsável pela Medição** | Apuração de boletim de medição, faturamento, aprovações, glosas e recebimentos. | Medição e Faturamento | C, R, U, E |
| **P-08** | **Usuário de Consulta** | Auditoria externa, fiscais do cliente ou analistas com acesso apenas leitura. | Conforme atribuição | R |

> [!IMPORTANT]
> **Privacidade e LGPD:** Dados de saúde do trabalhador, prontuários de acidentes e informações pessoais identificáveis (PII) de colaboradores são restritos aos perfis autorizados (RH e SMA), sendo mascarados ou agregados nos relatórios gerenciais e telas de consulta geral.

---

## 3. Estrutura Funcional do Dashboard (Módulos de Navegação)

A navegação da plataforma divide-se em 7 áreas fundamentais:

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                            GESTÃO A VISTA BI                                │
├───────────────┬─────────────────────────────────────────────────────────────┤
│ Menu Lateral  │ Cabeçalho Global: Filtro de Contrato | Competência | Unidade│
│               ├─────────────────────────────────────────────────────────────┤
│ [A] Visão Ger │ Página Analítica com Tabs, Gráficos Recharts e Tabelas      │
│ [B] RH        │ ┌──────────────────────┐  ┌───────────────────────────────┐ │
│ [C] SMA       │ │ KPI Card 1           │  │ KPI Card 2                    │ │
│ [D] Orçamento │ └──────────────────────┘  └───────────────────────────────┘ │
│ [E] Medição   │ ┌─────────────────────────────────────────────────────────┐ │
│ [F] Relatórios│ │ Gráficos Interativos / Grids de Análise                 │ │
│ [G] Configs   │ └─────────────────────────────────────────────────────────┘ │
└───────────────┴─────────────────────────────────────────────────────────────┘
```

### 3.1. Página A — Visão Geral do Contrato (Cockpit Executivo)
- **Objetivo**: Fornecer um panorama instantâneo e executivo da saúde contratual sem sobrecarregar com detalhes operacionais imediatos.
- **KPIs Principais**:
  - Head Count Contratual vs. Realizado (com índice de atendimento %).
  - Taxa de Absenteísmo e Taxa de Turnover da competência.
  - HHT (Horas-Homem Trabalhadas) e ocorrências de acidentes (com/sem afastamento).
  - Inspeções de Segurança (planejadas vs. realizadas).
  - Total Orçado vs. Total Realizado (Variação R$ e %).
  - Valor Medido, Aprovado, Faturado e Recebido.
  - Painel de Alertas Críticos (desvios graves, glosas iminentes, contratos a expirar).

### 3.2. Página B — Recursos Humanos (RH)
- **Objetivo**: Monitorar o fluxo de pessoas, cumprimento da escala contratual e custos indiretos gerados por rotatividade e ausências.
- **Painéis**:
  - Evolução mensal e acumulada de Turnover (admissões e desligamentos).
  - Análise de Absenteísmo (horas abonadas, atestados, faltas injustificadas).
  - Detalhamento de Efetivo: Ativos, Afastados (INSS/doença) e Férias.
  - Filtros analíticos: Por Função/Cargo, Unidade Operacional, Setor e Equipe/Turno.

### 3.3. Página C — Segurança, Meio Ambiente e Saúde (SMA)
- **Objetivo**: Assegurar a integridade física dos colaboradores, zero acidente e conformidade com as Normas Regulamentadoras (NRs).
- **Painéis**:
  - HHT consolidado da competência e acumulado de 12 meses.
  - TFCA (Taxa de Frequência de Acidentes com Afastamento) e TFSA (sem Afastamento).
  - Segregação de eventos: Acidente Típico vs. Acidente de Trajeto.
  - Inspeções Planejadas de Segurança (IPS): Taxa de cumprimento da meta.
  - Livro de Desvios de Segurança: Registros abertos, em tratamento e solucionados com prazo.
  - Mural de Boas Práticas e sugestões operacionais.

### 3.4. Página D — Orçamento e Custos
- **Objetivo**: Controlar o orçamento operacional do contrato evitando estouro de verba e custos não previstos.
- **Painéis**:
  - Orçamento Aprovado da Competência e Anual.
  - Realizado do Mês e Realizado Acumulado.
  - Desvio Financeiro Nominal ($) e Saldo Orçamentário Remanescente.
  - Índice de Consumo Percentual (%) com curva de tendência (Run Rate).
  - Detalhamento de Despesas por Categoria (Mão de Obra, Benefícios, Insumos/Materiais, Uniformes/EPIs, Equipamentos, Administrativo).
  - Visão por Centro de Custos e Unidades Contratuais.

### 3.5. Página E — Boletim de Medição (Ciclo Financeiro Contratual)
- **Objetivo**: Controlar o ciclo de vida da remuneração dos serviços prestados, assegurando que medição não seja confundida com faturamento ou recebimento.
- **Pipeline de Estados da Medição**:
  1. *Elaboração*: Cálculo inicial com base na assiduidade e entregas.
  2. *Submissão*: Envio do Boletim de Medição (BM) para fiscalização do cliente.
  3. *Aprovação / Glosa*: Análise do cliente com registro de eventuais glosas aplicadas e aceite formal.
  4. *Faturamento*: Emissão da Nota Fiscal de Serviços (NFS-e).
  5. *Recebimento*: Conciliação da liquidação bancária pelo cliente.
- **Indicadores**:
  - Valor Contratual Bruto.
  - Valor Medido Submetido.
  - Glosas Aplicadas (com motivo detalhado).
  - Valor Líquido Aprovado.
  - Valor Efetivamente Faturado e Saldo a Receber.
  - Lead Time Médio de cada etapa do ciclo (dias decorridos).

### 3.6. Página F — Relatórios Gerenciais e Exportação
- **Objetivo**: Permitir a extração de dados e relatórios formais para comitês executivos e prestação de contas com o cliente.
- **Funcionalidades**:
  - Seleção parametrizada de períodos (mês a mês, trimestral, YTD, personalizado).
  - Agrupamentos dinâmicos por Contrato, Cliente, Unidade e Linha de Negócio.
  - Exportação em formatos padronizados: Excel (.xlsx), CSV e PDF analítico.

### 3.7. Página G — Configurações e Governança
- **Objetivo**: Gerenciamento das tabelas base, parâmetros de negócio e integrações técnicas.
- **Funcionalidades**:
  - Gestão de Usuários, Vínculo de Perfis e Permissões Granulares.
  - Cadastro de Contratos, Clientes, Unidades Operacionais e Centros de Custo.
  - Definição de Metas Contratuais por Competência (metas de turnover, absenteísmo, IPS, limites de desvio).
  - Configuração de Fontes de Dados (Google Drive, Google Sheets, n8n webhooks).
  - Log de Auditoria e monitoramento de sincronizações.
