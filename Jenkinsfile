pipeline {
    agent any

    environment {
        AWS_REGION = 'us-east-1'
        LAMBDA_ZIP = 'lambda_function_payload.zip'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/yourusername/user-profile-service.git'
            }
        }

        stage('Install Dependencies & Package Lambda') {
            steps {
                sh '''
                rm -rf package
                mkdir package
                pip install -r lambda/requirements.txt -t package/
                cp lambda/user_handler.py package/
                cd package
                zip -r ../${LAMBDA_ZIP} .
                cd ..
                '''
            }
        }

        stage('Terraform Init & Apply') {
            steps {
                dir('terraform') {
                    sh 'terraform init'
                    sh 'terraform apply -auto-approve'
                }
            }
        }

        stage('Deploy Lambda') {
            steps {
                sh """
                aws lambda update-function-code --function-name user_profile_service_lambda --zip-file fileb://${LAMBDA_ZIP} --region ${AWS_REGION}
                """
            }
        }
    }
}
