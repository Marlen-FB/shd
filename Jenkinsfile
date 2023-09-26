pipeline {
  agent any
  stages {
    stage('Log Tool Version') {
      steps {
        sh '''mvn --version
git --version
java -version'''
      }
    }

    stage('Build with Maven') {
      steps {
        sh 'mvn compile test package'
      }
    }

    stage('Post Build Steps') {
      steps {
        writeFile(file: 'status.txt', text: 'oye, funciono!')
      }
    }

  }
}