import dns.resolver
import socket
def getAttr(attribute):
    return f"[dnsResolve[i].{attribute} for i in range(len(dnsResolve))]"
def dnsQuery(hostName,query):#hostname could be an ip also
    attributes=['mname', 'rname', 'serial', 'refresh', 'retry', 'expire', 'minimum']
    

    try:
        dnsResolve=dns.resolver.resolve(hostName,query)

        if query=='A':
            
            return [dnsResolve[i].address for i in range(len(dnsResolve))]
        elif query=='AAAA':
            
            return [dnsResolve[i].address for i in range(len(dnsResolve))]
        
        elif query=='CNAME':
            return [dnsResolve[i].target for i in range(len(dnsResolve))]
        elif query=='MX':
            return [dnsResolve[i].address for i in range(len(dnsResolve))]
        elif query=='TXT':
            return [[dnsResolve[i].preference for i in range(len(dnsResolve))],[dnsResolve[i].exchange for i in range(len(dnsResolve))]]
        elif query=='NS':
            return [dnsResolve[i].target for i in range(len(dnsResolve))]
        elif query=='SOA':
            return [[eval(getAttr(attribute.uppercase))] for attribute in attributes]
        else:
            print('query not supported')
    except:
        print("error on query execution,try a different ip or hostname")
def dnsLook(hostname):
    return socket.gethostbyname(hostname)
def reverseDnsLook(ip):
    return socket.gethostbyaddr(ip)