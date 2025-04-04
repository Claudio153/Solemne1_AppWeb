from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


@app.get("/")
async def main_route():
    return {"message": "Hey, It is me Goku"}

@app.get("/time")
async def get_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"current_time": current_time}