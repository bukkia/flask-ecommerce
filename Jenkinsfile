pipeline {
    agent any

    environment {
        SCANNER_HOME = tool 'sonar-scanner'
        IMAGE_NAME = "aolubukade/flask-ecommerce"
        IMAGE_TAG = "${BUILD_NUMBER}"
        CONTAINER_NAME = "abiolao-flask-ecom-flask-ecom"
    }

    stages {

        stage("Sonarqube Scan") {
            steps {
                withSonarQubeEnv('sonar-server') {
                    sh '''
                        $SCANNER_HOME/bin/sonar-scanner \
                        -Dsonar.projectKey=flask-ecomm \
                        -Dsonar.projectName=flask-ecomm \
                        -Dsonar.python.coverage.reportPaths=coverage.xml
                    '''
                }
            }
        }

        stage("Push Docker Image") {
            steps {
                sh 'docker push ${IMAGE_NAME}:${IMAGE_TAG}'
                echo "Docker image pushed successfully"
            }
        }
    }
}
