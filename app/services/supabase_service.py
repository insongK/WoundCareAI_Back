from app.core.config import settings
import requests
import uuid

SUPABASE_URL = settings.SUPABASE_URL
SUPABASE_BUCKET = settings.SUPABASE_BUCKET
SUPABASE_API_KEY = settings.SUPABASE_API_KEY

FOLDER_PATH = settings.FOLDER_PATH # 권한 설정된 폴더

def upload_image_to_supabase(file_bytes, original_filename):
    """
    Supabase Storage의 특정 폴더에 이미지를 업로드하고 public URL을 반환하는 함수
    """
    unique_filename = f"{uuid.uuid4()}_{original_filename}"
    upload_url = f"{SUPABASE_URL}/storage/v1/object/{SUPABASE_BUCKET}/{FOLDER_PATH}/{unique_filename}"
    headers = {
        "apikey": SUPABASE_API_KEY,
        "Authorization": f"Bearer {SUPABASE_API_KEY}",
        "Content-Type": "application/octet-stream"
    }
    response = requests.put(upload_url, headers=headers, data=file_bytes)
    if response.status_code == 200 or response.status_code == 201:
        public_url = f"{SUPABASE_URL}/storage/v1/object/public/{SUPABASE_BUCKET}/{FOLDER_PATH}/{unique_filename}"
        return public_url
    else:
        raise Exception(f"Supabase upload failed: {response.text}")
