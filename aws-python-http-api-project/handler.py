import json


def hello(event, context):
    body = {
        "message": "Hello Dosto! Your function executed successfully!"
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def bye(event, context):
    body = {
        "message": "Bye Bye  Dosto! Your function executed successfully!"
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
