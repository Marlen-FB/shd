pipeline {
    agent none
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'valecz/apivcz:1.1'
                    args '-p 6001:6001' // Mapear el puerto 6001 del contenedor al puerto 6001 del host
                }
            }
            steps {
                script {
                    // Agrega tus comandos de Flask aquí
                    sh 'ls -a'
                   // sh 'rm -r migrations'
                   // sh 'rm -r instance'
                    //sh 'source env/bin/activate'
                    sh 'flask db init'
                    sh 'flask db migrate -m "initial_DB"'
                    sh 'flask db upgrade'
                    sh 'flask run --host=0.0.0.0 --port=6001'
                }
            }
        }
    }
}
