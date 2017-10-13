from botocore.exceptions import ClientError
from random import randint
import random
import boto3
import json

ec2 = boto3.client('ec2')
client = boto3.client('lambda')

## assumption: A security group other than the default security group must exist ##

def addport(sgidnum):
    FromPort = randint(10000,65000)
    ToPort = FromPort + randint(0,5)
    Protocols = ["tcp", "udp"]
    Cidr = "0.0.0.0/0"
    PortPackage = {'IpProtocol': Protocols[randint(0,1)],
        'FromPort': FromPort,
        'ToPort': ToPort,
        'IpRanges': [{'CidrIp': Cidr}],
        'SecurityGroupId': sgidnum
    }
    return PortPackage


# get security group permissions
def getSecGroupIPPermissions(SGidNum):
    permissions = ec2.SecurityGroup(SGidNum).ip_permissions
    return permissions

# get a random security group ID number from the secgroup id list
def changeR(SGlist):
    sgid = randint(0,len(SGlist)-1)
    return SGlist[sgid]

# this function populates a list of security group id's that have the opt-in tag set to true
def getSGList(tagname):
    slinglist = []
    response = ec2.describe_security_groups()
    for securityGroup in response['SecurityGroups']:
        if 'Tags' in securityGroup:
            for tag in securityGroup['Tags']:
                if tag['Key'] == tagname:
                    if tag['Value'].lower() == "true":
                        print(securityGroup['GroupId'] + ' has the opt-in tag.')
                        slinglist.append(securityGroup['GroupId'])
                        break
    return slinglist

def lambda_handler(event, context):
    print(event)
    slingSG_List = []
    optintag = ""
    if "TagName" in event:
        optintag = event['TagName']
        slingSG_List = getSGList(optintag)
        if len(slingSG_List) >= 1:
            sgidnum = changeR(slingSG_List)
            PortChange = addport(sgidnum)
            Package = json.dumps(PortChange)
            print(sgidnum + ' selected for slinging.')
            print(Package)
            response = client.invoke(
                FunctionName='PortChange_Slingr',
                InvocationType='Event',
                Payload=Package
            )
        else:
            print('No security groups with opt-in tags found.  Doing nothing.')
    else:
        print("No opt-in tag specified.  Doing nothing.")
    #getSecGroupIPPermissions(sgidnum)
