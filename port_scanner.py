# TODO
# Printar as portas abertas por padrão
# Opção para printar portas fechadas
# Pegar os banners
# Usar regex para detectar o OS através dos banners
# Opções de scan personalizadas (portas 1-1024, 1-65565, as 10 mais comuns)
# 192.168.220.130

from socket import *
from pyfiglet import Figlet
import prettytable
import subprocess
import time
import argparse


class PortScanner:
    def __init__(self, target):
        self.target = target

    def scanPort(self, port):
        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(2)
        try:
            s.connect((self.target, port))
            print(f"{port}/tcp\topen")
            s.close()
        except:
            pass

    def scan(self):
        print(f"Scanning host {self.target}")
        print("PORT\tSTATUS")
        for port in range(1, 1024):
            self.scanPort(port)


if __name__ == "__main__":
    f = Figlet(font='slant')
    print(f.renderText('Port Scanner'))

    ps = PortScanner(
        target="192.168.220.130"
    )
    start = time.perf_counter()
    ps.scan()
    end = time.perf_counter()
    print(f"\nScanned 1024 ports in: {round(end - start, 2)}s")
    # CAPYBARA
