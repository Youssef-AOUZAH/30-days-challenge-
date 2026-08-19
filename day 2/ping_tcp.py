import socket

nmap_top_100_tcp = [
    80, 23, 443, 21, 22, 25, 3389, 110, 445, 139, 143, 53, 135, 3306, 8080, 1723, 
    111, 995, 993, 5900, 1025, 587, 8888, 199, 1720, 465, 548, 113, 81, 6001, 10000, 
    514, 5060, 179, 1026, 2000, 8443, 8000, 32768, 554, 26, 1433, 49152, 2001, 515, 
    8008, 49154, 1027, 5666, 646, 5000, 5631, 631, 49153, 8081, 2049, 88, 79, 5800, 
    106, 2121, 1110, 49155, 6000, 513, 990, 5357, 427, 49156, 543, 544, 5101, 144, 
    7, 389, 8009, 3128, 444, 9999, 5009, 7070, 5190, 3000, 5432, 1900, 3986, 13, 
    1029, 9, 5051, 6646, 49157, 1028, 873, 1755, 2717, 4899, 9100, 119, 37
]

def tcp_scan_top(ip): #used to quickly scan for nmap's top100 ports only


    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    for port in nmap_top_100_tcp:
        result=client.connect_ex((ip,port))
        

        if result==0:
            print(f'port {port}\topen ')
        elif result==111:
            print(f'port {port}\tclosed')

def tcp_scan_one_port(ip,port):
    
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    result=client.connect_ex((ip,int(port)))
    
    if result==0:
        print(f'port {port}\topen')
    elif result==111:
        print(f'port {port}\tclosed')

