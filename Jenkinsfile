node{
     
    stage('SCM Checkout'){
        git url: 'https://github.com/GopalakrishnanSubramani/enhance_docker_sec',branch: 'main'
    }

    stage('SCM Checkout'){
        sh './enhance_docker_sec/build_img.sh'
    }

    stage('SCM Checkout'){
        sh './enhance_docker_sec/scan_img.sh'
    }
}
