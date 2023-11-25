import nmap

nm = nmap.PortScanner()
print(nm.scan('127.0.0.1','20-443'))

print(nm['127.0.0.1'].hostname())
print(nm['127.0.0.1'].hostnames())
print(nm['127.0.0.1'].state())