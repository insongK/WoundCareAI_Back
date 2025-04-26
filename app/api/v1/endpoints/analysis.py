# app/api/v1/endpoints/analyze.py

from fastapi import APIRouter, UploadFile, Form
from app.services.gpt_service import generate_gpt_response

router = APIRouter()

@router.post("/analyze")
async def analyze_wound(file: UploadFile = None, description: str = Form("")):
    """
    상처 사진(file)과 설명(description)을 받아 GPT에게 분석 요청하는 API
    """
    result = await generate_gpt_response(file, description)
    return {"result": result}