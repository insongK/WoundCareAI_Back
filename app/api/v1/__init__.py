# app/api/v1/__init__.py

from fastapi import APIRouter
from app.api.v1.endpoints import analysis

api_router = APIRouter()
api_router.include_router(analysis.router)