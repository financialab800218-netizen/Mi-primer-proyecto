from fastapi import FastAPI

app = FastAPI(title="TutorIA Cuba API")

@app.get("/")
def raiz():
    return {"status": "ok", "proyecto": "TutorIA Cuba", "version": "0.1.0"}
