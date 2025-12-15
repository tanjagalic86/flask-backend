def test_message_empty_body(client):
    response = client.post(
        "/api/v1/message",
        headers={"Content-Type": "application/json"},
    )

    assert response.status_code == 400


def test_message_not_object(client):
    response = client.post(
        "/api/v1/message",
        json=["hello"],
    )

    assert response.status_code == 400
    assert "JSON body must be an object" in response.get_data(as_text=True)


def test_message_valid(client):
    response = client.post(
        "/api/v1/message",
        json={"message": "hello"},
    )

    assert response.status_code == 201
    assert response.json == {"received_message": "hello"}
