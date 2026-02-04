# Captura de Dados de Documentos

## 📋 Breve Explicação

Este repositório contém a implementação de um agente em um microsserviço baseado na arquitetura de APIs REST capaz de:

Ler documentos em formato PDF do banco de dados relacional **MongoDB**; extrair dados de tabelas presentes nestes documentos; inserir estes dados no banco de dados não relacional **SQLite**; consultar dados no banco de dados de acordo com as solicitações do usuário.

## 💻 Como Utilizar a Aplicação

### 1️⃣ Configurar a API do Google

Gere uma chave API do Google no site [Google AI Studio](https://aistudio.google.com/app/api-keys) e substitua na variável `GOOGLE_API_KEY` no arquivo `.env`.

### 2️⃣ Clonar o Repositório

```bash
git clone https://github.com/Maria-Clara-Bertoli/Document-Data-Capture.git
```

### 3️⃣ Inicializar a Aplicação com Docker

Execute o comando para criar as imagens e subir os containers da aplicação:

```bash
docker compose up --build
```

### 4️⃣ Adicionar Documentos PDF

Insira arquivos em formato PDF no diretório `./essay/documents/`.

> ℹ️ Este repositório traz dois exemplos incluídos.

### 5️⃣ Inicializar o Banco de Dados

Acesse o diretório `./essay/` e execute o comando para inserir os documentos no banco de dados MongoDB:

```bash
python database_startup.py
```

### 6️⃣ Configurar Portas

Exponha as portas **80** e **27017** caso seja necessário.

### 7️⃣ Testar a Aplicação

Acesse o Swagger no endereço [http://localhost:80/docs](http://localhost:80/docs) e teste a aplicação.

## ✨ Exemplos de Uso

O arquivo `essay.ipynb` presente no diretório `./essay/` contém exemplos de como conversar com o agente.

## 📂 Estrutura de Diretórios

Será incluída em breve.

