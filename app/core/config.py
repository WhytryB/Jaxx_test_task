from pydantic import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    API_V1_STR: str = "/api_v1"
    PROJECT_NAME: str = "Jaxx_test_task"
    SQLALCHEMY_DATABASE_URI: str = os.getenv('SQLALCHEMY_DATABASE_URI')
    KEY_FILE_LOCATION: str = os.getenv('KEY_FILE_LOCATION')


settings = Settings()
