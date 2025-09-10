# 🚀 FastAPI User API

A simple **FastAPI project** that manages users with models, schemas, routes, and a mock database.  
This project is meant as a learning starter kit, similar to how the **MERN stack** separates backend logic.

---


---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/fastapi-user-api.git
cd fastapi-user-api
```
2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```
3. Install dependencies:

```bash
pip install -r requirements.txt
```


▶️ Run the Server
```bash
uvicorn app.main:app --reload
```
Available Endpoints

GET /users/ → List all users

POST /users/ → Create a new user

GET /users/{user_id} → Get user by ID
