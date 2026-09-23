from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    deepseek_api_key: str = ""
    deepseek_base_url: str = "https://api.deepseek.com"
    database_url: str = ""
    secret_key: str = "cambia_esto"
    environment: str = "development"

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
