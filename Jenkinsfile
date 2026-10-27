pipeline {
    agent any

    stages {
        stage('Run Selenium Tests with pytest') {
    steps {
        echo "Running Selenium Tests using pytest"

        // 1. Install dependencies
        bat 'pip install -r requirements.txt'

        // 2. Start Flask app in the background
        bat 'start /B python app.py'

        // 3. Built-in sleep (avoids "ping not recognized" or "null" exit codes)
        sleep time: 5, unit: 'SECONDS'

        // 4. Run pytest
        bat 'pytest -v'
    }
}

        stage('Build Docker Image') {
            steps {
                echo "Build Docker Image"
                bat "docker build -t seleniumdemoapp1:v1 ."
            }
        }

        stage('Docker Login') {
            steps {
                bat 'docker login -u bhavyasrip -p Bhavya2612@@'
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                echo "Push Docker Image to Docker Hub"
                bat "docker tag seleniumdemoapp:v1 bhavyasrip/week12-registrationapp:v1"
                bat "docker push bhavyasrip/week12-registrationapp:v1"
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                // apply deployment & service
                bat 'kubectl apply -f deployment.yaml --validate=false'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}