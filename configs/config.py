import logging

from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    env_name: str = 'local'
    base_url: str = 'http://localhost:80'
    db_url: str = 'sqlite:///./shortener.db'

    class Config:
        env_file = '.env'


@lru_cache()
def get_settings() -> Settings:
    settings = Settings()
    logging.info(f"Loaded setting for : {settings.env_name}")
    return settings
