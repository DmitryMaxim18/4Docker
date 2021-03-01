pipeline {
    agent any
    stages {
        stage('Build') {
            agent {
                node {
                    label 'www'
                    customWorkspace '/usr/src/rep/regular/regular/regular/'
                }
            }
            steps {
                echo 'Hello World'
                sh 'pwd'
                sh 'ls'
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
