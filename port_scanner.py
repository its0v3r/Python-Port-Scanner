# TODO
# Printar as portas abertas por padrão
# Opção para printar portas fechadas
# Pegar os banners
# Usar regex para detectar o OS através dos banners
# Opções de scan personalizadas (portas 1-1024, 1-65565, as 10 mais comuns)
# 192.168.220.130

from socket import socket, AF_INET, SOCK_STREAM
from pyfiglet import Figlet
import subprocess
import time


class PortScanner:
    def __init__(self, target, ports):
        self.target = target
        self.ports = ports
        self.banner_list = []

    def tryGetOS(self):
        os = ""
        for banner in self.banner_list:
            if "Debian" in banner or "Ubuntu" in banner or "Linux" in banner:
                os = "Linux"
            elif "Windows" in banner:
                os = "Windows"
            else:
                os = "Could not detect"
        return os

    def scanPort(self, port):
        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(2)
        banner = ""
        try:
            s.connect((self.target, port))
            if port != 80:
                try:
                    banner = s.recv(1024).decode().strip()
                    self.banner_list.append(banner)
                except:
                    pass
            else:
                banner = subprocess.check_output([f"curl -IL {self.target}"], shell=True, stderr=subprocess.DEVNULL).decode().strip()
                self.banner_list.append(banner)
            print(f"{port}/tcp\t\topen")
            if banner != "":
                print(f"{banner}\n")
            s.close()
        except:
            pass

    def scan(self):
        print(f"Scanning host {self.target}")
        print("PORT\t\tSTATUS")

        initial_port = int(self.ports.split("-")[0])
        last_port = int(self.ports.split("-")[1])

        for port in range(initial_port, last_port):
            self.scanPort(port)
        print(f"The running OS is: {self.tryGetOS()}")


if __name__ == "__main__":
    f = Figlet(font='slant')
    print(f.renderText('portscanner'))

    ps = PortScanner(
        target="192.168.220.130",
        ports="1-500"
    )
    start = time.perf_counter()
    ps.scan()
    end = time.perf_counter()
    print(f"\nScanned {ps.ports.split('-')[1]} ports on host {ps.target} in: {round(end - start, 2)}s")
    # CAPYBARA
