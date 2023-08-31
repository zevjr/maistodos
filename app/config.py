"""
## Módulo de Configuração.
Esse módulo é responsável por definir as configurações do serviço.

Attributes:
    environment: Ambiente de execução, podendo ser (dev, prod, test, hml).
    service_name: Define o nome do serviço, por padrão é @maistodos/api.
    log_level: Define o nível de log, por padrão é INFO.
    is_sqlite: Define se o banco de dados é sqlite, por padrão é True.

    database_url: Define a url do banco de dados,
    por padrão é sqlite:///db.db, caso a variavel `is_sqlite` seja True .

    secret_key: Define a chave secreta para geração do token, por padrão é secret.
    algorithm: Define o algoritmo de geração do token, por padrão é HS256.
    token_expire: Define o tempo de expiração do token, por padrão é 30 minutos.

"""
import os

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    """
    As variaveis de ambiente são definidas no arquivo .env na raiz do projeto.

    """

    environment: str = os.environ.get("ENVIRONMENT", "dev")
    service_name: str = "@maistodos/api"
    log_level: str = os.environ.get("LOG_LEVEL", "INFO")
    is_sqlite: bool = bool(os.environ.get("IS_SQLITE", True))

    database_url: str = (
        "sqlite:///db.db" if is_sqlite else os.environ.get("DATABASE_URL", "")
    )
    secret_key: str = os.environ.get("SECRET_KEY", "secret")
    algorithm: str = os.environ.get("ALGORITHM", "HS256")
    token_expire: int = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", 30))


settings = Settings()
