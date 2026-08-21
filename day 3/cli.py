import dns_resolver
import argparse
from concurrent.futures import ThreadPoolExecutor
import wrap_json


path=''
def resolve_threads(listTarget,function):
    
    with ThreadPoolExecutor(max_workers=20) as executor:
            output=list(executor.map(function ,listTarget))
    wrap_json.wrap_json(output,path)

def resolve_queries_threads(listTarget,listQueries,function):
    
    with ThreadPoolExecutor(max_workers=20) as executor:
            output=list(executor.map(function,listTarget,listQueries))
    wrap_json.wrap_json(output,path)



def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--host",type=str,nargs='*',help='The host name,could input more than one')
    parser.add_argument("--ip",type=str,nargs='*',help='The ip address,could input more than one')
    parser.add_argument("--path",required=True,type=str,nargs=1,help='Output path for the json file containing results,which contains the name of the json file')
    parser.add_argument("--query",type=str,nargs='*',help="The dns query, 'A' 'AAAA',...")
    args=parser.parse_args()

    global path
    path=args.path[0]
    if args.query is None:
        if args.host is not None:
            resolve_threads(args.host,dns_resolver.dnsLook)
        elif args.ip is not None:
            resolve_threads(args.ip,dns_resolver.reverseDnsLook)
    
    else:
        if args.host is not None:
            resolve_queries_threads(args.host,args.query,dns_resolver.dnsQuery)
        if args.ip is not None:
            resolve_queries_threads(args.ip,args.query,dns_resolver.dnsQuery)
        




            
    




if __name__=='__main__':
    main()



