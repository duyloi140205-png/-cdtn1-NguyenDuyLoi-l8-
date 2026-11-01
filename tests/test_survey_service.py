
from datetime import date, timedelta
from unittest.mock import patch

import pytest

from src.services import survey_service as service


def test_create_survey_success():
    data = {
        "ticket_id": 1,
        "expire_date": (
            date.today() + timedelta(days=7)
        ).isoformat()
    }

    with patch.object(
        service.repo, "create_survey",
        return_value=1
    ) as mock_create:
        result = service.create(data)

    assert result == 1
    mock_create.assert_called_once()


def test_create_survey_expired():
    data = {
        "ticket_id": 1,
        "expire_date": (
            date.today() - timedelta(days=1)
        ).isoformat()
    }

    with pytest.raises(ValueError):
        service.create(data)


def test_update_survey_success():
    data = {
        "expire_date": (
            date.today() + timedelta(days=7)
        ).isoformat()
    }

    with patch.object(
        service.repo, "update_survey",
        return_value=True
    ) as mock_update:
        result = service.update(1, data)

    assert result is True
    mock_update.assert_called_once()


def test_respond_csat_boundary():
    survey = {
        "ExpireDate": date.today() + timedelta(days=7)
    }

    with patch.object(
        service.repo, "get_survey",
        return_value=survey
    ), patch.object(
        service.repo, "create_feedback",
        return_value=1
    ) as mock_feedback:

        result = service.respond(
            1,
            {"csat": 5, "nps": 10}
        )

    assert result == 1
    mock_feedback.assert_called_once()


def test_respond_invalid_nps():
    survey = {
        "ExpireDate": date.today() + timedelta(days=7)
    }

    with patch.object(
        service.repo, "get_survey",
        return_value=survey
    ), patch.object(
        service.repo, "create_feedback"
    ) as mock_feedback:

        with pytest.raises(ValueError):
            service.respond(
                1,
                {"csat": 5, "nps": 11}
            )

    mock_feedback.assert_not_called()
