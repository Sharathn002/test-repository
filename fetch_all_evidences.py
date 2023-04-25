import argparse
import time

if __name__ == "__main__":  
    start = time.perf_counter()
    parser = argparse.ArgumentParser()
    parser.add_argument("service_type", help="type of the service either s2s or c2s")  
    parser.add_argument("id",help="id of the gateway or vpn server as per the service")
    parser.add_argument("env",help="environment refers to either stage or prod")
    args = parser.parse_args()
    print("this is the output",args.service_type,args.id,args.env)
    print(args.service_type,args.id,args.env," thank you")
