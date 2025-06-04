import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

def handler(event, context):
    http_method = event.get('httpMethod')
    if http_method == 'GET':
        # Scan all users (demo only, not for prod)
        response = table.scan()
        return {
            "statusCode": 200,
            "body": json.dumps(response['Items']),
            "headers": {"Content-Type": "application/json"}
        }

    elif http_method == 'POST':
        try:
            body = json.loads(event['body'])
            user_id = body['userId']
            table.put_item(Item=body)
            return {
                "statusCode": 201,
                "body": json.dumps({"message": f"User {user_id} created"}),
                "headers": {"Content-Type": "application/json"}
            }
        except Exception as e:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": str(e)}),
                "headers": {"Content-Type": "application/json"}
            }
    else:
        return {
            "statusCode": 405,
            "body": json.dumps({"message": "Method Not Allowed"}),
            "headers": {"Content-Type": "application/json"}
        }
