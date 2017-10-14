import boto3, logging
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)
s3 = boto3.resource('s3')


def lambda_handler(event, context):
    if event is not None:
        try:
            acl = s3.BucketAcl(event['Bucket'])
            acl.put(ACL='public-read-write')
            logger.info('A Lambda function just updated your bucket ACL! Better update the bucket policy')
        except ClientError as e:
            raise Exception("Error writing log file to S3 bucket, S3 ClientError: " + e.response['Error']['Message'])
    else:
        print('No parameters')
