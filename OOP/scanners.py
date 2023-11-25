import nmap

nm = nmap.PortScanner()
# print(nm.scan('192.168.0.1','1-1000' ))

print(nm.scan('127.0.0.1', '22-443'))
print(nm.scaninfo())
print(nm.all_hosts())


print(nm['127.0.0.1'].hostname() )
print( nm['127.0.0.1'].hostnames() )

print( nm['127.0.0.1'].state())

print(nm['127.0.0.1'].all_protocols())

