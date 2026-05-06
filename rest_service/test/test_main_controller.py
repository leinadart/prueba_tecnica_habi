import io
import json
from unittest.mock import Mock, patch

from app.application.main_controller import MainController


def build_handler(path: str):
    handler = MainController.__new__(MainController)

    handler.path = path
    handler.headers = {}

    handler.rfile = io.BytesIO()
    handler.wfile = io.BytesIO()

    handler.send_response = Mock()
    handler.send_header = Mock()
    handler.end_headers = Mock()
    handler.send_error = Mock()

    return handler

class TestMainController:

    @patch("app.application.main_controller.get_use_case")
    def test_get_properties_success(self, mock_get_use_case):
        mock_use_case = Mock()
        mock_use_case.get_data.return_value = []
        mock_get_use_case.return_value = mock_use_case

        handler = build_handler("/get-properties?year=2020&city=bogota&state=en_venta")

        handler.do_GET()

        handler.send_response.assert_called_once_with(200)

        handler.send_header.assert_called_with("Content-Type", "application/json")
        response_body = handler.wfile.getvalue()
        assert json.loads(response_body) == []

    def test_not_found(self):
        handler = build_handler("/invalid")

        handler.do_GET()

        handler.send_response.assert_called_once_with(404)
        assert handler.wfile.getvalue() == b"Not found"

    def test_health(self):
        handler = build_handler("/health")

        handler.do_GET()

        handler.send_response.assert_called_once_with(200)

    @patch("app.application.main_controller.get_use_case")
    def test_value_error_returns_400(self, mock_get_use_case):
        mock_use_case = Mock()
        mock_use_case.get_data.side_effect = ValueError("bad request")
        mock_get_use_case.return_value = mock_use_case

        handler = build_handler("/get-properties?year=2020&city=bogota&state=en_venta")

        handler.do_GET()

        handler.send_error.assert_called_once_with(400, "bad request")

