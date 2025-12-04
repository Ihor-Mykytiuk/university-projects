from flask import Flask, jsonify
import logging
import os
import requests
from datetime import datetime, timezone


class LogstashHTTPHandler(logging.Handler):
    def __init__(self, endpoint: str):
        super().__init__()
        self.endpoint = endpoint.rstrip("/")

    def emit(self, record: logging.LogRecord) -> None:
        try:
            ts = datetime.fromtimestamp(record.created, tz=timezone.utc).isoformat()
            payload = {
                "@timestamp": ts,
                "level": record.levelname,
                "logger": record.name,
                "message": record.getMessage(),
                "filename": record.filename,
                "lineno": record.lineno,
                "funcName": record.funcName,
                "extra": getattr(record, "extra", {}),
            }
            headers = {"Content-Type": "application/json"}
            requests.post(self.endpoint, json=payload, headers=headers, timeout=1.5)
        except Exception:
            pass


def create_app() -> Flask:
    app = Flask(__name__)

    logstash_url = os.getenv("LOGSTASH_URL", "http://logstash:8080")
    http_endpoint = f"{logstash_url}"

    app_logger = logging.getLogger("flask_app")
    app_logger.setLevel(logging.INFO)

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(logging.Formatter("%(asctime)s %(levelname)s [%(name)s] %(message)s"))

    ls_handler = LogstashHTTPHandler(http_endpoint)
    ls_handler.setLevel(logging.INFO)

    app_logger.addHandler(console)
    app_logger.addHandler(ls_handler)

    @app.get("/")
    def index():
        return """
                <h2>Log Generator</h2>
                <a href="/info">Generate INFO</a><br>
                <a href="/warning">Generate WARNING</a><br>
                <a href="/error">Generate ERROR</a>
                """

    @app.get("/info")
    def gen_info():
        app_logger.info("User triggered an INFO event")
        return jsonify(status="ok", level="INFO"), 200

    @app.get("/warning")
    def gen_warning():
        app_logger.warning("User triggered a WARNING event")
        return jsonify(status="ok", level="WARNING"), 200

    @app.get("/error")
    def gen_error():
        try:
            _ = 1 / 0
        except Exception as exc:
            app_logger.exception("User triggered an ERROR event")
        return jsonify(status="ok", level="ERROR"), 200

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
