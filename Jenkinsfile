pipeline{
    agent any
    stages{
        stage('Clone'){
            steps{
                git branch:'main', url:'https://github.com/ThakurSahilSingh/pytest.git'
            }
        }
        //stage('Adding Files'){
        //    steps{
        //        sh '''
        //        cp /root/pytest/* /root/.jenkins/workspace/pytest/
        //        '''
        //    }
        //}
        stage('Build'){
            steps{
                sh '''
                docker build -t sahil0824/pytest:latest .
                '''
            }
        }
        stage('Test'){
            steps{
                sh '''
                docker run -d sahil0824/pytest:latest
                '''
            }
        }
        stage('Deploy'){
            steps{
                withCredentials([usernamePassword(credentialsId: 'docker-cred', passwordVariable: 'docker-pass', usernameVariable: 'docker-user')]){
                    sh '''
                    docker login -u "$docker-user" -p "$docker-pass"
                    docker push sahil0824/pytest:latest
                    '''
                }
            }
        }
    }
}
