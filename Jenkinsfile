pipeline {
    agent any

    environment {
        IMAGE_NAME = "aolubukade/flask-ecommerce:v1"
        IMAGE_TAG = "${BUILD_NUMBER}"
        CONTAINER_NAME = "abiolao-flask-ecom"
    }

    stages {

        stage("Push Docker Image") {
            steps {
                sh 'docker push ${IMAGE_NAME}:${IMAGE_TAG}'
                echo "Docker image pushed successfully"
            }
        }
    }
}
