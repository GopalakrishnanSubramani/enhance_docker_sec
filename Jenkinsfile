node{
     
    stage('SCM Checkout'){
        git url: 'https://github.com/GopalakrishnanSubramani/enhance_docker_sec',branch: 'main'
    }

    stage('Image Build'){
        sh './build_img.sh'
    }

    stage('Image Scan'){
        sh './scan_img.sh'
    }
     
    stage('show sample output'){
         cat image_1.txt    
    }     
}
