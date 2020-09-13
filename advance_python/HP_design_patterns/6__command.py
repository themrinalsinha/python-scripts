"""
Command Design Pattern -- This is behavioral design pattern
"""
from abc import ABC, abstractmethod


class BaseCommand(ABC):
    """ base command class """

    @abstractmethod
    def execute(self):
        raise NotImplementedError("Please implement the subclass")


class EmailCommand(BaseCommand):
    """ email command class """

    def __init__(self, receiver, data) -> None:
        self.receiver = receiver
        self.data     = data

    def execute(self):
        self.receiver.send_email(self.data)


class SMSCommand(object):
    """ SMS command class """

    def __init__(self, receiver, data) -> None:
        self.receiver = receiver
        self.data     = data

    def execute(self):
        self.receiver.send_sms(self.data)


class NotificationService(object):
    """ Receiver class """
    def send_email(self, data):
        print(f"Sending email: {data}")

    def send_sms(self, data):
        print(f"Sending SMS: {data}")


class NotificationInvoker(object):
    """ Invoker class """

    def __init__(self) -> None:
        self.notification_history = []

    def invoke(self, command):
        self.notification_history.append(command)
        command.execute()


if __name__ == "__main__":
    invoker  = NotificationInvoker()
    receiver = NotificationService()
    invoker.invoke(EmailCommand(receiver, {"subject": "Test Email"}))
    invoker.invoke(SMSCommand(receiver, {"subject": "Test SMS"}))
    print(invoker.notification_history)
