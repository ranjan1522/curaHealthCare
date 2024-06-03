pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: '7-corrections-in-yml-file', url: 'https://github.com/ranjan1522/curaHealthCare.git'
            }
        }

        stage('Set up Python Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    source ${VENV_DIR}/bin/activate
                    pytest --html=report.html
                '''
            }
            post {
                always {
                    archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
                    publishHTML(target: [
                        reportDir: '.',
                        reportFiles: 'report.html',
                        reportName: 'HTML Report'
                    ])
                }
            }
        }
    }
}
