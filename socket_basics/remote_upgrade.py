from contextlib import closing
from subprocess import check_call
from socket import socket, AF_INET, SOCK_STREAM

HOSTNAME = 'themrinalsinha.com'
USER     = 'mrinal'
PORT     = 22

with closing(socket(AF_INET, SOCK_STREAM)) as sock:
    sock.settimeout(2)
    if sock.connect_ex((HOSTNAME, PORT)) != 0:
        print("Error connecting host")
    else:
        check_call(
            f"ssh {USER}@{HOSTNAME} apt-get update && apt-get upgrade -y",
            shell=True
        )
