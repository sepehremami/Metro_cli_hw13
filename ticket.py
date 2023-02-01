import uuid
import datetime
import pickle
from abc import ABC, abstractmethod
from dateutil.relativedelta import relativedelta

# pip install python-dateutil
menu = '''
__  __      _
|  \/  | ___| |_ _ __ ___
| |\/| |/ _ \ __| '__/ _ \

| |  | |  __/ |_| | | (_) |
|_|  |_|\___|\__|_|  \___/'''
buy_ticket_menu = {
	'1' : 'Chargeble',
	'2' : 'Disposable(you can use it only once)',
	'3' : 'Date Expirable'}

class Ticket(ABC):
	def __init__(self):
		self.creation_date = datetime.datetime.now()
		self.ticket_id = uuid.uuid1()

	@abstractmethod
	def expire(self):
		pass
	@abstractmethod
	def __repr__(self):
		pass
class ExpirableTicket(Ticket):
	def __init__(self):
		super().__init__()
		self.expiration_date = self.creation_date + relativedelta(years=1)
		self.balance = 50

	def __repr__(self):
		return f'Type: Expirable Ticket\nTicket ID: {self.ticket_id}\nExpiration Date: {self.expiration_date}\nCredit: {self.balance}'


	def expire(self):
		pass

class ChargebleTicket(Ticket):
	def __init__(self):
		super().__init__()

	def epxire(self):
		pass


class DisposableTicket(Ticket):
	def __init__(self):
 		super().__init__()
#
# 	@staticmethod
# 	def ticket_kind_display():
# 		ticket_kind = ['chargeble', 'credible', 'expirable']
# 		for i in ticket_kind:
# 			yield i
# #
#
# class User:
# 	def __init__(self, name, ticket:Ticket = None):
# 		self.name = name
# 		self._id = uuid.uuid1()
# 		self.ticket = None
#
# 	# def select_ticket_type(self, kind):
# 	# 	self.ticket = Ticket(kind)
#
# 	@property
# 	def id(self):
# 		return self._id
#
#
# class Metro:
# 	pass
#
#
# sepehr = User('sepehr')
# sepehr.select_ticket_type('chargeble')
# #print(sepehr.ticket.creation_date,sepehr.ticket.kind)
#


# class Menu:
# 	@staticmethod
# 	def run():
# 		print(menu)
# 		print()
# 		print('Select one of the below')
# 		user_options= {
# 			'1' : 'register new user',
# 			'2' : 'BankAccount management',
# 			'3' : 'Buy Metro Ticket',
# 			'4' : 'Log into Account'
# 			}
#
# 		for k , v in enumerate(user_options.items()):
# 			print(v)
#
# 		user_input_menu = input('Choose: ')
#
# 		if user_input_menu == '3':
# 			for i in enumerate(Ticket.ticket_kind_display(), 1):
# 				print(i)
# 			user_input_ticket = input('What Kind of Ticket would you like to buy? ')
# 			if user_input_ticket == '1':
# 				pass
# 			elif user_input_ticket == '2':
# 				pass
# 			elif user_input_ticket == '3':
# 				pass
