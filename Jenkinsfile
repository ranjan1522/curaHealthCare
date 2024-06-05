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
                    pytest --html=./report/report.html
                '''
            }
        }
    }

    post {
        always {
            // Archive the report
            archiveArtifacts artifacts: 'report/**', allowEmptyArchive: true

            // Publish HTML report
            publishHTML(target: [
                reportName: 'Test Report',
                reportDir: 'report',
                reportFiles: 'report.html',
                alwaysLinkToLastBuild: true,
                keepAll: true
            ])
        }
    }
}
