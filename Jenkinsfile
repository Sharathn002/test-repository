pipeline {
    agent any

    parameters {
        stashedFile 'input_log.log'
        string(name: 'connection_id', defaultValue: '', description: 'Enter the connection_id')
        choice(choices: ['session_id', 'date', 'time_range'], description: 'select the filter choice by which log files should be filtered', name: 'myChoice')
    }
    
    stages {
        stage("upload"){
            steps{
                unstash 'input_log.log'
            }

        }
        stage("ls"){
            steps{
            sh "ls -al"
            }
        }
        stage('Enter parameters') {
            steps {
                script {
                    def userInput
                    if (params.myChoice == 'session_id') {
                        userInput = input(
                            message: 'Please enter the session_id by which the log file should be filtered',
                            parameters: [
                                string(defaultValue: '000', description: 'Enter the session_id', name: 'session_id')
                            ]
                        )
                    } else if (params.myChoice == 'date') {
                        userInput = input(
                            message: 'Please enter the date by which the log file should be filtered',
                            parameters: [
                                string(defaultValue: '2000-01-01', description: 'Enter a date in YYYY-MM-DD format', name: 'date')
                            ]
                        )
                    }else if (params.myChoice == 'time_range') {
                        userInput = input(
                            message: 'Please enter the date and time_range by which the log file should be filtered',
                            parameters: [
                                string(defaultValue: '2000-01-01', description: 'Enter the date in YYYY-MM-DD format', name: 'date'),
                                string(defaultValue: '00:00:00', description: 'Enter the START time in HH:MM:SS format', name: 'start_time'),
                                string(defaultValue: '00:00:00', description: 'Enter the END time in HH:MM:SS format', name: 'end_time')
                            ]
                        )
                    } else {
                        echo 'No parameters required for this branch'
                    }

                    if (userInput) {
                        if (params.myChoice == 'session_id') {
                            sh """python3 test.py ${params.myChoice} --connection_id ${params.connection_id} --session_ID ${userInput}"""  
                        } else if (params.myChoice == 'date') {
                            sh """python3 test.py ${params.myChoice} --connection_id ${params.connection_id} --dates ${userInput}"""
                        } else if (params.myChoice == 'time_range') {
                            sh "python3 test.py ${params.myChoice} --connection_id ${params.connection_id} --dates ${userInput.date} --start_time ${userInput.start_time} --end_time ${userInput.end_time}"
                        }

                    }
                }
            }
        }
    }
}
