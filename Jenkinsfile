pipeline {
    
    agent any

    environment {
        SCANNER_HOME = tool 'sonar-scanner'
        IMAGE_NAME = "idrisniyi94/flask-ecom"
        IMAGE_TAG = "${BUILD_NUMBER}"
        CONTAINER_NAME = "lab-server-flask-ecom"
    }

    stages {
        stage("Sonarqube Scan") {
            steps {
                withSonarQubeEnv('sonar-server') {
                    sh "$SCANNER_HOME/bin/sonar-scanner -Dsonar.projectKey=flask-ecom -Dsonar.projectName=flask-ecom"
                }
            }
        }
    }
}