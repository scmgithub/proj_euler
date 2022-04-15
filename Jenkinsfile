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
        }

        stage('deploy') {
            steps {
                retry(3) {
                    sh 'python prob002.py'
                    sh '''python -c "from random import randrange; 
r = randrange(3); 
print (r); 
if r>0:
    exit(1);"
'''
                }
                timeout(time: 3, unit: 'MINUTES') {
                    sh 'python divisors_slow.py'
                }
            }
        }
    }
}