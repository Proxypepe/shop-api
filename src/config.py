from typing import Optional

from functools import lru_cache

from pydantic import BaseSettings, Field


class GlobalSettings(BaseSettings):
    app_env: str = 'development'

    database_username: str = 'postgres'
    database_password: str = 'postgres123'
    database_host: str = 'localhost'
    database_port: str = '5432'
    database_name: str = 'ecommerce_database'

    test_database_name: str = 'test_database'

    redis_host: str = 'localhost'
    redis_port: str = '6379'
    redis_database: str = '0' if app_env == 'TESTING' else '0'

    secret_key: str = Field('', env='SECRET_KEY')
    algorithm: str = Field('', env='ALGORITHM')
    access_token_expire_minutes: int = Field(0, env='ACCESS_TOKEN_EXPIRE_MINUTES')

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
