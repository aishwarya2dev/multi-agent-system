from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str
    API_VERSION: str
    OPENAI_API_KEY: str = ""
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"


settings = Settings()