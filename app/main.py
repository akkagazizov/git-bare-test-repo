from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


import kpi_object_pos_err
import kpi_line_fn


app = FastAPI(debug=True, title='Custom API', version="0.0.1")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(kpi_object_pos_err.router)
app.include_router(kpi_line_fn.router)


@app.get('/')
async def info():
    return {"title": "FastAPI", "message": "Hello World"}


@app.get("/start")
async def start():
    return {"title": "Start", "message": "A new amazing feature"}


if __name__ == "__main__":
    uvicorn.run(app)