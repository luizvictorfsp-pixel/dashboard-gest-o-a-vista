# Critérios de Aceitação (BDD / Gherkin)
## Plataforma de Business Intelligence para Facilities (DNA Facilities)

Estes cenários de teste em formato Behavior-Driven Development (BDD / Gherkin) orientam a validação funcional, a homologação e a escrita de testes de aceitação automatizados (Playwright/Vitest).

---

### Cenário 1: Autenticação e Controle de Acesso por Perfil (RF-001 e RF-013)

```gherkin
Cenário: Usuário autentica-se com sucesso e visualiza apenas os módulos autorizados
  Dado que um usuário com o perfil "SMA / Segurança do Trabalho" está cadastrado
  E possui credenciais válidas "seguranca@dnafacilities.com.br"
  Quando ele insere seu e-mail e senha na tela de login (/auth)
  E clica no botão "Acessar Sistema"
  Então o sistema deve autenticar a sessão via Supabase Auth
  E redirecionar para a rota "/"
  E exibir no cabeçalho o badge de perfil "SMA"
  E as abas de "Visão Geral" e "SMA" devem estar visíveis e ativas
  E a aba de "Orçado x Realizado" e o botão "Upload" devem estar ocultos ou desabilitados
```

```gherkin
Cenário: Usuário tenta acessar rota protegida sem permissão
  Dado que um usuário com perfil "Usuário de Consulta" está autenticado
  Quando ele tenta navegar diretamente para a rota "/configuracoes" ou acionar o diálogo de gestão de usuários
  Então o sistema deve bloquear o acesso
  E exibir uma notificação de "Acesso Não Autorizado"
  E registrar uma tentativa de violação na trilha de auditoria
```

---

### Cenário 2: Seleção Reativa de Competência e Contrato (RF-002 e RF-004)

```gherkin
Cenário: Alternância de competência recalcula KPIs instantaneamente
  Dado que o Gestor de Contratos está visualizando a página "Visão Geral" do contrato "Hospital Central"
  E a competência ativa selecionada é "Outubro / 2026"
  Quando ele seleciona a competência "Setembro / 2026" no filtro superior
  Então todas as consultas de dados devem ser atualizadas para a competência "2026-09"
  E os cards de KPIs (Head Count, Turnover, Absenteísmo, Orçado, Realizado) devem exibir os valores de Setembro
  E os indicadores de tendência devem exibir a variação comparada a "Agosto / 2026"
  E o timestamp de "Última Atualização" deve refletir a carga de Setembro
```

---

### Cenário 3: Ingestão Idempotente de Dados de RH (RF-006 e RF-007)

```gherkin
Cenário: Importação de planilha de RH com dados válidos substitui a versão da competência
  Dado que o usuário com perfil "RH" acessa o modal de Upload de Dados
  E seleciona um arquivo "rh_outubro_2026.xlsx" válido contendo 120 colaboradores
  Quando ele confirma o upload
  Então o sistema deve validar a estrutura das colunas (EFETIVO, ADMISSOES, DEMISSOES, ABSENTEISMO, TURNOVER)
  E persistir os registros vinculados à competência "2026-10"
  E se já existirem registros para "2026-10" neste contrato, os dados devem ser atualizados (upsert) sem duplicar linhas
  E o total de colaboradores ativos deve ser computado exatamente como 120
  E uma mensagem de sucesso "Dados de RH sincronizados com sucesso" deve ser exibida
```

```gherkin
Cenário: Importação rejeita arquivo com layout inválido sem corromper base existente
  Dado que o usuário tenta importar um arquivo "custos_corrompido.csv" com colunas faltantes
  Quando o processador de arquivo executa o parser
  Então o sistema deve abortar a importação
  E não deve apagar os dados existentes no banco
  E exibir um alerta de erro detalhando "Coluna 'ORÇADO' ausente no arquivo"
  E registrar o evento na tabela de logs de integração
```

---

### Cenário 4: Cálculo e Validação do Boletim de Medição (RF-012 e IND-011)

```gherkin
Cenário: Aplicação de glosa contratual ajusta valor líquido a faturar
  Dado que para a competência atual o "Valor Medido Bruto" é de R$ 100.000,00
  Quando o Responsável pela Medição lança uma glosa no valor de R$ 3.500,00 com motivo "Falta de posto noturno no dia 12"
  Então o sistema deve recalcular o "Valor Líquido Aprovado" para R$ 96.500,00
  E computar o Índice de Glosa em 3,50%
  E o card de Índice de Glosa deve exibir a cor vermelha (Crítico, acima de 2,0%)
  E a glosa deve constar no relatório detalhado com justificativa e autor
```

---

### Cenário 5: Tratamento de Exceções de Divisão por Zero em Indicadores

```gherkin
Cenário: Cálculo de TFCA quando não há HHT registrado no período
  Dado que uma nova unidade operacional foi cadastrada sem apontamento de horas (HHT = 0)
  E ocorreu um acidente registrado
  Quando o dashboard de SMA processa os cálculos da unidade
  Então a TFCA não deve resultar em erro de tela ("NaN" ou "Infinity")
  E o sistema deve renderizar o valor "0,00" ou "N/D" (Não Disponível)
  E exibir uma flag informativa: "HHT não informado para esta competência"
```
