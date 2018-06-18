def IMAGE_NAME="auth-service"
def CONTAINER_NAME ="auth-service-cont"
def CONTAINER_TAG="latest"
def HTTP_PORT="5000"

node {
    stage('Build') {
        imagePrune(CONTAINER_NAME)
        sh "ls"

    }
    stage('Deploy'){
         sh "ls"
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