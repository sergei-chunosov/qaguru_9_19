import requests
from schemas import get_schema, post_schema, put_schema, patch_schema
from jsonschema import validate


def test_get_users():
    url = 'https://reqres.in/api/users/'
    response = requests.get(url, params={'page': 1})

    assert response.status_code == 200

    test_schema = response.json()["data"][0]
    validate(test_schema, get_schema.get_users)

    assert test_schema["first_name"] == 'George'


def test_create_users():
    url = 'https://reqres.in/api/users/'

    payload = {"name": "sergei", "job": "QA"}
    response = requests.post(url, data=payload)

    assert response.status_code == 201

    test_schema = response.json()
    validate(test_schema, post_schema.post_user)

    assert test_schema["job"] == "QA"


def test_change_username():
    url = 'https://reqres.in/api/users/2/'

    payload = {"name": "sergei ch", "job": "QA"}
    response = requests.put(url, data=payload)

    assert response.status_code == 200

    test_schema = response.json()
    validate(test_schema, put_schema.put_user)

    assert test_schema["name"] == "sergei ch"


def test_change_userjob():
    url = 'https://reqres.in/api/users/2/'

    payload = {"name": "sergei", "job": "QA++"}
    response = requests.patch(url, data=payload)

    assert response.status_code == 200

    test_schema = response.json()
    validate(test_schema, patch_schema.patch_user)

    assert test_schema["job"] == "QA++"


def test_delete_status():
    url = 'https://reqres.in/api/users/2/'

    response = requests.delete(url)
    assert response.status_code == 204

    assert response.text == ""


def test_get_single_users_negative():
    url = 'https://reqres.in/api/users/500'
    response = requests.get(url)

    assert response.status_code == 404
