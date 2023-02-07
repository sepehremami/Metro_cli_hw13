import datetime

class SubwayTicket:
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self, cost_per_trip, bank_balance):
        if self.balance < cost_per_trip:
            print("Insufficient balance.")
            return False
        if bank_balance < 1000:
            print("Insufficient balance in bank account.")
            return False
        self.balance -= cost_per_trip
        return True

    def disposable_ticket(self, cost_per_trip):
        if not self.check_balance(cost_per_trip):
            return

        expiry_date = datetime.datetime.now()
        if expiry_date < datetime.datetime.now():
            print("Ticket expired (disposed after last trip).")
            return

    def expirable_ticket(self, cost_per_trip, bank_balance):
        if not self.check_balance(cost_per_trip, bank_balance):
            return
            
        self.expiry_date = datetime.datetime.now() + datetime.timedelta(days=365)
        if self.balance < cost_per_trip or self.expiry_date < datetime.datetime.now():
            print("Ticket expired.")
            return
            
    def chargable_ticket(self, cost_per_trip, bank_balance):
        if not self.check_balance(cost_per_trip, bank_balance):
            return
            
        if self.balance < cost_per_trip:
            print("Ticket expired (insufficient balance).")
            return


class SubwayAdmin:
    def __init__(self):
        self.tickets = []
        self.banned_tickets = [] 

    def create_ticket(self, balance, ticket_type):
        ticket = SubwayTicket(balance)
        ticket.ticket_type = ticket_type
        self.tickets.append(ticket)
        return ticket
        
    def check_ticket_status(self, ticket):
        if ticket.expiry_date:
            if ticket.expiry_date < datetime.datetime.now():
                print("Ticket expired.")
                return
            print("Ticket valid until", ticket.expiry_date)
        else:
            if ticket.balance < ticket.cost_per_trip:
                print("Ticket expired (insufficient balance).")
                return
            print("Ticket valid.")
            
    def delete_ticket(self, ticket):
        if ticket in self.tickets:
            self.tickets.remove(ticket)

    def ban_ticket(self, ticket):
        if ticket in self.tickets:
            self.tickets.remove(ticket)
            self.banned_tickets.append(ticket)
            print("Ticket banned.")
