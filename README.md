## Setup

Lembre-se de criar uma tabela idêntica à do exemplo CSV e adicionar as credenciais necessárias no arquivo `.env`, conforme especificado abaixo:

* **SUPABASE_URL e SUPABASE_KEY:** Podem ser encontrados em *Project* > *API Settings* (ou na aba de conexões do painel do [Supabase](https://supabase.com/dashboard)).
* **INSTANCE_ID e TOKEN:** Podem ser encontrados em *Instâncias Web* > *Dados da Instância Web* no painel da [Z-API](https://app.z-api.io/app/instances).
* **CLIENT_TOKEN:** Encontra-se na aba *Segurança* > *Token de segurança da conta*, também na [Z-API](https://app.z-api.io/app/security).

> 💡 **Nota:** Os links acima assumem que você já está autenticado em suas respectivas contas.

---

## Passos para Execução

Siga os comandos abaixo no seu terminal para clonar o repositório, instalar as dependências e rodar o projeto:

```bash
# Clonar o repositório
git clone https://github.com/JulioPm142/desafio-b2bflow.git

# Entrar no diretório do projeto (opcional, mas recomendado se já não estiver nele)
cd desafio-b2bflow

# Instalar as dependências necessárias
pip install -r requirements.txt

# Executar o script principal
python Main.py
