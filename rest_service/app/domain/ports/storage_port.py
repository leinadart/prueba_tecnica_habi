from abc import abstractmethod, ABC

from app.domain.dto.query_data_dto import QueryDataDto


class StoragePort(ABC):

    @abstractmethod
    def get_data(self, query_data: QueryDataDto) -> list:
        pass