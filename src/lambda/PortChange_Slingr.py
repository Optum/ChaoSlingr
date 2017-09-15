import boto3
from botocore.exceptions import ClientError
import random
import json

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    print(event)
    if 'SecurityGroupId' in event and 'IpRanges' in event and 'IpProtocol' in event and 'FromPort' in event:
        try:
            data = ec2.authorize_security_group_ingress(
                GroupId= event['SecurityGroupId'],
                IpPermissions=[
                    {'IpProtocol': event['IpProtocol'],
                    'FromPort': event['FromPort'],
                    'ToPort': event['ToPort'],
                    'IpRanges': event['IpRanges']
                    }
                ])
            print('Ingress Successfully Set %s' % data)
        except ClientError as e:
            print(e)
    else:
        print("One or more parameters are missing. Nothing to do.")
