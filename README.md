# WoundCareAI - 협업 가이드

## 프로젝트 소개

WoundCareAI는 피부 상처 사진과 설명을 기반으로 AI가 분석하고 결과를 제공하는 서비스입니다. FastAPI, OpenAI API를 활용하여 개발 중입니다.

---

## Git 협업 규칙

### 브랜치 전략

- `main`: 최종 배포용 브랜치 (직접 push 금지)
- `dev`: 개발용 통합 브랜치
- `feature/이름`: 각자 작업할 기능별 브랜치 (예: feature/gpt-service)

### 커밋 메세지 스타일

- `feat:` 새로운 기능 추가
- `fix:` 버그 수정
- `docs:` 문서 수정
- `refactor:` 코드 리팩토링
- `test:` 테스트 코드 작성
- 예시: `feat: GPT 서비스 기본 기능 구현`

### PR(Pull Request) 규칙

- 기능 개발이 완료되면 `dev` 브랜치로 Pull Request를 생성합니다.
- 최소 1명 이상 코드 리뷰 후 Merge합니다.

### 코드 컨벤션

- 파일명: 소문자 + 언더스코어(`_`) 사용 (예: `gpt_service.py`)
- Python 3.12 버전 통일
- PEP8 코딩 스타일 준수 권장

---

## 개발 환경 세팅

### 필수 패키지 설치

```
pip install -r requirements.txt
```

### 서버 실행 방법

```
uvicorn main:app --reload
```

### 주의사항

- `.env` 파일을 반드시 로컬에 따로 관리하세요. (`.env`는 git에 올리지 않습니다.)
- `venv/` 폴더는 `.gitignore`에 포함되어 있습니다.

### 환경 변수 설정

- 프로젝트 루트에 `.env` 파일을 생성하고 다음과 같이 작성하세요.

예시 (.env 파일 내용):

```
OPENAI_API_KEY=your_openai_api_key_here
```

- `.env` 파일은 Git에 절대 업로드하지 마세요.
- 필요하면 `.env.example` 파일을 참고하거나 추가로 제공합니다.

---

## 추가 안내

- 이 저장소는 현재 **Public** 상태입니다.  
  만약 상업적 코드, 민감 데이터가 포함되면 반드시 **Private**로 전환해야 합니다.
