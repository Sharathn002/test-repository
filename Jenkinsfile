pipeline {
    agent any

    parameters {
        string(name: 'connection_id', defaultValue: '', description: 'Enter the connection_id')
        choice(choices: ['session_id', 'date', 'time_range'], description: 'select the filter choice by which log files should be filtered', name: 'myChoice')
    }

    stages {
        stage('Enter parameters') {
            steps {
                script {
                    def userInput
                    if (params.myChoice == 'session_id') {
                        userInput = input(
                            message: 'Please enter the session_id by which the log file should be filtered',
                            parameters: [
                                string(defaultValue: '', description: 'Enter the session_id', name: 'session_id')
                            ]
                        )
                    } else if (params.myChoice == 'date') {
                        userInput = input(
                            message: 'Please enter the date by which the log file should be filtered',
                            parameters: [
                                string(defaultValue: '', description: 'Enter a date in YYYY-MM-DD format', name: 'date'),
                            ]
                        )
                    }else if (params.myChoice == 'time_range') {
                        userInput = input(
                            message: 'Please enter the date and time_range by which the log file should be filtered',
                            parameters: [
                                string(defaultValue: '', description: 'Enter the date in YYYY-MM-DD format', name: 'date'),
                                string(defaultValue: '00:00:00', description: 'Enter the START time in HH:MM:SS format', name: 'start_time'),
                                string(defaultValue: '00:00:00', description: 'Enter the END time in HH:MM:SS format', name: 'end_time')
                            ]
                        )
                    } else {
                        echo 'No parameters required for this branch'
                    }

                    if (userInput) {
                        echo "User entered string: ${userInput.myStringParam}"
                        echo "User selected option: ${userInput.myChoiceParam}"
                        echo "User entered other string: ${userInput.myOtherStringParam}"
                        echo "User selected boolean: ${userInput.myBoolParam}"

                        if (params.myChoice == 'session_id') {
                            sh "python3 test.py ${params.myChoice} --connection_id ${params.connection_id} --session_id ${userInput.session_id}"  
                        } else if (params.myChoice == 'date') {
                            sh "python3 test.py ${params.myChoice} --connection_id ${params.connection_id} --date ${userInput.date}"
                        } else if (params.myChoice == 'time_range') {
                            sh "python3 test.py ${params.myChoice} --connection_id ${params.connection_id} --date ${userInput.date} --start_time ${userInput.start_time} --end_time ${userInput.end_time}"
                        }

                    }
                }
            }
        }
    }
}
