
import os
from hmac import compare_digest

from flask import Blueprint, jsonify, request, session

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")


@auth_bp.post("/login")
def login():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify(error="JSON không hợp lệ"), 400

    username = data.get("username")
    password = data.get("password")

    expected_username = os.getenv("DEMO_USERNAME", "")
    expected_password = os.getenv("DEMO_PASSWORD", "")

    if not expected_username or not expected_password:
        return jsonify(error="Chưa cấu hình tài khoản demo"), 503

    if not isinstance(username, str) or not isinstance(password, str):
        return jsonify(error="Dữ liệu đăng nhập không hợp lệ"), 400

    if not (
        compare_digest(username, expected_username)
        and compare_digest(password, expected_password)
    ):
        return jsonify(error="Sai tên đăng nhập hoặc mật khẩu"), 401

    session.clear()
    session["username"] = username

    return jsonify(authenticated=True, username=username)


@auth_bp.get("/me")
def me():
    username = session.get("username")

    if not username:
        return jsonify(authenticated=False), 401

    return jsonify(authenticated=True, username=username)


@auth_bp.post("/logout")
def logout():
    session.clear()
    return jsonify(logged_out=True)
