import json

def evenOdd(num):
    if int(num) % 2 == 0:
        return "even"

    return "odd"

def squaredNum(num):
    return int(num) * int(num)

def evenOr(event, context):
    yourNum = event["queryStringParameters"]["number"]
    body = {
        "message": "This service checks if your number is Even or Odd!!!",
        "input": yourNum,
        "output": evenOdd(yourNum)
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def squared(event, context):
    yourNum = event["queryStringParameters"]["number"]
    body = {
        "message": "This service squares your number!!!",
        "input": yourNum,
        "output": squaredNum(yourNum)
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response