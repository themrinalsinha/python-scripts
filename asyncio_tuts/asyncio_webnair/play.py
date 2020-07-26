# MUST READ: https://youtu.be/ZzfHjytDceU
from types import coroutine

@coroutine
def read_wait(sock):
    yield "read_wait", sock

@coroutine
def write_wait(sock):
    yield "write_wait", sock

class Loop(object):
    async def sock_recv(self, sock, maxbytes):
        await read_wait(sock)
        return sock.recv(maxbytes)

