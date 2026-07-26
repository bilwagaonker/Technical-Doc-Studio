from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.api.router import router

app = FastAPI(
    title="AI Technical Documentation Studio"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://192.168.1.6:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount(
    "/output",
    StaticFiles(directory="app/storage/output"),
    name="output"
)

app.mount(
    "/frames",
    StaticFiles(directory="app/storage/frames"),
    name="frames"
)

app.include_router(router)