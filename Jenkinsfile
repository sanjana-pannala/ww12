
pipeline {
    agent any

    stages {

        stage('Checkout SCM') {
            steps {
                echo 'Checking out source code'
                checkout scm
            }
        }

        stage('Run Selenium Tests with pytest') {
            steps {
                echo 'Installing Python dependencies'
                bat 'python -m pip install -r requirements.txt'

                echo 'Starting Flask application'
                bat 'start /B python app.py'

                echo 'Waiting for Flask application'
                sleep time: 5, unit: 'SECONDS'

                echo 'Running Selenium tests'
                bat 'python -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image'
                bat 'docker build -t seleniumdemoapp1:v1 .'
            }
        }

        stage('Docker Login') {
            steps {
                echo 'Logging in to Docker Hub'
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-credentials',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_TOKEN'
                    )
                ]) {
                    bat 'docker login -u "%DOCKER_USER%" --password-stdin'
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                echo 'Tagging Docker image'
                bat 'docker tag seleniumdemoapp1:v1 sanjana26122005/week12-registrationapp:v1'

                echo 'Pushing Docker image'
                bat 'docker push sanjana26122005/week12-registrationapp:v1'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo 'Applying Kubernetes deployment'
                bat 'kubectl apply -f deployment.yaml --validate=false'

                echo 'Applying Kubernetes service'
                bat 'kubectl apply -f service.yaml --validate=false'

                echo 'Checking deployment status'
                bat 'kubectl rollout status deployment/kubedemoapp-deployment --timeout=120s'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Please check the console logs.'
        }

        always {
            echo 'Jenkins pipeline execution finished.'
        }
    }
}
