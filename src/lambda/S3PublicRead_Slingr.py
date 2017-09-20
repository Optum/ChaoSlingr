import boto3
from botocore.exceptions import ClientError
import random
import json
import time

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = 'publicReadable'

    # Create benign S3 bucket
    create_response = s3.create_bucket(ACL='private', Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})
    print('create_response = ', create_response)

    # Make benign S3 bucket publicly visible
    config_response = s3.put_bucket_acl(Bucket=bucket_name, ACL='public-read-write')
    print('config_response = ', config_response)

    # Delete unnecessary S3 resource - change detection should have occurred by now
    delete_response = s3.delete_bucket(Bucket=bucket_name)
    print('delete_response = ', delete_response)
