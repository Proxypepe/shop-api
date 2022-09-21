from pydantic import BaseSettings


class Settings(BaseSettings):
    app_env: str = 'development'

    database_username: str = 'postgres'
    database_password: str = 'postgres123'
    database_host: str = 'localhost'
    database_port: str = '32700'
    database_name: str = 'ecommerce_database'

    test_database_name: str = 'test_database'

    redis_host: str = 'localhost'
    redis_port: str = '6379'
    redis_database: str = '0' if app_env == 'TESTING' else '0'

    class Config:
        env_file = ".env"


settings = Settings()
