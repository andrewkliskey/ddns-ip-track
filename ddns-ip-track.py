#!/usr/bin/env python
import dns.resolver
from datetime import datetime
import time
domain='example.com'
check=300 #5mins
current_ip=0

def check_new_ip(domain, current_ip):
    now = datetime.now()
    result = dns.resolver.resolve(domain, 'A')
    for ipval in result:
        print(ipval.to_text())

    #If IP has changed this is run 
    if ipval.to_text() != current_ip:
        #Print the new IP
        print ("New IP:", ipval.to_text())

        #Gets current date + time
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        filename=(domain+"-list.txt")
        #Appends new IP awith Date and Time to text file
        open(filename,"a").write(ipval.to_text()+ "  " + dt_string + "\n")
        current_ip=(ipval.to_text())
    else:
        print("No IP change")
    return current_ip
        

i=0
while i==0:
    current_ip = check_new_ip(domain, current_ip)
    time.sleep(check)