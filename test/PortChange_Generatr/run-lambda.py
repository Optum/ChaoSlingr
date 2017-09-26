#!/usr/bin/env python
import sys
import boto3
import json
import base64

tagName = sys.argv[1]
boto3.setup_default_session(profile_name='ChaoSlingr')
client = boto3.client('lambda')
payload = json.dumps({'TagName': tagName})
print("Invoking PortChange_Generatr")
response = client.invoke(
    FunctionName='PortChange_Generatr',
    InvocationType='RequestResponse',
    LogType='Tail',
    Payload=payload
)
print(base64.b64decode(response[u'LogResult']))
