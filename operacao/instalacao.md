# Guia de Instalação e Execução Local
## Plataforma de Business Intelligence para Facilities (DNA Facilities)

---

## 1. Pré-Requisitos do Sistema

- **Node.js**: Versão `>= 18.18.0` ou `>= 20.x` recomendada.
- **Gerenciador de Pacotes**: `npm` (versão 9+ ou 10+) ou `bun`.
- **Git**: Para controle de versionamento.
- **Acesso à Internet**: Para comunicação com os serviços de nuvem do Supabase.

---

## 2. Passo a Passo de Execução Local

### Passo 1: Navegar até a pasta da aplicação principal
Como identificado no diagnóstico da Etapa 0, a aplicação web completa está localizada no subdiretório `dashboard-gestaoavista-main`:

```powershell
cd c:\Antigravity\dashboard-gestaoavista-main
```

### Passo 2: Instalação das dependências
Execute o comando de instalação para sincronizar todas as dependências do `package.json`:

```powershell
npm install
```

### Passo 3: Verificação das Variáveis de Ambiente
Certifique-se de que o arquivo `.env` existe na pasta `dashboard-gestaoavista-main` contendo as credenciais de acesso ao Supabase:

```env
VITE_SUPABASE_PROJECT_ID="brihkumeqocjqhcfdlfi"
VITE_SUPABASE_PUBLISHABLE_KEY="<SUA_CHAVE_PUBLICA_ANON>"
VITE_SUPABASE_URL="https://brihkumeqocjqhcfdlfi.supabase.co"
```

### Passo 4: Inicialização do Servidor de Desenvolvimento
Inicie o servidor de desenvolvimento com hot-reloading (HMR):

```powershell
npm run dev
```

A aplicação estará disponível em `http://localhost:8080` (ou na porta indicada pelo Vite).

---

## 3. Scripts Disponíveis no `package.json`

- `npm run dev`: Inicia o servidor de desenvolvimento Vite.
- `npm run build`: Compila o bundle otimizado de produção na pasta `dist/`.
- `npm run preview`: Executa localmente o bundle compilado para validação pré-deploy.
- `npm run lint`: Executa a checagem de regras de código com ESLint.
