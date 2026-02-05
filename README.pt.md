# 📋 Captura de Dados de Documentos

🤖 Este repositório contém a implementação de um agente em um microsserviço baseado na arquitetura de uma API REST. O projeto foi concebido, majoritariamente, pelos frameworks Langchain e FastAPI. Os seguintes recursos são disponibilizados pela aplicação:

🧑‍💻 Ler documentos PDF do banco de dados não relacional **MongoDB**; extrair dados de tabelas presentes nestes documentos; inserir estes dados no banco de dados relacional **SQLite**; consultar dados no banco de dados relacional de acordo com as solicitações do usuário.

## 🛣️ Rotas da Aplicação

**/delete_database_information**: Responsável por excluir o banco de dados SQLite;

**/talk_to_the_agent**: Responsável por extrair dados de tabelas encontradas em documentos PDF, bem como inserir e consultar tabelas no banco de dados SQLite.

## 🧰 Tecnologias Utilizadas

- Mongo 🗄️
- Python 🐍
- SQLite 🗃️  
- FastAPI 👩‍💻
- Langchain 🦜

## 💻 Como Usar a Aplicação

### 1️⃣ Configurar API do Google

Gere uma chave de API do Google em [Google AI Studio](https://aistudio.google.com/app/api-keys) e substitua na variável `GOOGLE_API_KEY` no arquivo `.env`.

### 2️⃣ Clonar o Repositório

git clone https://github.com/Maria-Clara-Bertoli/Document-Data-Capture.git

### 3️⃣ Inicializar a Aplicação com Docker

Execute o comando para criar as imagens e iniciar os contêineres da aplicação:

docker compose up --build

### 4️⃣ Adicionar Documentos PDF

Insira arquivos PDF no diretório `./essay/documents/`.

> ℹ️ Este repositório inclui dois arquivos de exemplo.

### 5️⃣ Inicializar o Banco de Dados

Acesse o diretório `./essay/` e execute o comando para inserir os documentos no banco de dados MongoDB:

python database_startup.py

### 6️⃣ Configurar Portas

Exponha as portas **80** e **27017** se necessário.

### 7️⃣ Testar a Aplicação

Acesse o Swagger em [http://localhost:80/docs](http://localhost:80/docs) e teste a aplicação.

## ✨ Exemplos de Uso

O arquivo `essay.ipynb` localizado no diretório `./essay/` contém exemplos de como interagir com o agente.

## ✅ Observações

Testes unitários serão adicionados em breve.

