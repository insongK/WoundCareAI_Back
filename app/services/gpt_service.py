import base64
import openai
from fastapi import UploadFile
from app.core.config import settings

# OpenAI API Key 설정
openai.api_key = settings.OPENAI_API_KEY

async def generate_gpt_response(file: UploadFile = None, description: str = "") -> str:
    """
    사진(옵션) + 설명(옵션)을 GPT에게 보내고, 분석 결과를 받아온다.
    """
    system_prompt = {
        "role": "system",
        "content": (
            "You are a friendly and empathetic medical assistant specializing in wound analysis. "
            "You must always output JSON in one of the following formats:\n\n"
            "- If it is an analysis result, output:\n"
            "{\n"
            '  "type": "result",\n'
            '  "severity": (1~10 integer),\n'
            '  "confidence": (0~100 integer, prediction confidence),\n'
            '  "summary": "analysis summary text"\n'
            "}\n\n"
            "- If you need to ask the user for more information, output:\n"
            "{\n"
            '  "type": "question",\n'
            '  "question": "question text to ask the user"\n'
            "}\n\n"
            "Never mix result and question together. Choose only one per message."
        )
    }

    # 기본 messages 준비
    messages = [system_prompt]

    # description(텍스트)이 있으면 추가
    if description:
        messages.append({"role": "user", "content": description})

    # file(사진)이 있으면 base64로 변환 후 추가
    if file:
        image_bytes = await file.read()
        encoded_image = base64.b64encode(image_bytes).decode('utf-8')
        
        # Vision 지원하는 GPT 모델로 전송할 수 있게 구성
        messages.append({
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Please analyze this wound image and provide a diagnosis, severity, and basic treatment recommendations."
                },
                {
                    "type": "image",
                    "image": {
                        "base64": encoded_image
                    }
                }
            ]
        })

    # GPT 호출
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        max_tokens=500,
    )

    answer = response.choices[0].message.content
    return answer