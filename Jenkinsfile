pipeline {
    agent any
    stages {
        stage('Checkout') {
            checkout([
                $class: 'GitSCM', branches: [[name: '*/main']],
                userRemoteConfigs: [[url: 'https://github.com/DmitryMaxim18/4Docker.git'],[credentialsId:'test_pipeline']]
            ])
            steps {
                echo 'Hello World'
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
