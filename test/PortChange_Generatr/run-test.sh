#!/bin/bash
./configure-test-groups.sh

echo "***Testing Generatr.***"
TAG_NAME='OptMeInTest'
./run-lambda.py $TAG_NAME
SECURITY_GROUP_ID=`./get-tf-output.sh security_group_id_truetag`
./verify-lambda.py $SECURITY_GROUP_ID 1
SECURITY_GROUP_ID=`./get-tf-output.sh security_group_id_falsetag`
./verify-lambda.py $SECURITY_GROUP_ID 0
SECURITY_GROUP_ID=`./get-tf-output.sh security_group_id_notag`
./verify-lambda.py $SECURITY_GROUP_ID 0

./cleanup-test-groups.sh
