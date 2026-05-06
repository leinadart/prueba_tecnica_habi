from app.application.config import get_settings
from app.domain.services.main_service import MainService
from app.infrastructure.adapters.mysql_adapter import MySqlDBAdapter


def get_db_adapter() -> MySqlDBAdapter:

    settings = get_settings()
    return MySqlDBAdapter(host=settings.host,
                          user=settings.user,
                          password=settings.password,
                          database=settings.database,
                          port = settings.port)


def get_use_case() -> MainService:

    return MainService(db_repository=get_db_adapter())