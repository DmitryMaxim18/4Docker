pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                echo 'Hello World'
                script {
                    git credentialsId: 'test_pipeline', url: 'https://github.com/DmitryMaxim18/4Docker.git'
                    sh 'git checkout */main'
                }
                sh 'ls'
            }
        }
        stage('Preparing') {
            steps {
                sh 'python3 -m pip install -r req.txt'
            }
        }
        stage('Run') {
            agent {
                node {
                    label 'www'
                    customWorkspace '/usr/src/rep/regular'
                }
            }
            steps {
                sh 'pytest -n 5 -m shallow --junitxml=result.xml'
            }
            post {
                always {
                    junit 'result.xml'
                }
            }
        }
    }
}
