
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
            bat '''
                @echo off
                echo %DOCKER_TOKEN% | docker login -u "%DOCKER_USER%" --password-stdin
            '''
        }
    }
}
