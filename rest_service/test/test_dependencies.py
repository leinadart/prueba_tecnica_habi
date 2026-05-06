from unittest.mock import patch, Mock, MagicMock

from app.application.dependencies import get_db_adapter, get_use_case
from app.domain.services.main_service import MainService
from app.infrastructure.adapters.mysql_adapter import MySqlDBAdapter


class TestDependencies:

    @patch('app.application.dependencies.MySqlDBAdapter')
    @patch('app.application.dependencies.get_settings')
    def test_dependencies_db_adapter(self, mock_get_settings, mock_adapter_class):

        mock_settings = Mock()
        mock_settings.host = "test_host"
        mock_settings.user = "test_user"
        mock_settings.password = "test_passwd"
        mock_settings.database = "test_database"
        mock_settings.port = "test_port"

        mock_get_settings.return_value = mock_settings

        mock_adapter = Mock()
        mock_adapter_class.return_value = mock_adapter

        get_db_adapter()

        mock_adapter_class.assert_called_once_with(
            host = "test_host",
            user = "test_user",
            password = "test_passwd",
            database = "test_database",
            port = "test_port"
        )

    @patch('app.application.dependencies.get_db_adapter')
    def test_use_case_returns_use_case_instance(self, mock_get_adapter):
        # Arrange
        mock_adapter = Mock(spec=MySqlDBAdapter)
        mock_get_adapter.return_value = mock_adapter

        # Act
        use_case = get_use_case()

        # Assert
        assert isinstance(use_case, MainService)