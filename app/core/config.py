########################################################
# pydantic는 .env 파일을 읽어서 환경변수를 설정해준다.           #
# - os.environ를 먼저 읽고, 없으면 .env 파일을 읽는다.         #
# - 환경변수를 설정하려면 환경변수 이름과 값을 설정해야 한다.        #
# - 환경변수 이름은 대문자로 설정하고, 값은 소문자로 설정한다.       #
########################################################

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    OPENAI_API_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()