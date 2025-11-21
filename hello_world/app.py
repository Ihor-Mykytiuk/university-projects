import json
import os
import boto3
import requests

s3 = boto3.client('s3')
BUCKET_NAME = os.environ.get('BUCKET_NAME')
OBJECT_NAME = 'counter.json'

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    try:
        response = s3.get_object(Bucket=BUCKET_NAME, Key=OBJECT_NAME)
        content = response['Body'].read().decode('utf-8')
        data = json.loads(content)
        counter = data.get('visits', 0)
    except s3.exceptions.NoSuchKey:
        counter = 0
    except Exception as e:
        print(e)
        raise e

    counter += 1

    new_data = {'visits': counter}
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=OBJECT_NAME,
        Body=json.dumps(new_data),
        ContentType='application/json'
    )

    try:
        ip = requests.get("http://checkip.amazonaws.com/")
    except requests.RequestException as e:
        # Send some context about this error to Lambda Logs
        print(e)

        raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            "location": ip.text.replace("\n", ""),
            "total_visits": counter
        }),
    }

