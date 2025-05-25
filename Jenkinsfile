pipeline {
    agent any

    environment {
        IMAGE_NAME = "olubukade/flask-ecommerce"
        IMAGE_TAG = "v1-${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/bukkia/flask-ecommerce.git', branch: 'main'
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG .'
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push $IMAGE_NAME:$IMAGE_TAG'
                echo 'Docker image pushed successfully'
            }
        }
    }
}
