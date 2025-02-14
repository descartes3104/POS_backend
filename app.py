from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.get("/night")
async def night():
    return {"message": "Good Night!"}

@app.get("/morning")
async def morning():
    return {"message": "Good Morning!"}