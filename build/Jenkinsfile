node {
    stage ('Checkout') {
        checkout scm
    }
    stage ('GetUpdatedLambdaFiles') {
        sh '''
            git diff --name-only HEAD HEAD^  >> diff.txt
            echo "Here is the diff"
            cat diff.txt
            if grep -q src/lambda diff.txt; then
              grep py diff.txt | cut -d \'/\' -f3 > files.txt
              grep py files.txt | cut -d \'.\' -f1 > changedfiles.txt
              echo "FILENAME WITHOUT .py extension"
              cat changedfiles.txt
            else
              echo "No lambda file changed"
            fi
        '''
    }
    stage ('DeployLambdaFunctions') {
        def exists = fileExists 'changedfiles.txt'
        if (exists) {
          def props = readFile  'JenkinsConfig'
          String propString = props.toString();
          String[] propertiesArray = propString.split("\n")
          def propertyMap = [:]
          for (String property : propertiesArray) {
            propertyMap[property.substring(0,property.indexOf('='))] = property.substring(property.indexOf('=')+1).trim()
          }
          def fileNames = readFile 'changedfiles.txt'
          print fileNames
          List fileList = fileNames.split("\n")
          for (item in fileList) {
              deployLambda(propertyMap,item)
          }
       }
   }
}

def deployLambda(Map propertyMap, String functionName) {
	  print 'Deploying lambda function, ' + functionName + ' from the location, ' +  propertyMap['artifactLocation']
    withCredentials([string(credentialsId: 'AWS_DEPLOY_ID', variable: 'AWS_DEPLOY_KEY')]) {
      deployLambda([alias: '', artifactLocation: propertyMap['artifactLocation'],
            awsAccessKeyId: propertyMap['awsAccessKeyId'], awsRegion: propertyMap['awsRegion'],
            awsSecretKey: env.AWS_DEPLOY_KEY,
            deadLetterQueueArn: '', description:propertyMap['description'],
            environmentConfiguration: [kmsArn: ''], functionName: functionName,
            handler: functionName +'.lambda_handler', memorySize: propertyMap['memorySize'],
            role: propertyMap['role'], runtime: propertyMap['runtime'],
            securityGroups: '', subnets: '', timeout: '3', updateMode: 'full'])
            return true
    }
}
