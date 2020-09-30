"""
Assume that we want to create an operating system using a multi-server approach,
A multi-server operating system has a minimal kernel, called the microkernel, that
runs in privileged mode. All the other services of the system are following a server
architecture (driver server, process server, file server, and so forth). Each server
belongs to a different memory address space and runs on top of the microkernel in
user mode. The pros of this approach are that the operating system can become more
fault-tolerant, reliable, and secure. For example, since all drivers are running in
user mode on a driver server, a bug in a driver cannot crash the whole system, and
neither can it affect the other servers. The cons of this approach are the performance
overhead and the complexity of system programming, because the communication between
a server and the microkernel, as well as between the independent servers, happens
using message passing. Message passing is more complex than the shared memory model
used in monolithic kernels like Linux.

We begin with a Server interface. An Enum parameter describes the different possible
states of a server. We use the abc module to forbid direct instantiation of the Server
interface and make the fundamental boot() and kill() methods mandatory, assuming that
different actions are needed to be taken for booting, killing, and restarting each server.
If you have not used the abc module before, note the following important things.

- We need to subclass ABCMeta, using metaclass keyword
- We use the `@abstractmethod` decorator for stating which methods should be
  implemented (mandatory) by all subclasses of Server.
"""

from abc  import ABCMeta, abstractmethod
from enum import Enum

class User:
    pass
class Process:
    pass
class File:
    pass

State = Enum("State", "new running sleeping restart zombie")

class Server(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return self.name

    @abstractmethod
    def boot(self):
        pass

    @abstractmethod
    def kill(self, restart=True):
        pass

"""
A modular operating system can have a great number of interesting servers: a file
server, a process server, an authentication server, a network server, a graphical/
window server, and so forth. The following example includes two stub servers-
the FileServer , and the ProcessServer. Apart from the methods required to be
implemented by the Server interface, each server can have its own specific methods.
For instance the FileServer has a create_file() method for creating files, and the
ProcessServer has a create_process() method for creating processes.
"""
class FileServer(Server):
    def __init__(self) -> None:
        """actions required for initiating the file server"""
        self.name = 'FileServer'
        self.state = State.new

    def boot(self):
        print(f'booting the {self}')
        """actions required for booting the file server"""
        self.state = State.running

    def kill(self, restart=True):
        print(f"Killing {self}")
        """actions required for killing the file server"""
        self.state = State.restart if restart else State.zombie

    def create_file(self, user, name, permissions):
        """Check validity of permissions, user rights etc.."""
        print(f"trying to create the file '{name}' for user '{user}' with permissions {permissions}")


class ProcessServer(Server):
    def __init__(self) -> None:
        """actions required for initiating the process server"""
        self.name  = "ProcessServer"
        self.state = State.new

    def boot(self):
        print(f"booting the {self}")
        """ actions required for booting the process server """
        self.state = State.running

    def kill(self, restart=True):
        print(f"Killing {self}")
        self.state = State.restart if restart else State.zombie

    def create_process(self, user, name):
        """ check user rights, generated PID, etc. """
        print(f"trying to create the process '{name}' for user '{user}'")

"""
The OperatingSystem class is a Facade. In __init__() , all the necessary server
instances are created. The start() method, used by the client code, is the entry point
to the system. More wrapper methods can be added, if necessary, as access point
to the services of the servers such as the wrappers create_file() and create_
process() . From the client's point of view, all those services are provided by the
OperatingSystem class. The client should not be confused with unnecessary details
such as the existence of servers and the responsibility of each server.
"""
class OperatingSystem:
    """ The Facade """
    def __init__(self) -> None:
        self.fs = FileServer()
        self.ps = ProcessServer()

    def start(self):
        [i.boot() for i in (self.fs, self.ps)]

    def create_file(self, user, name, permissions):
        return self.fs.create_file(user, name, permissions)

    def create_process(self, user, name):
        return self.ps.create_process(user, name)

os = OperatingSystem()
os.start()
os.create_file('foo', 'hello', '-rw-r-r')
os.create_process('bar', 'ls /tmp')


"""
The Facade OperatingSystem class does a good job. The client code can create files
and processes without needing to know internal details about the operating system,
such as the existence of multiple servers. To be precise, the client code can call the
methods for creating files and processes, but they are currently dummy. As an
interesting exercise, you can implement one of the two methods, or even both.
"""
