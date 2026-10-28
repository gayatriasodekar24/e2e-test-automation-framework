import requests

BASE_URL = "https://dummyjson.com"


def test_get_post_by_id_returns_valid_post():
    response = requests.get(f"{BASE_URL}/posts/1", timeout=15)

    assert response.status_code == 200, (
        f"Expected HTTP 200, got {response.status_code}"
    )

    post = response.json()

    assert post["id"] == 1, "Expected the response to contain post ID 1"
    assert isinstance(post["title"], str) and post["title"].strip(), (
        "Expected the post title to be a non-empty string"
    )
    assert isinstance(post["body"], str), (
        "Expected the post body to be a string"
    )
    assert isinstance(post["userId"], int), (
        "Expected the userId to be an integer"
    )
    
def test_get_missing_post_returns_not_found():
    response = requests.get(f"{BASE_URL}/posts/999999", timeout=15)

    assert response.status_code == 404, (
        f"Expected HTTP 404 for missing post, got {response.status_code}"
    )


def test_get_posts_by_user_returns_matching_posts():
    response = requests.get(f"{BASE_URL}/posts/user/5", timeout=15)

    assert response.status_code == 200, (
        f"Expected HTTP 200, got {response.status_code}"
    )

    data = response.json()

    assert isinstance(data["posts"], list), (
        "Expected posts to be a list"
    )
    assert len(data["posts"]) > 0, "Expected at least one post for user 5"
    assert all(post["userId"] == 5 for post in data["posts"]), (
        "Every returned post should belong to user 5"
    )
