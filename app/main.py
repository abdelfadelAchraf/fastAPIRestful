from fastapi import FastAPI
from app.routes import users
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for dev only; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# include routers
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI 🚀"}
