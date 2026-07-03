import json
import os
import boto3
import requests

s3 = boto3.client('s3')
BUCKET_NAME = os.environ.get('BUCKET_NAME')
OBJECT_NAME = 'counter.json'


def lambda_handler(event, context):
    try:
        response = s3.get_object(Bucket=BUCKET_NAME, Key=OBJECT_NAME)
        content = response['Body'].read().decode('utf-8')
        data = json.loads(content)
        counter = data.get('visits', 0)
    except s3.exceptions.NoSuchKey:
        counter = 0

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
        print(e)

        raise e

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "message": "This API was deployed with Terraform.",
            "location": ip.text.replace("\n", ""),
            "total_visits": counter
        }, indent=4),
    }