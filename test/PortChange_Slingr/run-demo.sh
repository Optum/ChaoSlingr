#!/bin/bash
echo "Configuring Test Environment"
./configure-test-groups.sh >> demo.out

echo "Testing TCP slinging"
SECURITY_GROUP_ID=`./get-tf-output.sh security_group_id_truetag`
PROTOCOL='tcp'
FROM_PORT=22
TO_PORT=25
./run-lambda.py $SECURITY_GROUP_ID $PROTOCOL $FROM_PORT $TO_PORT >> demo.out
./verify-lambda.py $SECURITY_GROUP_ID $PROTOCOL $FROM_PORT $TO_PORT

echo "Testing UDP slinging"
SECURITY_GROUP_ID=`./get-tf-output.sh security_group_id_truetag`
PROTOCOL='udp'
FROM_PORT=32
TO_PORT=35
./run-lambda.py $SECURITY_GROUP_ID $PROTOCOL $FROM_PORT $TO_PORT >> demo.out
./verify-lambda.py $SECURITY_GROUP_ID $PROTOCOL $FROM_PORT $TO_PORT
