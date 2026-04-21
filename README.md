# 🚀 FastAPI Notes Service

A simple yet powerful **Notes Management API** built with FastAPI.
This project demonstrates core backend concepts like CRUD operations, request validation, and API design.

---

## 📌 Features

* Create a new note 📝
* Get all notes 📖
* Get a single note by ID 🔍
* Update existing notes ✏️
* Delete notes ❌
* Proper status codes & error handling ⚡

---

## 🛠 Tech Stack

* **FastAPI** (Backend framework)
* **Python**
* **Uvicorn** (ASGI server)
* **Pydantic** (Data validation)

---

## 📂 Project Structure

```
fastapi-notes-service/
│── app/
│   ├── main.py
│   ├── schemas.py
│   ├── mock_data.py
│
│── requirements.txt
│── README.md
│── venv/
```

---

## ⚙️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/your-username/fastapi-notes-service.git

# Navigate into the project
cd fastapi-notes-service

# Create virtual environment
python -m venv venv

# Activate environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn app.main:app --reload
```

---

## 🌐 API Endpoints

| Method | Endpoint    | Description    |
| ------ | ----------- | -------------- |
| POST   | /notes      | Create a note  |
| GET    | /notes      | Get all notes  |
| GET    | /notes/{id} | Get note by ID |
| PUT    | /notes/{id} | Update note    |
| DELETE | /notes/{id} | Delete note    |

---

## 📖 API Docs

After running the server, open:

👉 http://127.0.0.1:8000/docs

Interactive Swagger UI for testing endpoints.

---

## 🧠 What I Learned

* Building REST APIs using FastAPI
* Handling request/response validation
* Implementing CRUD operations
* Error handling with HTTP exceptions
* Structuring backend projects

---

## 🚀 Future Improvements

* Database integration (PostgreSQL)
* Authentication (JWT)
* Pagination & filtering
* Docker support

---

## 👨‍💻 Author

Built with focus and consistency 💪
Ready to scale further 🚀
    ~MEHFOOZ
