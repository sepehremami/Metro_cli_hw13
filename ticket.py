import uuid
import datetime
import pickle
from abc import ABC, abstractmethod
from dateutil.relativedelta import relativedelta
import json
import os

# pip install python-dateutil

buy_ticket_menu = {
	'1' : 'Chargeble',
	'2' : 'Disposable(you can use it only once)',
	'3' : 'Date Expirable'}


def pickle_tickets(ticket_obj):
	with open(f"tickets/{ticket_obj.ticket_id}.ticket.pickle" , 'wb') as ticket:
		pickle.dump(ticket_obj, ticket)

class Ticket(ABC):
	trip_fee = 10
	def __init__(self):
		self.creation_date = datetime.datetime.now()
		self.ticket_id = uuid.uuid1()
		self.expire = False


	@abstractmethod
	def use_ticket(self):
		pass

	@abstractmethod
	def _update(self):
		pass

	@abstractmethod
	def	_delete_ticket(self):
		pass

	def check_expiration(self):
		pass

	@abstractmethod
	def expire(self):
		pass

	@abstractmethod
	def __repr__(self):
		pass

class ExpirableTicket(Ticket):
	ticket_raw_price = 5
	ticket_constant_charge = 50
	def __init__(self):
		super().__init__()
		self.expiration_date = self.creation_date + relativedelta(years=1)
		self.balance = self.__class__.ticket_constant_charge

	def use_ticket(self):
		if not self.check_expiration():
			assert self.balance >= self.__class__.trip_fee, ValueError('Not Enough ticket credit')
			self.balance = self.balance - self.__class__.trip_fee
		self.check_expiration()
		self._update

	def check_expiration(self):
		if datetime.datetime.now() >= self.expiration_date:
			self.__delete_ticket()
			return True
		if self.balance == 0:
			self.__delete_ticket()
			return True
		return False

	def _delete_ticket(self):
		file_path = f"tickets/{self.ticket_id}.pickle"
		if os.path.isfile(file_path):
			os.remove(file_path)
			return "File has been deleted"
		else:
			return "File does not exist"

	def expire(self):
		pass

	def _update(self):
		with open(f"tickets/{self.ticket_id}.ticket.pickle" , 'wb') as ticket:
			pickle.dump(self, ticket)

	def __repr__(self):
		return f'\tType: Expirable Ticket\n\tTicket ID: {self.ticket_id}\n\tExpiration Date: {self.expiration_date}\n\tCredit: {self.balance}'


class ChargebleTicket(Ticket):
	def __init__(self):
		super().__init__()
		self.balance = 50


	def charge_ticket(self, amount):
		self.balance += amount

	def use_ticket(self):
		pass

	def _update(self):
		with open(f"tickets/{self.ticket_id}.ticket.pickle" , 'wb') as ticket:
			pickle.dump(self, ticket)

	def _delete_ticket(self):
		file_path = f"tickets/{self.ticket_id}.pickle"
		if os.path.isfile(file_path):
			os.remove(file_path)
			return "File has been deleted"
		else:
			return "File does not exist"

	def expire(self):
		pass

	def __repr__(self):
		return f'\tType: Chargeble Ticket\n\tTicket ID: {self.ticket_id}\n\tCredit: {self.balance}'


class DisposableTicket(Ticket):
	def __init__(self):
 		super().__init__()
 		print('print2')

	def use_disposable_ticket(self):
		self.used = True

	def expire(self):
		pass

	def __repr__(self):
		return f'\tType: Expirable Ticket\n\tTicket ID: {self.ticket_id}\n\tExpiration Date: {self.expiration_date}\n\tCredit: {self.balance}'


