Port Change
------------

### Experiment

One of the common indicators of a breach is unexpected ports being opened or closed.  This experiment introduces that misconfiguration into the environment so that monitoring, alerting, and correction mechanisms can be validated.

### PortChange_Generatr

PortChange_Generatr kicks off the experiment.  It selects a random security group that is tagged with the specified opt-in tag and picks a random port range to open for ingress with either TCP or UDP access.

#### Input Parameters

*TagName*

The opt-in tag that designates that a security group is eligible to be selected for the experiment.

#### Sample Input Event

```
{
    "TagName": "OptMeIn"
}
```

### PortChange_Slingr

PortChange_Slingr makes the change to the security group.

#### Input Parameters

*SecurityGroupId*

The ID of the security group to modify.

*IpProtocol*

The IP protocol to use.  Acceptable values are "tcp" and "udp".

*FromPort*

The starting port of the range to open.

*ToPort*

The ending port of the range to open.

*IpRanges*

The range of IP addresses allowed to access the opened ports.

#### Sample Input Event

```
{
    "SecurityGroupId": "sg-245e834c",
    "IpProtocol": "tcp",
    "FromPort": 19984,
    "ToPort": 19989,
    "IpRanges": [{"CidrIp": "0.0.0.0/0"}]
}
```

### PortChange_Slack_Trackr
PortChange_Slack_Trackr discovers the changes made by PortChanger_Generatr. Triggered by cloud watch events that are monitoring for security group changes. Once discovered a notification will be sent to specified Slack Channel.  See [Incoming Slack Webhooks](https://api.slack.com/incoming-webhooks) for information on how to set up a webhook if one is needed.  See [PortChange_Slack_Tracker Setup](../docs/PortChange_Slack_Trackr.md) for information on how to configure the events that invoke PortChange_Slack_Trackr.

#### Lambda Environment Variables

*channel*

The Slack Channel

*hook*

The webhook for Slack Channel (This should be stored in S3 and encrypted)

#### Sample Input Event

```
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "xxxxxxxxxxxxxxx:michael.michael.michael@michael.com",
        "arn": "arn:aws:sts::xxxxxxxxxxxxxxx:assumed-role/xxxxxxxxxxxxxxx/michael.michael.michael@michael.com",
        "accountId": "xxxxxxxxxxxxxxx",
        "accessKeyId": "xxxxxxxxxxxxxxx",
        "sessionContext": {
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2017-09-15T17:57:59Z"
            },
            "sessionIssuer": {
                "type": "Role",
                "principalId": "xxxxxxxxxxxxxxx",
                "arn": "arn:aws:iam::xxxxxxxxxxxxxxx:role/xxxxxxxxxxxxxxx",
                "accountId": "xxxxxxxxxxxxxxx",
                "userName": "xxxxxxxxxxxxxxx"
            }
        }
    },
    "eventTime": "2017-09-15T17:59:15Z",
    "eventSource": "ec2.amazonaws.com",
    "eventName": "AuthorizeSecurityGroupIngress",
    "awsRegion": "us-east-2",
    "sourceIPAddress": "xxxxxxxxxxxxxxx",
    "userAgent": "console.ec2.amazonaws.com",
    "requestParameters": {
        "groupId": "sg-xxxxxxxxxxxxxxx",
        "ipPermissions": {
            "items": [
                {
                    "ipProtocol": "6",
                    "fromPort": 31000,
                    "toPort": 31000,
                    "groups": {},
                    "ipRanges": {
                        "items": [
                            {
                                "cidrIp": "0.0.0.0/0"
                            }
                        ]
                    },
                    "ipv6Ranges": {},
                    "prefixListIds": {}
                }
            ]
        }
    },
    "responseElements": {
        "_return": true
    },
    "requestID": "xxxxxxxxxxxxxxx",
    "eventID": "xxxxxxxxxxxxxxx",
    "eventType": "AwsApiCall",
    "recipientAccountId": "xxxxxxxxxxxxxxx"
}
```

#### Sample Output Event

```
{
  'Name': 'assumed-role/ROLEROLE/michael.michael.michael@michael.com'
  'Description': 'Warning: There were port changes made',
  'SecurityGroup': 'sg-12345678',
  'Ports':[
    30001-30005
  ],
  Protocols: [
    'TCP'
  ],
  Ranges: [
    '0.0.0.0/0'
  ]
}
```
