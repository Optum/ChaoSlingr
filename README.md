![ChaoSlingr Diagram](./docs/choas.jpg)

# HACKRU challenge
Best pull request for a feature or experiment (deadline is Sunday)

# How to begin
You will need installed on your workstation docker, node, and python
1. `git clone -b hackru https://github.com/Optum/ChaoSlingr.git`
2. `virtualenv hacked`
3. `source hacked/bin/activate`
4. `pip install localstack`
5. `npm install -g aws-sam-local'
6. `localstack start` or if you want to run in background `localstack start &`
7. `aws --endpoint-url=http://localhost:4572 s3api create-bucket --bucket test-bucket --region us-east-1` (you just made your first AWS call!)
8. `cd test/bucketpolicy`
9. `sam local invoke slingrFunction -e slingr_event.json` (just ran your first experiment!)

# If you found AWS Credit begin by
Find some AWS credit and make your own account to move from local env to public cloud. 

# ChaoSlingr: Introducing Security into Chaos Testing
ChaoSlingr is a Security Chaos Engineering Tool focused primarily on the experimentation on AWS Infrastructure to bring system security weaknesses to the forefront.

Join the community - https://chaoslingr.slack.com
