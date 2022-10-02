from typing import Optional
import os

from functools import lru_cache

from pydantic import BaseSettings, Field


class GlobalSettings(BaseSettings):
    app_env: str = Field('development', env='APP_ENV')

    database_username: str = os.getenv('DATABASE_USERNAME', 'postgres')
    database_password: str = os.getenv('DATABASE_PASSWORD', 'postgres123')
    database_host: str = os.getenv('DATABASE_HOST', 'localhost')
    database_port: str = os.getenv('DATABASE_PORT', '5432')
    database_name: str = os.getenv('DATABASE_NAME', 'ecommerce_database')

    test_database_name: str = Field('test_database', env='TEST_DATABASE_NAME')

    redis_host: str = 'localhost'
    redis_port: str = '6379'
    redis_database: str = '0' if app_env == 'TESTING' else '0'

    secret_key: str = Field('09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7', env='SECRET_KEY')
    algorithm: str = Field('HS256', env='ALGORITHM')
    access_token_expire_minutes: int = Field(30, env='ACCESS_TOKEN_EXPIRE_MINUTES')

    class Config:
        env_file = ".env"

#
# class DevConfig(GlobalSettings):
#     """Development configurations."""
#
#     class Config:
#         env_prefix: str = "DEV_"
#
#
# class ProdConfig(GlobalSettings):
#     """Production configurations."""
#
#     class Config:
#         env_prefix: str = "PROD_"
#
#
# class FactoryConfig:
#     """Returns a config instance dependending on the ENV_STATE variable."""
#
#     def __init__(self, env_state: Optional[str]):
#         self.env_state = env_state
#
#     def __call__(self):
#         if self.env_state == "dev":
#             return DevConfig()
#
#         elif self.env_state == "prod":
#             return ProdConfig()


@lru_cache()
def get_settings():
    return GlobalSettings()


settings = get_settings()

