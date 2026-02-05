# 📋 Document Data Capture

🤖 This repository contains the implementation of an agent in a microservice based on a REST API architecture. The project was designed primarily using the Langchain and FastAPI frameworks. The following resources are available in the application:

🧑‍💻 Reading PDF documents from the **MongoDB** non-relational database; extracting data from tables present in these documents; inserting this data into the **SQLite** relational database; querying data in the relational database according to user requests.

## 🛣️ Application Routes

**/delete_database_information**: Responsible for deleting the SQLite database;

**/talk_to_the_agent**: Responsible for extracting data from tables found in PDF documents, as well as inserting and querying tables in the SQLite database.

## 🧰 Technologies Used

- Mongo 🗄️
- Python 🐍
- SQLite 🗃️  
- FastAPI 👩‍💻
- Langchain 🦜

## 💻 How to Use the Application

### 1️⃣ Configure Google API

Generate a Google API key at [Google AI Studio](https://aistudio.google.com/app/api-keys) and replace it in the `GOOGLE_API_KEY` variable in the `.env` file.

### 2️⃣ Clone the Repository

```bash
git clone https://github.com/Maria-Clara-Bertoli/Document-Data-Capture.git
```

### 3️⃣ Initialize the Application with Docker

Run the command to create the images and start the application containers:

```bash
docker compose up --build
```

### 4️⃣ Add PDF Documents

Insert PDF files into the `./essay/documents/` directory.

> ℹ️ This repository includes two example files.

### 5️⃣ Initialize the Database

Access the `./essay/` directory and run the command to insert the documents into the MongoDB database:

```bash
python database_startup.py
```

### 6️⃣ Configure Ports

Expose ports **80** and **27017** if necessary.

### 7️⃣ Test the Application

Access Swagger at [http://localhost:80/docs](http://localhost:80/docs) and test the application.

## ✨ Usage Examples

The `essay.ipynb` file located in the `./essay/` directory contains examples of how to interact with the agent.

## ✅ Observations

Unit tests will be added soon.
