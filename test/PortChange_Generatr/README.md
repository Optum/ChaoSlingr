Overview
------------

This folder contains a test of executing the PortChange_Generatr lambda function in AWS.  Verification is done by looking at the results of PortChange_Slingr since that lambda is called from PortChange_Generatr.  Terraform is used to create a temporary security group for the test.  The terraform state files are persisted locally.

Prerequisites
------------

* Docker
* Python
* AWS CLI

Files Needed to Run
------------

**subscription.tf**

You will need to create your own subscription.tf file with your AWS creds to be able to run this example.  This file is not included.  A sample subscription file, subscription.tf.sample, is provided with empty strings for all of the credentials.

**security-group.tf**

This is the terraform file that creates the security groups.

**variables.tf**

This is the declaration file for the variables that are used to run the test.

**terraform.tfvars**

This is the file that contains all the variables necessary for the test to run.

**outputs.tf**

This is the file that calls out the terraform outputs needed for later steps in the test.

**run-test.sh**

This script runs the end-to-end test.

**configure-test-groups.sh**

This script creates the security groups used for the test.

**cleanup-test-groups.sh**

This script runs a terraform destroy operation that cleans up what was created by configure-test-groups.sh.

**get-tf-output.sh**

This script gets the value of an output variable from terraform.  It takes one command line parameter of the name of the variable.

**run-lambda.py**

This script runs the PortChange_Generatr lambda function out in AWS.  It takes one command line parameter of the opt-in tag name.

**verify-lambda.py**

This script verifies the result of the PortChange_Generatr lambda function out in AWS.  It takes one command line parameter of the ID of the security group to check.

How to Run
------------

The following commands need to be run from this directory.  The initialize step only needs to be done once.  The values entered at the prompts should match what is in subscription.tf.

**Initialize**

```
aws configure --profile ChaoSlingr
```

**Run**

```
./run-test.sh
```
