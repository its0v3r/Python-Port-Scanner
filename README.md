# Python Port Scanner

## What is this script?

This is a simple Python Port Scanner that tries to detect open ports from a host in the same network, the banners from each open port and the current OS that the host is running.

## How to use the script?

- First, to scan a target, the user needs to pass a valid IPv4 with the -t --target option;
- If the user doesn't pass a target, the script will scan open ports on the localhost (127.0.0.1);
- The user can provide the port range that should be scanned with the option -p --ports and passing the inital port and the last port (e.g.: 1-1023);
- If the option -p --ports in not provided, then the script will scan all 65535 ports;
- There are 3 preconfigured scan modes, that the user can use by passing a value from 0 to 2 with the option -m --mode:
  - Mode 0 will scan only the privileged ports (1-1023);
  - Mode 1 will scan only the top 10 most common ports to be open (20, 21, 22, 23, 25, 53, 80, 110, 119, 443);
  - Mode 2 will scan only the 80 and 443;
- This code is meant to work with Python3.

Example 1 - Specifing the host target IPv4 address and scanning all 65535 ports:

```
python3 port_scanner.py -t 192.168.0.53
```

Example 2 - Specifing the host target IPv4 address and scanning only ports 1 to 100:

```
python3 port_scanner.py -t 192.168.0.53 -p 1-100
```

Example 3 - Scanning the localhost ports 80 and 443:

```
python3 port_scanner.py -m 2
```
