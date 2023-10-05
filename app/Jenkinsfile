pipeline {
    agent any
    environment {
        AWS_ACCOUNT_ID="223320623045"
        AWS_DEFAULT_REGION="us-east-2"
        IMAGE_REPO_NAME="ecr-demo-jenkins"
        IMAGE_TAG="latest"
        REPOSITORY_URI = "223320623045.dkr.ecr.us-east-2.amazonaws.com/ecr-demo-jenkins"
    }
   
    stages {
        
         stage('Logging into AWS ECR') {
            steps {
                script {
                sh """aws ecr get-login-password --region ${AWS_DEFAULT_REGION} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com"""
                }
                 
            }
        }
        
        stage('Clone Repository') {
            steps {
                git credentialsId: '156d07ae-9e32-47c8-a778-ca3621206016', url: 'https://github.com/Alexeanred/learning-docker-python-2.git'
            }
        }
  
        // Building Docker images
        stage('Building image') {
            steps {
                script {
                dockerImage = docker.build "${IMAGE_REPO_NAME}:${IMAGE_TAG}"
                }
            }
        }
   
        // Uploading Docker images into AWS ECR
        stage('Pushing to ECR') {
            steps {  
                script {
                        sh """docker tag ${IMAGE_REPO_NAME}:${IMAGE_TAG} ${REPOSITORY_URI}:$IMAGE_TAG"""
                        sh """docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}:${IMAGE_TAG}"""
                }
            }
        }
    }
}