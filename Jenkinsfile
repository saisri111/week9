
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t saisri12/registration-app:latest .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKERHUB_USER',
                    passwordVariable: 'DOCKERHUB_PASSWORD'
                )]) {
                    bat '''
                        @echo off
                        echo %DOCKERHUB_PASSWORD%| docker login -u %DOCKERHUB_USER% --password-stdin
                        if errorlevel 1 exit /b 1
                        docker push saisri12/registration-app:latest
                        if errorlevel 1 exit /b 1
                        docker logout
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat '''
                    set KUBECONFIG=C:\\Users\\saisr\\.kube\\config
                    kubectl apply -f k8s\\deployment.yaml
                    if errorlevel 1 exit /b 1
                    kubectl apply -f k8s\\service.yaml
                    if errorlevel 1 exit /b 1
                    kubectl rollout status deployment/kubedemoapp --timeout=180s
                    kubectl get pods
                    kubectl get services
                '''
            }
        }
    }

    post {
        success {
            echo 'Build, push and deployment completed successfully.'
        }
        failure {
            echo 'Pipeline failed. Check Console Output.'
        }
    }
}
