import pytest

#  Пример с API weather
from main import get_weather

def test_get_weather_success(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'weather': [{'description': 'clouds'}],
        'main': {'temp': 10}
    }

    api_key = '2029b8b51e4bae5500421b9230bd0bf5'
    city = 'London'

    weather_data = get_weather(api_key, city)

    assert weather_data == {
        'weather': [{'description': 'clouds'}],
        'main': {'temp': 10}
    }

def test_get_weather_with_error(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 404

    api_key = '2029b8b51e4bae5500421b9230bd0bf5'
    city = 'London'

    weather_data = get_weather(api_key, city)

    assert weather_data == None

# Пример с API github
from main import get_github_user_info

def test_get_github_user_info_success(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'login': 'testuser',
        'id': 1,
        'name': 'Test User'
    }

    username = 'testuser'

    user_info = get_github_user_info(username)

    assert user_info == {
        'login': 'testuser',
        'id': 1,
        'name': 'Test User'
    }

def test_get_github_user_info_with_error(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 500

    username = 'testuser'

    user_info = get_github_user_info(username)

    assert user_info == None