pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ranjan1522/curaHealthCare.git'
            }
        }

        stage('Set up Python Environment') {
            steps {
                 bat """
                    pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
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
