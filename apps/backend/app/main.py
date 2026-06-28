from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router

app = FastAPI(
    title="AI Technical Documentation Studio API",
    version="1.0.0",
    description="Backend API for AI-powered SAP Technical Documentation Generator"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)


@app.get("/")
async def root():
    return {
        "message": "AI Technical Documentation Studio API",
        "status": "running"
    }