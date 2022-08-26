from socket import socket, AF_INET, SOCK_STREAM
import scapy
from pyfiglet import Figlet
import subprocess
import argparse
import time


class PortScanner:
    def __init__(self, target, ports, timeout, scan_mode):
        self.target = target
        self.ports = ports
        self.timeout = timeout
        self.scan_mode = scan_mode
        self.banner_list = []

    def tryGetOS(self):
        linux_system_list = ["debian", "ubuntu", "linux"]
        windows_system_list = ["microsft", "windows"]

        for banner in self.banner_list:
            banner = str(banner).lower()
            for os in linux_system_list:
                if os in banner:
                    return "Linux"
            for os in windows_system_list:
                if os in banner:
                    return "Windows"

    def scanPort(self, port):
        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(2)
        banner = ""

        try:
            s.connect((self.target, port))
            if port == 80 or port == 443:
                banner = subprocess.check_output([f"curl -IL {self.target}"], shell=True, stderr=subprocess.DEVNULL).decode().rstrip()
                self.banner_list.append(banner)
            else:
                try:
                    banner = s.recv(1024).decode().strip()
                    self.banner_list.append(banner)
                except:
                    pass

            port = f"{port}/tcp".ljust(26)
            print(f"{port}open")

            if banner != "":
                print(f"{banner}\n")
            s.close()

        except:
            pass

    def scan(self):
        print(f"Scanning host {self.target}\n")
        print(f"PORT".ljust(26) + "STATUS")

        if (isinstance(args.ports, str)):
            initial_port = int(self.ports.split("-")[0])
            last_port = int(self.ports.split("-")[1])
            self.ports = list(range(initial_port, last_port + 1))

        for port in self.ports:
            self.scanPort(port)

        os = self.tryGetOS()
        print(f"\n{'Could not detect OS' if not os else f'The host current OS is: {os}'}")


def getArguments():
    parser = argparse.ArgumentParser(description="PYTHON PORT SCANNER - Script to scan for open ports on a host")
    parser.add_argument("-t", "--target", action="store", help="The target host IPv4 address. If you don't provide a target, it will scan the localhost")
    parser.add_argument("-p", "--ports", action="store", help="The port or the port range that will be scanned (1-65535). If this field is not provided, the script will scan all 65535 ports")
    parser.add_argument("-m", "--mode", action="store", help="The pre configured scan mode that will be executed. Use 0 to scan only the privileged ports (1-1023), 1 to scan only the top 10 most common ports to be open, and 2 to scan only HTTP and HTTPS ports (80 and 443)")
    parser.add_argument("--timeout", action="store", help="The max timeout value for getting an response from each scanned port. Default value is 2")
    args = parser.parse_args()

    if not args.target:
        print("No target host IPv4 address, scanning localhost")
        args.target = "127.0.0.1"

    if not args.ports and not args.mode:
        args.ports = "1-65535"

    if not args.timeout:
        args.timeout = 2

    if args.mode:
        if args.ports:
            print(f"You set a port range with -p and a scan mode with -m. The script will run the scan based on the scan mode selected which is {args.mode}")
        if args.mode == "0":
            args.ports = "1-1023"
        elif args.mode == "1":
            args.ports = [20, 21, 22, 23, 25, 53, 80, 110, 119, 443]
        elif args.mode == "2":
            args.ports = [80, 443]
        else:
            print(f"Invalid scan mode inserted, quitting...")
            quit()

    return args


if __name__ == "__main__":
    f = Figlet(font='slant')
    print(f.renderText('portscanner'))

    args = getArguments()
    ps = PortScanner(
        target=args.target,
        ports=args.ports,
        timeout=args.timeout,
        scan_mode=args.mode
    )

    start = time.perf_counter()
    ps.scan()
    end = time.perf_counter()

    print(f"\nScanned {len(ps.ports)} ports on host {ps.target} in: {round(end - start, 2)}s")
