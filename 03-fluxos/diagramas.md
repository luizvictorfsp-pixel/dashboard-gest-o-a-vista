# Diagramas de Processos, Arquitetura e Ciclo de Vida
## Plataforma de Business Intelligence para Facilities (DNA Facilities)

---

## 1. Diagrama de Sequência — Ingestão e Processamento de Planilhas

```mermaid
sequenceDiagram
    autonumber
    actor Usuario as Usuário (RH/Gestor)
    participant UI as Interface Web (React)
    participant Parser as Validador / Parser (Zod + XLSX)
    participant DB as Banco de Dados (Supabase)
    participant Cache as Cache Local (localStorage)
    participant Audit as Trilha de Auditoria

    Usuario->>UI: Seleciona arquivo .xlsx/.csv no modal de Upload
    UI->>Parser: Envia buffer do arquivo para validação
    alt Arquivo Inválido (Cabeçalhos incorretos ou tipos inválidos)
        Parser-->>UI: Retorna lista de erros por linha/coluna
        UI-->>Usuario: Exibe alerta vermelho com detalhamento
    else Arquivo Válido
        Parser-->>UI: Retorna array de objetos sanitizados
        UI->>DB: Executa upsert atômico (contrato_id, competencia)
        alt Falha de Conexão com Supabase
            DB-->>UI: Timeout / Network Error
            UI->>Cache: Salva cópia de contingência no cache local
            UI-->>Usuario: Exibe aviso de contingência local ativa
        else Sucesso no Banco
            DB-->>UI: Confirmação de 200 OK (registros gravados)
            UI->>Cache: Atualiza timestamp de última sincronização
            UI->>Audit: Registra inserção na tabela audit_logs
            UI-->>Usuario: Exibe toast verde de sincronização concluída
        end
    end
```

---

## 2. Diagrama de Estados — Ciclo de Vida do Boletim de Medição (BM)

```mermaid
stateDiagram-v2
    [*] --> Elaboracao: Fechamento da Competência
    Elaboracao --> Submetido: Envio do BM para o Cliente
    
    state Submetido {
        [*] --> AnaliseFiscalizacao
        AnaliseFiscalizacao --> ComApontamentoGlosas: Divergência de Efetivo/SLA
        AnaliseFiscalizacao --> SemGlosas: Conformidade Total
    }

    ComApontamentoGlosas --> AprovadoComGlosas: Aceite e Justificativa das Glosas
    SemGlosas --> AprovadoIntegral: Aceite Formal do Cliente

    AprovadoComGlosas --> Faturado: Emissão da NFS-e (Valor Líquido)
    AprovadoIntegral --> Faturado: Emissão da NFS-e (Valor Bruto)

    Faturado --> Recebido: Liquidação Financeira pelo Cliente
    Recebido --> [*]: Ciclo Concluído com Sucesso
```

---

## 3. Diagrama de Atividades — Consulta Interativa do Dashboard

```mermaid
flowchart TD
    Start([Usuário acessa o Dashboard]) --> CheckAuth{Sessão válida?}
    CheckAuth -- Não --> RedirectLogin[Redireciona para /auth]
    CheckAuth -- Sim --> LoadRoles[Carrega perfil e permissões do usuário]
    
    LoadRoles --> SelectContract[Identifica contrato padrão ou atribuído]
    SelectContract --> FetchData[Consulta métricas agregadas da competência ativa]
    
    FetchData --> RenderCards[Renderiza Cards de KPIs com tendências]
    FetchData --> RenderCharts[Renderiza Gráficos Recharts]
    
    RenderCharts --> UserInteraction{Usuário altera filtro?}
    UserInteraction -- Troca Competência --> FetchData
    UserInteraction -- Troca Contrato --> FetchData
    UserInteraction -- Aplica Filtro de Unidade --> LocalFilter[Filtra dados em memória]
    LocalFilter --> RenderCharts
```
