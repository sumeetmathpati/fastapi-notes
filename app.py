from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome. This is yet another note taking app."}