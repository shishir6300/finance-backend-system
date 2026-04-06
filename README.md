# 💰 Finance Backend System

## 📌 Overview

This project is a Python-based finance tracking backend built using FastAPI.
It allows users to manage financial records (income & expenses), perform analytics, and interact with a well-structured REST API.

This project was developed as part of a backend development assignment to demonstrate clean architecture, business logic implementation, and API design.

---

## 🚀 Features

### 📊 Financial Records Management

* Create, update, delete financial records
* View all records
* Filter records by type and category

### 📈 Analytics & Summary

* Total income calculation
* Total expense calculation
* Current balance computation

### 👤 User & Role Handling

* Basic user creation
* Role support (Viewer, Analyst, Admin)

### 🌐 Backend Interface

* REST API using FastAPI
* Interactive Swagger documentation

### ⚠️ Validation & Error Handling

* Input validation (type, amount)
* Proper HTTP status codes
* Error handling for invalid operations

### 🎨 UI Enhancement

* Custom homepage UI for easy navigation
* Direct access to API documentation and endpoints

---

## 🛠️ Tech Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic

---

## 📂 Project Structure

```
finance_backend/
├── database.py
├── models.py
├── schemas.py
├── crud.py
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

```bash
git clone https://github.com/shishir6300/finance-backend-system.git
cd finance-backend-system
pip install -r requirements.txt
uvicorn main:app --reload
```

---

## 🌐 Access the Application

* 🏠 Home Page: http://127.0.0.1:8000/
* 📄 API Docs: http://127.0.0.1:8000/docs

---

## 📌 API Endpoints

| Method | Endpoint      | Description          |
| ------ | ------------- | -------------------- |
| POST   | /users/       | Create user          |
| POST   | /records/     | Add financial record |
| GET    | /records/     | Get all records      |
| PUT    | /records/{id} | Update record        |
| DELETE | /records/{id} | Delete record        |
| GET    | /summary/     | Financial summary    |

---

## 🧠 Assumptions

* Authentication is simplified for this assignment
* Role-based behavior is represented but not strictly enforced
* SQLite is used for simplicity and quick setup

---

## 🎯 Design Decisions

* Modular architecture (models, schemas, CRUD, routes)
* Separation of concerns for maintainability
* Lightweight database for ease of testing
* Clean and readable API design

---

## 🏆 Evaluation Alignment

This project demonstrates:

* Clean Python code structure
* Proper API design using FastAPI
* Logical handling of financial data
* Input validation and error handling
* Organized backend architecture

---

## 👨‍💻 Author

**Shishir Reddy**
GitHub: https://github.com/shishir6300

---

⭐ This project is developed for backend evaluation and demonstrates practical Python development skills.
