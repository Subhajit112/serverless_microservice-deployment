# serverless_microservice-deployment

This project demonstrates a complete serverless microservice deployment using **AWS Lambda**, **API Gateway**, **DynamoDB**, and **Terraform**, along with a CI/CD pipeline managed via **Jenkins**.

## 🚀 Features

- RESTful user profile API powered by AWS Lambda
- Infrastructure as Code using Terraform
- API Gateway integration with Lambda
- DynamoDB as the backend data store
- Jenkins pipeline for automated deployment and packaging
- Secure IAM roles and policies
- Scalable and cost-effective architecture

## 🗂 Project Structure

serverless_microservice-deployment/
├── lambda/ # Lambda function handler and dependencies
│ ├── user_handler.py
│ └── requirements.txt
├── terraform/ # Terraform code for AWS infrastructure
│ ├── main.tf
│ ├── variables.tf
│ ├── iam.tf
│ ├── lambda.tf
│ ├── dynamodb.tf
│ ├── api_gateway.tf
│ └── outputs.tf
├── Jenkinsfile # Jenkins pipeline for CI/CD
├── tests/ # Basic unit tests for Lambda
│ └── test_lambda.py
├── lambda_function_payload.zip # Zipped deployment package
└── README.md
└── .gitignore


## 🧪 How to Deploy

### Prerequisites

- AWS CLI configured
- Terraform v1.0+
- Python 3.9+
- Jenkins installed (locally or on a server)

### 1. Set up Terraform Infrastructure

```bash
cd terraform
terraform init
terraform apply -auto-approve
```
### 2. Deploy with Jenkins
Use the provided Jenkinsfile to create a CI/CD pipeline:

- Checks out code
- Packages Lambda
- Deploys infrastructure
- Updates Lambda function code

### 3. Test the API
After deployment, use the API Gateway URL from Terraform output to test:

```bash
curl https://<api_id>.execute-api.<region>.amazonaws.com/dev/users
```
### 4. Security
- Uses IAM roles with least privilege for Lambda
- All API calls restricted via method authorization (can be extended)
