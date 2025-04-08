from fastapi import FastAPI
from datetime import datetime
import uvicorn 

app = FastAPI()

@app.get("/time")
async def get_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"current_time": current_time}

if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1", port=8000,reload=True)
