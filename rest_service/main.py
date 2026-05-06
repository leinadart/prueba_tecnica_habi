from http.server import HTTPServer

from app.application.main_controller import MainController
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def run():
    server = HTTPServer(("0.0.0.0", 8000), MainController)
    print("Running on http://localhost:8000")
    server.serve_forever()

if __name__ == "__main__":
    run()