node{
     
    stage('SCM Checkout'){
        git url: 'https://github.com/GopalakrishnanSubramani/enhance_docker_sec',branch: 'main'
    }

    // stage('Image Build'){
    //      echo " ******************* "
    //      sh "chmod +x -R ${env.WORKSPACE}"     
    //      sh './build_img.sh'
    // }

    // stage('Image Scan'){
    //     sh './scan_img.sh'
    // }
     
    stage('show sample output'){
        sh 'cat image_1.txt'    
    }     
}
