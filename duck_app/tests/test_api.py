import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_test_api(client):
    """
    Test that /api/test/ returns 200 and correct JSON response.
    """
    url = reverse('test-api')  # Uses the URL name from urls.py
    response = client.get(url)

    assert response.status_code == 200
    data = response.json()

    assert data["status"] == "success"
    assert data["message"] == "Test API is working!"
    assert data["environment"] == "staging"


@pytest.mark.django_db
def test_cricket_report_api(client):
    """
    Test that /api/test/ returns 200 and correct JSON response.
    """
    url = reverse('cricket-report')  # Uses the URL name from urls.py
    response = client.get(url)

    assert response.status_code == 200
    data = response.json()

    assert data["status"] == "success"
    assert data["message"] == "Cricket Results"
    assert data["environment"] == "feature"