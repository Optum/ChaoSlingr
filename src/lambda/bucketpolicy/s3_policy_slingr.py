import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3', endpoint_url='http://localhost:4572')

def lambda_handler(event, context):
    if event is not None:
        try:
            s3.put_object(
                Bucket=event['Bucket'],
                Key='TESTOBJECT',
                Body=b'Throwing objects at you better deny!!!'
            )
        except ClientError as e:
            raise Exception("Error writing log file to S3 bucket, S3 ClientError: " + e.response['Error']['Message'])
    else:
        print('No parameters')
