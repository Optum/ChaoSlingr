#!/usr/bin/python
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
protocol = sys.argv[2]
fromPort = int(sys.argv[3])
toPort = int(sys.argv[4])
boto3.setup_default_session(profile_name='ChaoSlingr')
client = boto3.client('ec2')
IpRanges = [{'CidrIp': '0.0.0.0/0'}]
print("Validating PortChange_Slingr for security group " + securityGroupId)
response = client.describe_security_groups(GroupIds=[securityGroupId])
changeFound = False
if 'SecurityGroups' in response and 'IpPermissions' in response['SecurityGroups'][0]:
    for IpPermission in response['SecurityGroups'][0]['IpPermissions']:
        if IpPermission['IpProtocol'] == protocol and IpPermission['FromPort'] == fromPort and IpPermission['ToPort'] == toPort and IpPermission['IpRanges'] == IpRanges:
            changeFound = True
            break
if changeFound:
    print(colors.SUCCESS + "***Test successful.***" + colors.ENDC)
else:
    print(colors.FAIL + "***Test FAILED.***" + colors.ENDC)
