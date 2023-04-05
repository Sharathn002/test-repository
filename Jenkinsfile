pipeline {
   agent any
   parameters {
      string(name: 'FUNCTION', defaultValue: '', description: 'Name of function to call')
      string(name: 'ARG1', defaultValue: '', description: 'First argument')
      string(name: 'ARG2', defaultValue: '', description: 'Second argument')
   }
   stages {
      stage('Run Python Script') {
         steps {
            sh "python your_script.py create --arg1 ${params.ARG1} --arg2 ${params.ARG2}"
         }
      }
   }
}
