from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException


def create_app() -> Flask:
    app = Flask(__name__)

    from app.routes.api import api_bp

    app.register_blueprint(api_bp)

    @app.errorhandler(HTTPException)
    def handle_http_exception(e: HTTPException):
        response = {
            "error": {
                "type": e.__class__.__name__,
                "message": e.description,
            }
        }
        return jsonify(response), e.code

    return app


app = create_app()
