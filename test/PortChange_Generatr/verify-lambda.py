#!/usr/bin/env python
import sys
import boto3
import json
import base64

class colors:
    SUCCESS = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

securityGroupId = sys.argv[1]
numberOfChangesExpected = sys.argv[2]
boto3.setup_default_session(profile_name='ChaoSlingr')
client = boto3.client('ec2')
print("Validating PortChange_Generatr for security group " + securityGroupId)
response = client.describe_security_groups(GroupIds=[securityGroupId])
changeFound = False
if 'SecurityGroups' in response and 'IpPermissions' in response['SecurityGroups'][0] and len(response['SecurityGroups'][0]['IpPermissions']) == int(numberOfChangesExpected):
    changeFound = True
if changeFound:
    print(colors.SUCCESS + "***Test successful.***" + colors.ENDC)
else:
    print(colors.FAIL + "***Test FAILED.***" + colors.ENDC)
