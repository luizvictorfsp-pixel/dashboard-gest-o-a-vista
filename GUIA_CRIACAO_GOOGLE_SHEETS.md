# 🚀 Guia Prático: Como Ativar a Planilha no Google Sheets — Gestão à Vista

Esta documentação orienta o passo a passo para criar, importar e conectar a planilha oficial do projeto ao **Dashboard Gestão à Vista**.

---

## 📦 Arquivos Gerados Disponíveis no Projeto

| Arquivo / Pasta | Descrição | Como Usar |
|---|---|---|
| [`Planilha_Gestao_a_Vista_GoogleSheets.xlsx`](./Planilha_Gestao_a_Vista_GoogleSheets.xlsx) | **Arquivo Excel Oficial consolidado** com as 4 abas formatadas (`RH`, `SMA`, `Orcamento`, `Medicao`), com estilos, cabeçalhos escuros, linhas zebradas e larguras ajustadas. | **Recomendado**: Faça upload direto no Google Drive ou importe no Google Sheets. |
| [`Criar_Planilha_Google_Sheets.gs`](./Criar_Planilha_Google_Sheets.gs) | **Google Apps Script** para criação 100% automática na nuvem sem precisar fazer download/upload manual de arquivo. | Cole no [script.new](https://script.new) e clique em **Executar ▶**. |
| [`planilha-google-sheets/`](./planilha-google-sheets/) | Pasta com os 4 arquivos `.csv` avulsos: <br>• [`RH.csv`](./planilha-google-sheets/RH.csv)<br>• [`SMA.csv`](./planilha-google-sheets/SMA.csv)<br>• [`Orcamento.csv`](./planilha-google-sheets/Orcamento.csv)<br>• [`Medicao.csv`](./planilha-google-sheets/Medicao.csv) | Importação manual aba por aba ou contingência. |

---

## 🛠️ Método 1: Importando o arquivo Excel (.xlsx) no Google Sheets (Mais Rápido)

1. Acesse o **Google Drive** ([drive.google.com](https://drive.google.com)) ou o **Google Sheets** ([sheets.new](https://sheets.new)).
2. Clique em **Novo (+) → Upload de arquivo** e selecione o arquivo:
   ```
   C:\Antigravity\docs\Planilha_Gestao_a_Vista_GoogleSheets.xlsx
   ```
3. Abra o arquivo carregado no Google Drive e clique em **Salvar como Planilha Google** (ou abra com Google Planilhas).
4. Verifique que as 4 abas estão presentes na barra inferior com os nomes exatos:
   - `RH`
   - `SMA`
   - `Orcamento`
   - `Medicao`

---

## ⚡ Método 2: Criação 100% Automática via Google Apps Script (script.new)

1. No seu navegador, abra [script.new](https://script.new).
2. Apague o código padrão que aparece no editor.
3. Abra o arquivo [`Criar_Planilha_Google_Sheets.gs`](./Criar_Planilha_Google_Sheets.gs), copie todo o seu conteúdo e cole no editor do Apps Script.
4. Clique no ícone de disquete **Salvar** (Ctrl+S) e depois clique em **Executar ▶** na barra superior.
5. Autorize as permissões de acesso ao Google Planilhas na sua conta Google.
6. Ao término (cerca de 3 segundos), veja no painel de log a URL da planilha recém-criada e o **ID do Google Sheets**.

---

## 🌐 Como Publicar e Conectar ao Dashboard

Para que o dashboard web consiga ler os dados via API pública da Google sem requerer chaves de autenticação no navegador:

1. Na sua planilha no Google Sheets, clique no menu:
   **Arquivo → Compartilhar → Publicar na web**
2. Na janela que abrir:
   - Selecione **"Documento inteiro"**
   - No formato, selecione **"Valores separados por vírgula (.csv)"**
3. Clique no botão azul **Publicar**.
4. Copie o **ID da planilha** da barra de endereços (a sequência de letras e números entre `/d/` e `/edit`):
   ```text
   https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
                                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                                      (ESTE É O ID)
   ```
5. Abra o dashboard do projeto [`dashboard.html`](./dashboard.html) no navegador:
   - No menu lateral ou superior direito, cole o seu ID no campo **Google Sheets ID**.
   - Clique em **Salvar & Conectar**.
   - O indicador mudará de `● Dados Demo` para `● Google Sheets` com todos os 13 indicadores calculados em tempo real!

---

## 📊 Estrutura e Dicionário de Colunas das Abas

### 1. Aba `RH`
| Coluna | Tipo | Descrição | Exemplo |
|---|---|---|---|
| `MES` | Texto | Competência / Mês | `Jan/26` |
| `EFETIVO_CONTRATUAL` | Inteiro | Headcount contratual acordado | `130` |
| `EFETIVO_REALIZADO` | Inteiro | Headcount ativo em operação | `120` |
| `ADMISSOES` | Inteiro | Contratações no mês | `4` |
| `DESLIGAMENTOS` | Inteiro | Saídas/rescisões no mês | `2` |
| `AFASTAMENTO` | Inteiro | Colaboradores afastados (INSS/saúde) | `3` |
| `FERIAS` | Inteiro | Colaboradores em gozo de férias | `5` |
| `HORAS_PREVISTAS` | Inteiro | Total de horas trabalháveis | `21600` |
| `HORAS_AUSENCIA` | Inteiro | Total de horas perdidas | `432` |

### 2. Aba `SMA`
| Coluna | Tipo | Descrição | Exemplo |
|---|---|---|---|
| `MES` | Texto | Competência / Mês | `Jan/26` |
| `HHT` | Inteiro | Horas-Homem Trabalhadas | `21600` |
| `ACIDENTES_COM_AFASTAMENTO` | Inteiro | Acidentes com afastamento (CPT) | `0` |
| `ACIDENTES_SEM_AFASTAMENTO` | Inteiro | Acidentes sem afastamento (SPT) | `0` |
| `ACIDENTES_TRAJETO` | Inteiro | Acidentes de percurso/trajeto | `0` |
| `INSPECOES_PLANEJADAS` | Inteiro | Inspeções de segurança planejadas | `10` |
| `INSPECOES_REALIZADAS` | Inteiro | Inspeções de segurança executadas | `10` |
| `DESVIOS_REGISTRADOS` | Inteiro | Condições/atos inseguros reportados | `2` |
| `DESVIOS_TRATADOS` | Inteiro | Desvios com plano de ação concluído | `2` |

### 3. Aba `Orcamento`
| Coluna | Tipo | Descrição | Exemplo |
|---|---|---|---|
| `MES` | Texto | Competência / Mês | `Jan/26` |
| `CATEGORIA` | Texto | Grupo de custos (Mão de Obra, Insumos, etc.) | `Mão de Obra e Encargos` |
| `ORCADO` | Decimal (R$) | Valor orçado para a categoria | `180000.00` |
| `REALIZADO` | Decimal (R$) | Valor efetivamente despendido | `178500.00` |
| `CENTRO_CUSTO` | Texto | Centro de custo da operação | `CC-101` |
| `UF` | Texto | Unidade Federativa | `SP` |

### 4. Aba `Medicao`
| Coluna | Tipo | Descrição | Exemplo |
|---|---|---|---|
| `COMPETENCIA` | Texto (AAAA-MM) | Mês de competência | `2026-01` |
| `CONTRATO` | Texto | Código do contrato | `CT-2024-HOSP` |
| `VALOR_CONTRATUAL` | Decimal (R$) | Valor mensal em contrato | `350000.00` |
| `VALOR_MEDIDO` | Decimal (R$) | Valor apurado na medição | `350000.00` |
| `VALOR_APROVADO` | Decimal (R$) | Valor homologado pelo cliente | `349000.00` |
| `VALOR_GLOSAS` | Decimal (R$) | Descontos contratuais aplicados | `1000.00` |
| `MOTIVO_GLOSA` | Texto | Justificativa técnica do desconto | `Atraso em ponto` |
| `VALOR_FATURADO` | Decimal (R$) | Valor da Nota Fiscal emitida | `349000.00` |
| `VALOR_RECEBIDO` | Decimal (R$) | Valor liquidado em conta | `349000.00` |
| `STATUS` | Texto | `submetido`, `faturado` ou `recebido` | `recebido` |
| `DATA_SUBMISSAO` | Data | Data de entrega do boletim | `02/02/2026` |
