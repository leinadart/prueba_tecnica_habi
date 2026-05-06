import logging

from app.domain.dto.query_data_dto import QueryDataDto
from app.domain.ports.storage_port import StoragePort

logger = logging.getLogger(__file__)
logger.setLevel(logging.INFO)


class MainService:

    def __init__(self, db_repository: StoragePort):
        self.repository = db_repository

    def get_data(self, query_data: QueryDataDto) -> list:

        return self.repository.get_data(query_data= query_data)