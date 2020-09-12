"""
Proxy design pattern
A type of structural design pattern...
"""

from abc import ABCMeta, abstractmethod


class AbstractCmd(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, command):
        pass

class RealCmd(AbstractCmd):
    def execute(self, command):
        print(f"{command} command executed !!")

class ProxyCmd(AbstractCmd):
    def __init__(self, user) -> None:
        self.is_authorized = False
        if user == "admin":
            self.is_authorized = True
        self.executor = RealCmd()
        self.restricted_commands = ["rm", "mv"]

    def execute(self, command):
        if self.is_authorized:
            self.executor.execute(command)
        else:
            if any([command.strip().startswith(cmd)
                    for cmd in self.restricted_commands]):
                raise Exception(f"{command} command is not allowed for non-admin users")
            else:
                self.executor.execute(command)

admin_executor = ProxyCmd("admin")
other_executor = ProxyCmd("other")

admin_executor.execute("apt update")
admin_executor.execute("rm")

other_executor.execute("apt update")
other_executor.execute("rm")
