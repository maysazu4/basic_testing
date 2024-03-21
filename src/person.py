class Person:
    def __init__(self,tickets=0):
        self.tickets = tickets
    def add_ticket(self):
        self.tickets += 1