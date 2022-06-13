"""
Strategy Design Pattern
-----------------------

In programming, the strategy pattern is a design pattern that enables an algorithm's behavior to be
changed at runtime. Instead of implementing a single algorithm directly, code receives run-time
instructions as to which in a family of algorithms to use.

"""

import string, random

def generate_id(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))

class SupportTicket:
    id: str
    customer: str
    issue: str

    def __init__(self, customer, issue) -> None:
        self.id = generate_id()
        self.customer = customer
        self.issue = issue

class Strategy:
    FIFO = 'FIFO'
    LIFO = 'LIFO'
    RAND = 'RAND'


class CustomerSupport:
    tickets: list[SupportTicket] = []

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self, processing_strategy: str = Strategy.FIFO):
        if len(self.tickets) == 0:
            print('No tickets to process')
            return

        if processing_strategy == Strategy.FIFO:
            for t in self.tickets:
                self.process_ticket(t)

        elif processing_strategy == Strategy.LIFO:
            for t in reversed(self.tickets):
                self.process_ticket(t)

        elif processing_strategy == Strategy.RAND:
            list_copy = self.tickets.copy()
            random.shuffle(list_copy)

            for t in list_copy:
                self.process_ticket(t)

    def process_ticket(self, ticket: SupportTicket):
        print(
            "=========================================\n"
            f"Processing ticket id : {ticket.id}\n"
            f"Customer             : {ticket.customer}\n"
            f"Issue                : {ticket.issue}\n"
            "=========================================\n"
        )

app = CustomerSupport()
app.create_ticket('John', 'Laptop not working')
app.create_ticket('Jane', 'Mobile not working')
app.create_ticket('Jack', 'Life sucks, nothing is working ')
app.process_tickets()

"""
In the above example, the problem lies in the if...else statement of the process_tickets() method.
If we come up with more than one strategy, we need to change the if...else statement etc. Now,
strategy pattern is a way to solve this problem.
"""
# ===============================================================================================
print("= " * 50)

from abc import ABC, abstractmethod

class TicketOrderingStrategy(ABC):

    @abstractmethod
    def create_ordering(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        pass

class FIFO_OrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        return tickets

class LIFO_OrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        return reversed(tickets)

class RAND_OrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        list_copy = tickets.copy()
        random.shuffle(list_copy)
        return list_copy

class CustomerSupport:
    tickets: list[SupportTicket] = []

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self, processing_strategy: TicketOrderingStrategy):
        if len(self.tickets) == 0:
            print('No tickets to process')
            return

        # create the ordered list
        ticket_list = processing_strategy.create_ordering(self.tickets)
        for t in ticket_list:
            self.process_ticket(t)

    def process_ticket(self, ticket: SupportTicket):
        print(
            "=========================================\n"
            f"Processing ticket id : {ticket.id}\n"
            f"Customer             : {ticket.customer}\n"
            f"Issue                : {ticket.issue}\n"
            "=========================================\n"
        )

app = CustomerSupport()
app.create_ticket('John', 'Laptop not working')
app.create_ticket('Jane', 'Mobile not working')
app.create_ticket('Jack', 'Life sucks, nothing is working ')
app.process_tickets(processing_strategy=FIFO_OrderingStrategy())
print('- ' * 50)
app.process_tickets(processing_strategy=LIFO_OrderingStrategy())
print('- ' * 50)
app.process_tickets(processing_strategy=RAND_OrderingStrategy())
print('- ' * 50)
