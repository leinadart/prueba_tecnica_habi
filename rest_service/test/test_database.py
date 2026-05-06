from unittest.mock import patch

import pytest

from app.domain.dto.query_data_dto import QueryDataDto
from app.infrastructure.adapters.mysql_adapter import MySqlDBAdapter

class TestDataBase:

    @pytest.fixture
    def config(self):
        return {
            "host": "",
            "user": "",
            "password": "",
            "database": "",
            "port": ""
        }
    @patch("mysql.connector.connect")
    def test_get_data_only_year(self, mock_connect, config):
        mock_con = mock_connect.return_value
        mock_cur = mock_con.cursor.return_value
        mock_cur.fetchall.return_value = (())
        main = MySqlDBAdapter(**config)
        query_data = QueryDataDto("2000", "", "")
        results = main.get_data(query_data)
        assert len(results) == 0
        assert isinstance(results, list)

    @patch("mysql.connector.connect")
    def test_get_data_year_and_city(self, mock_connect, config):
        mock_con = mock_connect.return_value
        mock_cur = mock_con.cursor.return_value
        mock_cur.fetchall.return_value = (())
        main = MySqlDBAdapter(**config)
        query_data = QueryDataDto("2000", "bogota", "")
        results = main.get_data(query_data)
        assert len(results) == 0
        assert isinstance(results, list)


    @patch("mysql.connector.connect")
    def test_get_data_year_and_state(self, mock_connect, config):
        mock_con = mock_connect.return_value
        mock_cur = mock_con.cursor.return_value
        mock_cur.fetchall.return_value = (())
        main = MySqlDBAdapter(**config)
        query_data = QueryDataDto("2000", "", "en_venta")
        results = main.get_data(query_data)
        assert len(results) == 0
        assert isinstance(results, list)

