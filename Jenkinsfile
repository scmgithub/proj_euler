pipeline {
    agent { docker { image 'python:3.10.1-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh '''
                    python -c "print(\'Go hang a salami!  I\'m a lasagna hog!\')"
                    ls -lah
                '''
            }
        }
    }
}