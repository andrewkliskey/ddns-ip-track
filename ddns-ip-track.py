#!/usr/bin/env python
import dns.resolver
from datetime import datetime
import time
from os import environ
import os.path

# SETUP #
if environ.get('DOMAIN_LIST') is not None:
    domains = environ['DOMAIN_LIST'].split(',')
    domains = [i.strip(' ') for i in domains]
else:
    domains = ['example.com']  # change domains here if using without docker

default_sleep = 300  # 5 mins # change sleep here if using without docker
try:
    sleep = int(environ['SLEEP'])
except:
    sleep = default_sleep

directory = "logs"
if not os.path.exists(directory):
    os.makedirs(directory)

current_ip = {}
for domain in domains:
    current_ip[domain] = 0

my_resolver = dns.resolver.Resolver(configure=False)
my_resolver.nameservers = [
    '1.1.1.1',
    '1.0.0.1'
]

# SETUP #


def check_new_ip(domain, current_ip):
    now = datetime.now()
    result = my_resolver.resolve(domain, 'A')
    for ip_val in result:
        print(ip_val.to_text())

    # If IP has changed this is run
    if ip_val.to_text() != current_ip:
        # Print the new IP
        print("New IP:", ip_val.to_text())

        # Gets current date + time
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        filename = ("./logs/" + domain + ".txt")
        # Appends new IP with Date and Time to text file
        open(filename, "a+").write(ip_val.to_text() + "  " + dt_string + "\n")
        current_ip = (ip_val.to_text())
    else:
        print("No IP change")
    return current_ip


while __name__ == "__main__":
    for domain in domains:
        current_ip[domain] = check_new_ip(domain, current_ip[domain])
    time.sleep(sleep)
