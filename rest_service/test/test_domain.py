from unittest.mock import Mock

import pytest

from app.domain.dto.query_data_dto import QueryDataDto
from app.domain.ports.storage_port import StoragePort
from app.domain.services.main_service import MainService


class TestDomain:

    @pytest.fixture
    def mock_repository(self):
        return Mock(spec=StoragePort)

    @pytest.fixture
    def use_case(self, mock_repository):
        return MainService(mock_repository)

    def test_domain(self, mock_repository, use_case):
        mock_repository.get_data.return_value = []
        query_data = QueryDataDto("2000", "", "en_venta")
        results = use_case.get_data(query_data= query_data)
        assert results == []


