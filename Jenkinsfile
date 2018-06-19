def IMAGE_NAME="auth-service"
def CONTAINER_NAME ="auth-service-cont"
def CONTAINER_TAG="latest"
def HTTP_PORT="5000"

pipeline {
    agent none
    stages {
        stage('Test') {
            agent {
                docker {
                    image 'python:3'
                }
            }
            steps {

                sh "echo 'some-test'"
            }
        }
    }
}
node {
    stage('Build') {
        imagePrune(CONTAINER_NAME)
        sh 'cd configs && ls'
        sh "export SERVICE_NAME=10"
        sh "echo $SERVICE_NAME"
        sh "docker build -t $IMAGE_NAME ."
    }
    stage('Deploy'){
         sh "docker run -p $HTTP_PORT:5000 -d --name=$CONTAINER_NAME  $IMAGE_NAME"
    }
}

def imagePrune(containerName){
    try {
        sh "docker image prune -f"
        sh "docker stop $containerName"
        sh "docker rm $containerName"
    } catch(error){
        sh "echo $error"

    }
}