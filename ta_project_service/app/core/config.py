from pydantic_settings import BaseSettings


class Config(BaseSettings):
    app_port: int

    postgres_host: str
    postgres_port: int
    postgres_user: str
    postgres_password: str
    postgres_db: str

    client_id: str
    client_secret: str

    ea_auth_url: str


config = Config()   # type: ignore
