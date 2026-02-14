import requests

def test_jsonplaceholder_post_1():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    data = response.json()
    print(f"JSONPlaceholder post id: {data['id']}")
    assert response.status_code == 200
    assert data["id"] == 1
