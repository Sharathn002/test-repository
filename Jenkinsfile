pipeline {
    agent any
  parameters {
        choice(name: 'service_type', choices: ['c2s','s2s'], description: 'type of the service either s2s or c2s')
        choice(name: 'env', choices: ['stage','production'], description: 'environment refers to either stage or prod')
        string(name: 'id', defaultValue: '', description: 'id of the gateway or vpn server as per the service')
    }
  stages {
    stage('silencing alert') {
            steps {
//               sh """python3 fetch_all_evidences.py ${params.service_type} ${params.id} ${params.env} """
                sh """python3 fetch_all_evidences.py ${params.service_type} 45346345 prod"""
            }
          }
  }

}
