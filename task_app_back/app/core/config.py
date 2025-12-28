from pydantic_settings import BaseSettings


class Config(BaseSettings):
    app_port: int

    postgres_host: str
    postgres_port: int
    postgres_user: str
    postgres_password: str
    postgres_db: str


config = Config()   # type: ignore
