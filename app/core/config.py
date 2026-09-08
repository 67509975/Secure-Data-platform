from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Secure Data Platform API"
    environment: str = "development"

    database_url: str

    jwt_secret_key:str
    jwt_algorithm: str = "HS256"

    class Config:
        env_file = ".env"


settings = Settings()