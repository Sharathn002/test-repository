import re
import json
from datetime import datetime,timezone
import argparse

def filter_error_logs_on_session(file_op,logs_content,connection_id,session_id,error="peer not responding"):
    
    flag = False

    # UTC 2022-07-05 05:20:25 11[IKE] <peer_95.43.229.201_02b7-7f855c54-bdb6-49cc-baf9-dffb1d837851_0x0|943> 
    date_connection_session_regex = 'UTC \d{4}-[01]\d-[0-3]\d [012]\d:[0-5]\d:[0-5]\d \d\d\[.+\] <peer\_.+\_'+connection_id+'\_.+\|'+session_id+'>'
    
    # UTC 2022-07-05 05:20:25 11[IKE] <peer_95.43.229.201_02b7-7f855c54-bdb6-49cc-baf9-dffb1d837851_0x0|943> peer not responding, trying again (3/3) 
    error_regex = date_connection_session_regex+' '+error+'\, trying again \(3\/3\)'
    
    # UTC 2022-07-05 05:20:25 11[IKE] <peer_95.43.229.201_02b7-7f855c54-bdb6-49cc-baf9-dffb1d837851_0x0|943> initiating Main Mode IKE_SA peer_95.43.229.201_02b7-7f855c54-bdb6-49cc-baf9-dffb1d837851_0x0[943] to 95.43.229.201 
    main_mode_regex = date_connection_session_regex+' initiating Main Mode .+'
    
    # UTC 2022-07-05 05:20:37 01[IKE] <peer_95.43.229.201_02b7-7f855c54-bdb6-49cc-baf9-dffb1d837851_0x0|943> IKE_SA peer_95.43.229.201_02b7-7f855c54-bdb6-49cc-baf9-dffb1d837851_0x0[943] state change: CONNECTING => DESTROYING
    destroy_regex = date_connection_session_regex + '.+state change: CONNECTING => DESTROYING'
    
    for line_no in range(len(logs_content)):
    
        if(bool(re.findall(error_regex,logs_content[line_no]))):
            # print(re.findall(error_regex,logs_content[line_no]))
            file_op.write(re.findall(error_regex,logs_content[line_no])[0]+"\n\n\n")
            flag=True

        if(bool(re.findall(main_mode_regex,logs_content[line_no])) and flag):
                
            while(True):
                
                # print(line_no+1 ,logs_content[line_no])
                file_op.write(logs_content[line_no])
                line_no+=1
                
                if(bool(re.findall(destroy_regex,logs_content[line_no]))):
                    # print(line_no+1 ,logs_content[line_no])
                    file_op.write(logs_content[line_no])
                    flag=False
                    return
 
 
def filter_error_logs_on_time(file_op,logs_content,connection_id,input_date,start_time,end_time,error="peer not responding"):
    
    # UTC 2022-07-05 05:20:25 11[IKE] <peer_95.43.229.201_02b7-7f855c54-bdb6-49cc-baf9-dffb1d837851_0x0|943> 
    date_connection_session_regex = 'UTC \d{4}-[01]\d-[0-3]\d [012]\d:[0-5]\d:[0-5]\d \d\d\[.+\] <peer\_.+\_'+connection_id+'\_.+\|.+>'
    
    # UTC 2022-07-05 05:20:37 01[IKE] <peer_95.43.229.201_02b7-7f855c54-bdb6-49cc-baf9-dffb1d837851_0x0|943> IKE_SA peer_95.43.229.201_02b7-7f855c54-bdb6-49cc-baf9-dffb1d837851_0x0[943] state change: CONNECTING => DESTROYING
    destroy_regex = date_connection_session_regex + '.+state change: CONNECTING => DESTROYING'
    
    # UTC 2022-07-05 05:20:01 09[CFG] received stroke: initiate 'peer_95.43.229.201_02b7-7f855c54-bdb6-49cc-baf9-dffb1d837851_0x0'
    initiate_regex = 'UTC \d{4}-[01]\d-[0-3]\d [012]\d:[0-5]\d:[0-5]\d \d\d\[.+\] received stroke: initiate \'peer\_.+\_'+connection_id+'\_.+\''
    
    flag=False
    freq = 0
    
    for line_no in range(len(logs_content)):
        date=datetime.strptime(logs_content[line_no].split(' ')[1], '%Y-%m-%d').date()
        time=datetime.strptime(logs_content[line_no].split(' ')[2], '%H:%M:%S').time()
        
        
        
        if(date==input_date and time>=start_time):
            session_id = ''
            while(date==input_date and time<=end_time):
                if(bool(re.findall(initiate_regex,logs_content[line_no]))):
                    flag=True
                    
                if(bool(re.findall(destroy_regex,logs_content[line_no])) and flag):
                    print(line_no+1)
                    # Extracting session id from <peer_95.43.229.201_02b7-7f855c54-bdb6-49cc-baf9-dffb1d837851_0x0|942>
                    session_id = logs_content[line_no].split(' ')[4].split('|')[1].replace('>','')
                    freq+=1
                    flag=False
                
                line_no+=1
                
                date=datetime.strptime(logs_content[line_no].split(' ')[1], '%Y-%m-%d').date()
                time=datetime.strptime(logs_content[line_no].split(' ')[2], '%H:%M:%S').time()
                
            filter_error_logs_on_session(file_op,logs_content,connection_id,session_id)
            file_op.write("\n\n The frequency of the 'peer not responding' error for "+connection_id+" in cycles of 3 : "+ str(freq))
            break
        
def filter_error_logs_on_date(file_op,logs_content,connection_id,input_date,error="peer not responding"):
    
    # UTC 2022-07-05 05:20:25 11[IKE] <peer_95.43.229.201_02b7-7f855c54-bdb6-49cc-baf9-dffb1d837851_0x0|943> 
    date_connection_session_regex = 'UTC \d{4}-[01]\d-[0-3]\d [012]\d:[0-5]\d:[0-5]\d \d\d\[.+\] <peer\_.+\_'+connection_id+'\_.+\|.+>'
    
    # UTC 2022-07-05 05:20:37 01[IKE] <peer_95.43.229.201_02b7-7f855c54-bdb6-49cc-baf9-dffb1d837851_0x0|943> IKE_SA peer_95.43.229.201_02b7-7f855c54-bdb6-49cc-baf9-dffb1d837851_0x0[943] state change: CONNECTING => DESTROYING
    destroy_regex = date_connection_session_regex + '.+state change: CONNECTING => DESTROYING'
    
    # UTC 2022-07-05 05:20:01 09[CFG] received stroke: initiate 'peer_95.43.229.201_02b7-7f855c54-bdb6-49cc-baf9-dffb1d837851_0x0'
    initiate_regex = 'UTC \d{4}-[01]\d-[0-3]\d [012]\d:[0-5]\d:[0-5]\d \d\d\[.+\] received stroke: initiate \'peer\_.+\_'+connection_id+'\_.+\''
    
    flag=False
    freq = 0
    
    for line_no in range(len(logs_content)):
        date=datetime.strptime(logs_content[line_no].split(' ')[1], '%Y-%m-%d').date()
 
        session_id = ''
        while(date==input_date and (line_no in range(len(logs_content)))):

            if(bool(re.findall(initiate_regex,logs_content[line_no]))):
                flag=True
                
            if(bool(re.findall(destroy_regex,logs_content[line_no])) and flag):
                print(line_no+1)
                # Extracting session id from <peer_95.43.229.201_02b7-7f855c54-bdb6-49cc-baf9-dffb1d837851_0x0|942>
                session_id = logs_content[line_no].split(' ')[4].split('|')[1].replace('>','')
                freq+=1
                flag=False
            
            line_no+=1
            
            if(line_no in range(len(logs_content))):
                date=datetime.strptime(logs_content[line_no].split(' ')[1], '%Y-%m-%d').date()
            else:
                break
        
        if(bool(freq)):    
            filter_error_logs_on_session(file_op,logs_content,connection_id,session_id)
            file_op.write("\n\n The frequency of the 'peer not responding' error for "+connection_id+" in cycles of 3 : "+ str(freq))
            break

                                

def main():

    file_inp = open('input_log.log','r')
    logs_content = file_inp.readlines()

    # json_file=open('template.json','r')
    # json_content=json.load(json_file)

    file_op = open('filter.txt','w')
    parser = argparse.ArgumentParser()
    parser.add_argument('function', help='Name of function to call')
    parser.add_argument('--connection_id', help='Session id', default='0')
    parser.add_argument('--session_id', help='Session id', default='0')
    parser.add_argument('--date', help='date', default='0')
    parser.add_argument('--start_time', help='start time', default='0')
    parser.add_argument('--end_time', help='end time', default='0')
    args = parser.parse_args()

    if args.function == 'session_id':
        filter_error_logs_on_session(file_op,logs_content,args.connection_id,args.session_id)

    elif args.function == 'date':
        inp_date = datetime.strptime(args.date,'%Y-%m-%d').date()
        filter_error_logs_on_date(file_op,logs_content,args.connection_id,inp_date)

    elif args.function == 'time_range':
        inp_date = datetime.strptime(args.date,'%Y-%m-%d').date()
        start_time = datetime.strptime(args.start_time,'%H:%M:%S').time()
        end_time = datetime.strptime(args.end_time,'%H:%M:%S').time()
        filter_error_logs_on_time(file_op,logs_content,args.connection_id,inp_date,start_time,end_time)

if __name__=='__main__':
    main()
