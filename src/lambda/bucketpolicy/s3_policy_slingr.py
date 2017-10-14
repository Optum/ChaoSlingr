import boto3, logging
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)
s3 = boto3.client('s3')


def lambda_handler(event, context):
    if event is not None:
        try:
            s3.put_object(
                Bucket=event['Bucket'],
                Key='TESTOBJECT',
                Body=b'Throwing objects at you! Better deny!!!'
            )
            logger.info('A Lambda function just uploaded an object to your bucket! Better update the bucket policy')
        except ClientError as e:
            raise Exception("Error writing log file to S3 bucket, S3 ClientError: " + e.response['Error']['Message'])
    else:
        print('No parameters')
