import json
import user_handler

def test_get_users():
    event = {
        "httpMethod": "GET"
    }
    context = {}
    response = user_handler.handler(event, context)
    assert response['statusCode'] == 200
    assert 'application/json' in response['headers']['Content-Type']

def test_post_user():
    event = {
        "httpMethod": "POST",
        "body": json.dumps({"userId": "123", "name": "John Doe"})
    }
    context = {}
    response = user_handler.handler(event, context)
    assert response['statusCode'] == 201
    body = json.loads(response['body'])
    assert "created" in body['message']
