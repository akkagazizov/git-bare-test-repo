from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(debug=True, title='Custom API', version="0.0.1")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def info():
    return {"title": "FastAPI", "message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app)