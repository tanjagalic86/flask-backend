from typing import Any

from flask import Blueprint, jsonify, request
from werkzeug.exceptions import BadRequest, UnsupportedMediaType


def validate_message_payload(data: Any) -> None:
    if data is None:
        raise BadRequest("Invalid or empty JSON body")

    if not isinstance(data, dict):
        raise BadRequest("JSON body must be an object")

    if "message" not in data:
        raise BadRequest("Field 'message' is required")

    if not isinstance(data["message"], str):
        raise BadRequest("Field 'message' must be a string")

    if not data["message"].strip():
        raise BadRequest("Field 'message' cannot be empty")


api_bp = Blueprint("api", __name__, url_prefix="/api/v1")


@api_bp.get("/health")
def health():
    return jsonify({"status": "ok"})


@api_bp.post("/message")
def message():
    if not request.is_json:
        raise UnsupportedMediaType("Content-Type must be application/json")

    data = request.get_json(silent=True)

    validate_message_payload(data)

    return jsonify({"received_message": data["message"]}), 201
