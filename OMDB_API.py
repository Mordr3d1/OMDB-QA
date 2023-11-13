import subprocess
import json
import pytest

API_KEY = ""

BASE_URL = "http://www.omdbapi.com/"

def run_curl_command(url, params):
    command = ["curl", "-s", url + params]

    result = subprocess.run(command, capture_output=True, text=True)

    return json.loads(result.stdout)

def test_search_by_title():
    title = input("Введите название фильма для поиска: ")

    params = f"?apikey={API_KEY}&t={title}&r=json"

    response = run_curl_command(BASE_URL, params)

    assert response.get("Response") == "True"

    print(f"Информация о фильме '{title}':")
    print(f"Название: {response.get('Title')}")
    print(f"Год выпуска: {response.get('Year')}")
    print(f"Жанр: {response.get('Genre')}")
    print(f"Режиссер: {response.get('Director')}")

    print("OK")

def test_random_movies():
    params = f"?apikey={API_KEY}&s=&type=movie&r=json"

    response = run_curl_command(BASE_URL, params)

    assert response.get("Response") == "True"

    random_movies = response.get("Search")[:5]

    for movie in random_movies:
        print(f"Название: {movie.get('Title')}, Год выпуска: {movie.get('Year')}")