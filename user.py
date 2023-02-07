from bankAccount import BankAccount
import uuid
import logging
from ticket import *


class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password
        self.account = BankAccount(title="Main_Account", balance = 10)
        self.ticket_list = []
        self.__id = uuid.uuid1()

        logging.basicConfig(filename='user_instances.log', level=logging.INFO,
        format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
        logging.info('User instance created: name=%s, id=%r', self.username, self.__id)

    @property
    def id(self):
        return self.__id

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, newpass):
        self.validate_password(newpass)
        self.__password = newpass

    def reset_password(self):
        npass = self.security()
        if npass:
            self._password = npass

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self

    def display_account_info(self):
        self.account.display_account_info(self.username)
        return self

    def buy_ticket(self, ticket):
        self.ticket_list.append(ticket)


    def make_trip(self, location):
        pass

    def use_ticket_bynumber(self, ticket):
        self.ticket_list[ticket - 1].use_ticket()
        self.ticket_validation(self.ticket_list[ticket - 1])

    def use_ticket_byid(self, ticket_id):
        for ticket in self.ticket_list:
            print(ticket)
            if ticket_id == str(ticket.ticket_id):
                ticket.use_ticket()
                self.ticket_validation(ticket)

    def charge_chargeble_ticket(self, number, amount):
        self.ticket_list[number - 1].charge_ticket(amount)


    def ticket_validation(self, ticket):
        if ticket.check_expiration():
            self.ticket_list.remove(ticket)

    def show_ticket_list(self):
        for ticket in (self.ticket_list):
            yield ticket

    def show_account_information(self):
        return f"""
                    username:{self.username}
                    user_id:{self.__id}
                    """


