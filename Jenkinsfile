pipeline {
  agent any
  parameters {
    string(name: 'cluster_name', defaultValue: 'webapCluster/cfvdf6ef0lb6gpb1puig', description: 'Enter the cluster name')
    string(name: 'region', defaultValue: '"jp tok"', description: 'Enter the region name in ' ' formate. ex:"jp tok" ')
    string(name: 'api_token', defaultValue: '3e91771e-40d2-42cd-96ac-ebe08462c96c', description: 'Enter the api token of that region')
    string(name: 'duration_in_hours', defaultValue: '1.5', description: 'Enter the duration for the silencing')
  }
  stages {
    stage('silencing alert') {
      steps {
        sh """python3 creating_silencing_rule.py ${params.cluster_name} ${params.region} ${params.api_token} ${params.duration_in_hours}"""
      }
    }
     stage('sleep') {
       steps {
         sleep time: 60, unit: 'SECONDS' 
       }
     }
//      stage('crash') {
//        steps {
//          sh 'python3 crash.py'
//        }
//        post {
//          always {
//                sh """python3 deleting_silencing_rule.py ${params.cluster_name} ${params.region} ${params.api_token} ${params.duration_in_hours}"""
//                }
//            }
//     }
     stage('deleting silencing rule') {
       steps {
         sh """python3 deleting_silencing_rule.py ${params.cluster_name} ${params.region} ${params.api_token} ${params.duration_in_hours}"""
       }
     }
  }
  
}
// pipeline {
//   agent any
//   parameters {
//     string(name: 'arg1', defaultValue: 'default_arg1', description: 'First argument for Python script')
//     string(name: 'arg2', defaultValue: 'default_arg2', description: 'Second argument for Python script')
//   }
//   stages {
//     stage('Run Python Script') {
//       steps {
//         sh """
//           python3 my_script.py ${params.arg1} ${params.arg2}
//         """
//       }
//     }
//   }
// }
