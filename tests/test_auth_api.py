
from app import app


def test_surveys_requires_login():
    app.config["TESTING"] = True

    with app.test_client() as client:
        response = client.get("/api/surveys")

    assert response.status_code == 401
    assert response.get_json()["error"] == "Vui lòng đăng nhập"


def test_login_wrong_password(monkeypatch):
    app.config["TESTING"] = True

    monkeypatch.setenv("DEMO_USERNAME", "test_admin")
    monkeypatch.setenv("DEMO_PASSWORD", "correct_password")

    with app.test_client() as client:
        response = client.post(
            "/api/auth/login",
            json={
                "username": "test_admin",
                "password": "wrong_password"
            }
        )

    assert response.status_code == 401
    assert response.get_json()["error"] == (
        "Sai tên đăng nhập hoặc mật khẩu"
    )

def test_feedback_api_returns_201_after_success(monkeypatch):
    from app import app
    from src.routes import survey_routes

    # Mock service để không ghi dữ liệu MySQL thật.
    monkeypatch.setattr(
        survey_routes.svc,
        "respond",
        lambda survey_id, data: 123
    )

    app.config["TESTING"] = True

    with app.test_client() as client:
        with client.session_transaction() as sess:
            sess["username"] = "test_user"

        response = client.post(
            "/api/surveys/3/feedback",
            json={"csat": 5, "nps": 9, "comment": "Test"}
        )

        assert response.status_code == 201
        assert response.get_json() == {"id": 123}

def test_feedback_api_survey_not_found(monkeypatch):
    from app import app
    from src.routes import survey_routes

    def fake_respond(survey_id, data):
        raise LookupError("Không tìm thấy khảo sát")

    monkeypatch.setattr(
        survey_routes.svc, "respond", fake_respond
    )

    app.config["TESTING"] = True

    with app.test_client() as client:
        with client.session_transaction() as sess:
            sess["username"] = "test_user"

        response = client.post(
            "/api/surveys/999999/feedback",
            json={"csat": 5, "nps": 9}
        )

        assert response.status_code == 404
        assert "error" in response.get_json()


def test_feedback_api_invalid_nps_returns_400(monkeypatch):
    from app import app
    from src.routes import survey_routes

    def fake_respond(survey_id, data):
        raise ValueError("NPS phải là số nguyên từ 0 đến 10")

    monkeypatch.setattr(
        survey_routes.svc, "respond", fake_respond
    )

    app.config["TESTING"] = True

    with app.test_client() as client:
        with client.session_transaction() as sess:
            sess["username"] = "test_user"

        response = client.post(
            "/api/surveys/3/feedback",
            json={"csat": 5, "nps": 11}
        )

        assert response.status_code == 400
        assert "error" in response.get_json()
