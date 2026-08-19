import ping_tcp
import argparse
def scanner(args):
    if args.port is not None:
        if 'F' in args.port:
            ping_tcp.tcp_scan_top(args.ip)
        else:
            for i in range(len(args.port)):
                ping_tcp.tcp_scan_one_port(args.ip,args.port[i])
def main():
    print("Scan starting...")
    parser=argparse.ArgumentParser()
    parser.add_argument("ip",help="The target device ip")
    parser.add_argument("-p","--port",required=True,nargs='+',choices=[str(i) for i in range(1,65536)]+['F'],help="ports to scan")
    args=parser.parse_args()

    if args.ip is not None:
        scanner(args)
    print("Scan ended")








if __name__=='__main__':
    main()