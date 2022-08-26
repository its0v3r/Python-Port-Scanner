# TODO
# Printar as portas abertas por padrão
# Opção para printar portas fechadas
# Pegar os banners
# Usar regex para detectar o OS através dos banners
# Opções de scan personalizadas (portas 1-1024, 1-65565, as 10 mais comuns)
# 192.168.220.130

from socket import *
import subprocess
import time
import argparse


class PortScanner:
    def __init__(self, target):
        self.target = target

    def tryGetBanner(self):
        print()

    def scanPort(self, port):
        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(2)
        try:
            s.connect((self.target, port))
            print(f"Open port {port}")
            s.close()
        except Exception as e:
            pass

    def scan(self):
        for port in range(1, 1024):
            self.scanPort(port)


if __name__ == "__main__":
    ps = PortScanner(
        target="192.168.220.130"
    )
    ps.scan()
