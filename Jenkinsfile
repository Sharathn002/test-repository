pipeline {
    agent any
  parameters {
        choice(name: 'service_type', choices: ['c2s','s2s'], description: 'Select the type of the service')
        choice(name: 'env', choices: ['stage','production'], description: 'Select the type of the environment')
        string(name: 'id', defaultValue: '', description: 'Enter the id')
    }
  stages {
    stage('silencing alert') {
            steps {
              sh """python3 fetch_all_evidences.py --service_type ${params.service_type} --id ${params.id} --env ${params.env}"""
            }
          }
  }

}
