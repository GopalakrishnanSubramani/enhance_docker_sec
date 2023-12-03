node{
     
    stage('SCM Checkout'){
        git url: 'https://github.com/GopalakrishnanSubramani/enhance_docker_sec',branch: 'main'
    }

     stage('Running the Image building'){
        sh ./enhance_docker_sec/build_img.sh
     }

     stage('Scanning the Images'){
        sh ./enhance_docker_sec/scan_img.sh
     }    
}
