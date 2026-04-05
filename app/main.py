from fastapi import FastAPI
from app.routers.users import router as users_router

app = FastAPI()



print("LOADED CORRECT MAIN.PY")
print("LOADED CORRECT MAIN.PY")
print("LOADED CORRECT MAIN.PY")
print("LOADED CORRECT MAIN.PY")
print("LOADED CORRECT MAIN.PY")

@app.get("/")
def home():
    return {"message": "FastApi works!!!"}

app.include_router(users_router)