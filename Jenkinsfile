pipeline {
    agent { docker { image 'python:3.10.1-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh '''
                    python prob001.py
                    ls -lah
                '''
            }
        stage('deploy') {
            steps {
                retry(3) {
                    sh 'python prob002.py'
                }
                timeout(time: 3, unit: 'SECONDS') {
                    sh 'python divisors_slow.py'
                }
            }
        }
        }
    }
}