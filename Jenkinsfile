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
        sh "pwd"
        sh "ls -la"

    }
    stage('Deploy'){
         sh "pwd"
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