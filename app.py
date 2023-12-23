import json

def test_user_registration(client):
    # Test user registration endpoint
    user_data = {
        "username": "test_user",
        "password": "test_password",
        "email": "test@example.com"
    }
    response = client.post("/api/register", json=user_data)
    assert response.status_code == 201

def test_user_login(client):
    # Test user login endpoint
    login_data = {
        "username": "test_user",
        "password": "test_password"
    }
    response = client.post("/api/login", json=login_data)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "access_token" in data

def test_edit_user_profile(client, access_token):
    # Test user profile edit endpoint
    new_profile_data = {
        "username": "updated_user",
        "email": "updated@example.com"
    }
    headers = {"Authorization": f"Bearer {access_token}"}
    response = client.put("/api/profile", json=new_profile_data, headers=headers)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["username"] == new_profile_data["username"]
    assert data["email"] == new_profile_data["email"]

def test_delete_user_account(client, access_token):
    # Test user account deletion endpoint
    headers = {"Authorization": f"Bearer {access_token}"}
    response = client.delete("/api/profile", headers=headers)
    assert response.status_code == 204

def test_user_logout(client, access_token):
    # Test user logout endpoint
    headers = {"Authorization": f"Bearer {access_token}"}
    response = client.post("/api/logout", headers=headers)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "message" in data
    assert data["message"] == "Successfully logged out"
