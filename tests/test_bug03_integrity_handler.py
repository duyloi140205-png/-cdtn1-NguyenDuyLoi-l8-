from flask import Flask
from pymysql.err import IntegrityError

from src.routes.survey_routes import bp


def test_integrity_error_handler_registered():
    app = Flask(__name__)
    app.secret_key = "test-only-key"
    app.register_blueprint(bp)

    with app.test_request_context():
        handler = app._find_error_handler(
            IntegrityError(1062, "Duplicate entry"),
            ["survey", None],
        )

    assert handler is not None, (
        "BUG-03: Chưa đăng ký handler cho IntegrityError"
    )