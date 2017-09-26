#!/usr/bin/env python
import sys
import boto3
import json
import base64

securityGroupId = sys.argv[1]
protocol = sys.argv[2]
fromPort = int(sys.argv[3])
toPort = int(sys.argv[4])
boto3.setup_default_session(profile_name='ChaoSlingr')
client = boto3.client('lambda')
payload = json.dumps({'SecurityGroupId': securityGroupId,
    'IpProtocol': protocol,
    'FromPort': fromPort,
    'ToPort': toPort,
    'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
})
print("Invoking PortChange_Slingr for security group " + securityGroupId)
response = client.invoke(
    FunctionName='PortChange_Slingr',
    InvocationType='RequestResponse',
    LogType='Tail',
    Payload=payload
)
print(base64.b64decode(response[u'LogResult']))
