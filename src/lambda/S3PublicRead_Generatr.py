import boto3
from botocore.exceptions import ClientError
from random import randint
import random
import json
import time

s3 = boto3.client('s3')
ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    # Print even for debuggin
    print("event="event)

    # Generate unique bucket name
    unique_bucket_number = randint(100000,999999)
    bucket_name = 'publicReadable-experiment'+str(unique_bucket_number)
    print("bucket name will be: "+bucket_name)

    # Get target region
    target_region = ""

    if "region" in event:
        print("region parameter detected - experiment to be conducted in: ",event['region'])
        target_region = event['region']
    else:
        print("no region parameter passed - experiment conducted in random region")
        regions = [region['RegionName'] for region in ec2.describe_regions()['Regions']]
        print(regions)
        region_int = randint(0,regions.length-1)
        target_region = regions[region_int]
        print("experiment to be conducted in: "+target_region)

    # Create benign S3 bucket
    create_response = s3.create_bucket(ACL='private', Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': target_region})
    print('create_response = ', create_response)

    # Create payload for S3PublicRead_Slingr.py
    if bucket_name:
        s3_details = {'bucket_name': bucket_name}
        Package = json.dumps(s3_details)
        print(sgidnum + ' selected for slinging.')
        print(Package)
        response = client.invoke(
            FunctionName='S3PublicRead_Slingr',
            InvocationType='Event',
            Payload=Package
        )
    else:
        print('No security groups with opt-in tags found.  Doing nothing.')
