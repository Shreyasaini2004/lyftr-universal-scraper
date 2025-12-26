from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from backend.app.api import router
import os

app = FastAPI()
app.include_router(router)

# Serve React build
if os.path.exists("frontend/dist"):
    app.mount("/assets", StaticFiles(directory="frontend/dist/assets"), name="assets")

@app.get("/")
def serve_react():
    return FileResponse("frontend/dist/index.html")
