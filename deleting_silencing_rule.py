
#this is the python script to delete the silencing rule 
import requests
import json
from datetime import datetime
import sys
def disable_silencing_alert(json_data):


    for dict in json_data:
        
        api_token=dict["api_token"]

        #This is the endpoint for the silencing
        silencing_url='https://'+dict['region'].split('_')[0].lower()+'-'+dict['region'].split('_')[1].lower()+'.monitoring.cloud.ibm.com/api/v1/silencingRules'

        #this is the endpoint for disabling the silencing rule
        disable_url=silencing_url+'/disable'
        # print(disable_url)

        headers = {'Authorization': f'Bearer {api_token}', 'Content-Type': 'application/json'}
        response = requests.get(silencing_url, headers=headers)

        if response.status_code == 200:
            silence_rules = response.json()
            for silence_rule in silence_rules:
                
                #current date and time
                now=datetime.now()
                curr_time_in_millisec = now.timestamp() * 1000

                #end time of the silencing_rule in milliseconds
                silence_end_time=silence_rule['startTs']+(silence_rule['durationInSec']*1000)

                # if (dict["cluster_name"] in silence_rule['scope']): # this condition is used to  check all the silencing rule with the same cluster name 

                #this condition is used to  check all the silencing rule with the same cluster name and to check whether the curr_time_in_millisec is lesser than silence_end_time
                if (dict["cluster_name"] in silence_rule['scope']) and (curr_time_in_millisec < silence_end_time) and (silence_rule['enabled']==True):
                    print(silence_rule['id'])
                    rule_id=silence_rule['id']
                    delete_silencing_url=silencing_url+f"/{rule_id}"
                    # print(delete_silencing_url)
                    response = requests.delete(delete_silencing_url, headers=headers)
                    if response.status_code == 200:
                        print(f'Silencing rule with id:{rule_id} deleted successfully.')
                    else:
                        print('Failed to delete silencing rule. Status code:', response.status_code)


        else:
            print(f'Request failed with status code {response.status_code}')




def main():

    #converting the json file into python objects
    duration=float(sys.argv[4])

    json_data=[
      {
        "list_of_regions_available":["US South","EU DE","EU GB","JP OSA","JP TOK","US East","AU SYD","CA TOR","BR SAO"],
        "region":sys.argv[2],
        "api_token": sys.argv[3],
        "cluster_name":sys.argv[1],
        "duration_in_hours": duration
      }
    ]
#     print(json_data[0]["region"])
#     print(json_data[0]["api_token"])
#     print(json_data[0]["cluster_name"])
#     print(json_data[0]["duration_in_hours"])
#     print(type(json_data[0]["duration_in_hours"]))

    disable_silencing_alert(json_data)
    
if __name__=='__main__':
    main()
