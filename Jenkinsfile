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
    post {
        always {
            echo 'In post, this will always run.'
        }
        success {
            echo 'This runs if successful.'
        }
        failure {
            echo 'This runs if failure.'
        }
        unstable {
            echo 'This runs if build was considered unstable, however that works.'
        }
        changed {
            echo 'This will run only if the state of the pipeline has changed.'
            echo 'For example, if the pipeline was previously failing but is now successful.'
        }
    }
}