import boto3
import logging
import json
import botocore
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)
s3 = boto3.client('s3')
lam = boto3.client('lambda')

def lambda_handler(event, context):
    optin = False
    buckets = s3.list_buckets()
    for bucket in buckets['Buckets']:
        logger.info('bucket: %s', bucket['Name'])
        try:
            tags = s3.get_bucket_tagging(Bucket=bucket['Name'])
            if any(d.get('Key') == 'optin' and d.get('Value') == 'yes' for d in tags.get('TagSet')):
                logger.info('Invoking slingr against: %s', bucket['Name'])
                lam.invoke(
                    FunctionName=os.environ['slingr'],
                    InvocationType='Event',
                    Payload=json.dumps({'Bucket':bucket['Name']})
                )
                optin = True
        except botocore.exceptions.ClientError as e:
            logger.error(e)
    
    if not optin:
        logger.info('No buckets want to be tested')
