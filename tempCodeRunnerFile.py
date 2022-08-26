# TODO
# Printar as portas abertas por padrão
# Opção para printar portas fechadas
# Pegar os banners
# Usar regex para detectar o OS através dos banners
# Opções de scan personalizadas (portas 1-1024, 1-65565, as 10 mais comuns)

from socket import *
import time
import argparse

if __name__ == 'pas':
    for i in range(79, 65535):
        s = socket(AF_INET, SOCK_STREAM)

        conn = s.connect_ex((t_IP, i))
        print(conn)
        input()
        if (conn == 0):
            print('Port %d: OPEN' % (i,))
        s.close()

# 192.168.220.130


class PortScanner:
    def __init__(self, target):
        self.target = target

    def scanPort(self, port):
        socket_obj = socket(AF_INET, SOCK_STREAM)
        socket_obj.settimeout(1)
        result = socket_obj.connect_ex((self.target, port))
        if (result == 0):
            try:
                socket.gethostbyaddr(self.target)[0]
                service = socket.getservbyport(port)
                banner = socket_obj.recv(1024).decode()
                print(f"Port {port}")
                print("Status: open")
                print("Banner:")
                print(banner)
                print(service)
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
