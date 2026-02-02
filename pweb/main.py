from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "success", "message": "¡Hola Alex, FastAPI ya está funcionando!"}