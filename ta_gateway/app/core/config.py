from pydantic_settings import BaseSettings


class Config(BaseSettings):
    app_port: int
    
    user_auth_service_url: str
    project_service_url: str


config = Config()   # type: ignore
