# TODO
# Printar as portas abertas por padrão
# Opção para printar portas fechadas
# Pegar os banners
# Usar regex para detectar o OS através dos banners
# Opções de scan personalizadas (portas 1-1024, 1-65565, as 10 mais comuns)
# 192.168.220.130

from socket import *
import time
import argparse


class PortScanner:
    def __init__(self, target):
        self.target = target

    def scanPort(self, port):
        socket_obj = socket(AF_INET, SOCK_STREAM)
        socket_obj.settimeout(1)
        result = socket_obj.connect_ex((self.target, port))
        if (result == 0):
            try:
                banner = socket_obj.recv(1024).decode()
                print(f"Port {port}")
                print("Status: open")
                print("Banner:")
            except Exception as e:
                print(e)
                pass
        socket_obj.close()

    def scan(self):
        for port in range(1, 1024):
            self.scanPort(port)


if __name__ == "__main__":
    ps = PortScanner(
        target="192.168.220.130"
    )
    ps.scan()
