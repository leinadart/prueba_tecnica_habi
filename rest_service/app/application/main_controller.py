import json
from http.server import BaseHTTPRequestHandler

import logging
from urllib.parse import urlparse, parse_qs

from app.application.dependencies import get_use_case
from app.domain.dto.query_data_dto import QueryDataDto

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class MainController(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            parsed_url = urlparse(self.path)
            path = parsed_url.path
            query = parse_qs(parsed_url.query)

            if path == "/get-properties":
                year = query.get("year", [""])[0]
                city = query.get("city", [""])[0]
                state = query.get("state", [""])[0]

                if not state in ['en_venta', 'pre_venta', 'vendido']:
                    self.send_response(400)
                    response = {"details": "The states permitted are: 'en_venta', 'pre_venta', 'vendido'"}

                else:
                    query_data = QueryDataDto(year=year,
                                              city= city,
                                              state= state)

                    use_case = get_use_case()

                    results = use_case.get_data(query_data=query_data)

                    response = results

                    self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()

                self.wfile.write(json.dumps(response).encode())
            elif path == "/health":

                response = {"details": "Service online"}

                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()

                self.wfile.write(json.dumps(response).encode())

            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"Not found")
        except ValueError as e:
            logger.error(str(e))
            self.send_error(400, str(e))

        except Exception as e:
            logger.error(str(e))
            self.send_error(500, "Error interno del servidor")