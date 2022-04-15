pipeline {
    agent { docker { image 'python:3.10.1-alpine' } }

    environment{
        STEVE_VAR = 'awesome'
        MATTHEW_VAR = 'even awesomer'
    }

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
    pass;"
'''
                }
                timeout(time: 3, unit: 'MINUTES') {
                    sh 'python divisors_slow.py'
                }
            }
        }

        stage('arbitrary stage name') {
            steps{
                echo "Steve is ${STEVE_VAR}"
                echo "Matthew is ${MATTHEW_VAR}"
                sh 'printenv'
            }
        }

        stage('sanity check') {
            steps {
                input "Should I continue with the build?  (How will this work???)"
            }
        }

        stage('continuing') {
            steps{
                echo 'looks like we are continuing to the end...'
            }
        }
    }
    post {
        always {
            echo 'In post, this will always run.'
        }
        success {
            echo 'This runs if successful.'
            // localhost needs Java mail setup to send mail
            // mail to: 'stevem1191@yahoo.com',
            //      subject: "Successful Pipeline: ${currentBuild.fullDisplayName}",
            //      body: "${env.BUILD_URL} worked out great."
        }
        failure {
            echo 'This runs if failure.'
            // mail to: 'stevem1191@yahoo.com',
            //      subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
            //      body: "Something is wrong with ${env.BUILD_URL}"
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