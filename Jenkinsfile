pipeline {
    
    agent any

    environment {
        SCANNER_HOME = tool 'sonar-scanner'
        IMAGE_NAME = "abiolao/flask-ecom:stable"
        IMAGE_TAG = "${BUILD_NUMBER}"
        CONTAINER_NAME = "abiolao-flask-ecom"
    }

    stages {
        stage("Install Dependencies & Run Tests") {
            steps {
                script {
                    sh 'pip install -r requirements.txt --break-system'
                    sh 'pytest --cov=. --cov-report=xml'
                }
            }
        }
        stage("Sonarqube Scan") {
            steps {
                withSonarQubeEnv('sonar-server') {
                    sh "$SCANNER_HOME/bin/sonar-scanner -Dsonar.projectKey=flask-ecom -Dsonar.projectName=flask-ecom -Dsonar.python.coverage.reportPaths=coverage.xml"
                }
            }
        }
    }
}