## Jenkins Configuration
This repository has the Jenkinsfile that can be used to deploy the lambda functions to aws.
Steps to create your own jenkins job
### Step1:
  Create a pipeline job in your jenkins instance and provide the github repository and credentials to access the jenkinsfile.
### Step2:
  Create a JenkinsConfig file and add all the configuration properties of your aws instance.
  Example file is provided in this repository.
### Step3:
  Create a jenkins secret key and store your aws key in there. (default id is AWS_DEPLOY_ID)
### Step4:
  Provide the id associated with the key in the JenkinsConfig file.
