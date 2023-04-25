import argparse
def main():
    

    parser = argparse.ArgumentParser()
    parser.add_argument('function', help='Name of function to call')
    parser.add_argument('--connection_id', help='Session id', default='0')
    parser.add_argument('--session_ID', help='Session id', default='0')
    parser.add_argument('--dates', help='date', default='0')
    parser.add_argument('--start_time', help='start time', default='0')
    parser.add_argument('--end_time', help='end time', default='0')
    args = parser.parse_args()
    print(args.dates,args.start_time,args.session_ID,args.end_time,args.connection_id)
    
if __name__=='__main__':
    main()
