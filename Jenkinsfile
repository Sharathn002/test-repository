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
              sh """python3 fetch_all_evidences.py --service_type "c2s" --id "we432we4r32" --env "prod""""
            }
          }
  }

}
