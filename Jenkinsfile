// pipeline {
//   agent any
// //   parameters {
// //     string(name: 'cluster_name', defaultValue: 'None', description: 'Enter the cluster name')
// //     string(name: 'region', defaultValue: 'None', description: 'Enter the region name in"jp tok" formate')
// //     string(name: 'API_token', defaultValue: 'None', description: 'Enter the api token of that region')
// //     string(name: 'duration_in_hours', defaultValue: 1.5, description: 'Enter the duration for the silencing')
// //   }
//   stages {
//     stage('silencing alert') {
//       steps {
//         sh 'python3 silencing_rule.py '
//       }
//     }
//      stage('sleep') {
//        steps {
//          sleep time: 60, unit: 'SECONDS' 
//        }
//      }
//      stage('crash') {
//        steps {
//          sh 'python3 crash.py'
//        }
//        post {
//          always {
//                sh 'python3 deleting_silencing_rule.py '
//                }
//            }
//     }
//      stage('deleting silencing rule') {
//        steps {
//          sh 'python3 deleting_silencing_rule.py '
//        }
//      }
//   }
  
// }
pipeline {
  agent any
  parameters {
    string(name: 'arg1', defaultValue: 'default_arg1', description: 'First argument for Python script')
    string(name: 'arg2', defaultValue: 'default_arg2', description: 'Second argument for Python script')
  }
  stages {
    stage('Run Python Script') {
      steps {
        sh """
          python3 my_script.py ${params.arg1} ${params.arg2}
        """
      }
    }
  }
}
