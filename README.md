# Domain-IP-Track

Monitor the changes of the IP address that a domain resolves to.

This can be used to monitor how ofter your Dynamic IP address is changing, when being used in correlation with a DDNS provider such as duckdns.org.

The default config checks every 5 mins, any changes are recorded into a text file.

## Usage

### Docker

1. Get the repository
   ```bash
   git clone https://github.com/andrewkliskey/domain-ip-track.git
   ```
1. Modify the `docker-compose.yml` file's environment variables
   ```yaml
   environment:
     # Enter Domains you wish to track, separated by commas
     - DOMAIN_LIST=www.example.com, example.com
     # Interval you wish to wait before re-checking domain
     - SLEEP=300
   ```
1. Run
   ```
   docker-compose up
   ```

### Manual Install Guide

Install prerequisites (Ubuntu/Debian):

```bash
sudo apt install python3 python3-pip
sudo pip3-install dnspython
```

Download Python Script then edit domain :

```bash
wget https://raw.githubusercontent.com/andrewkliskey/ddns-ip-track/master/ddns-ip-track.py
sudo nano ddns-ip-track.py
```

Run:

```bash
python3 ddns-ip-track.py
```

Terminal view:

![Terminal Screenshot](https://raw.githubusercontent.com/andrewkliskey/ddns-ip-track/master/screenshots/terminal.png)

Output File:

![Output Screenshot](https://raw.githubusercontent.com/andrewkliskey/ddns-ip-track/master/screenshots/output-file.png)
