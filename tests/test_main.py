 
import unittest
import pickle
import glob
from tickett import *
from clearr import clear
import json
import logging
import os
from usser import User,Admin

from bank_acc import BankAccount
from mainn import Menu

class TestMenu(unittest.TestCase):
    def test_create_new_user(self):
        user_obj = User("TestUser", "TestPassword")
        with open(f"C:/Users/DearUser/Desktop/metro-gp/user/{user_obj.id}.pickle" , 'wb') as user:
            pickle.dump(user_obj, user)

        with open(f"C:/Users/DearUser/Desktop/metro-gp/user/{user_obj.id}.pickle", 'rb') as user:
            loaded_user = pickle.load(user)

        self.assertEqual(loaded_user.username, "TestUser")
        self.assertEqual(loaded_user.password, "TestPassword")

    def test_log_in_as_user(self):
        user_obj = User("TestUser", "TestPassword")
        with open(f"C:/Users/DearUser/Desktop/metro-gp/user/{user_obj.id}.pickle" , 'wb') as user:
            pickle.dump(user_obj, user)

        objects = []
        for file in glob.glob("C:/Users/DearUser/Desktop/metro-gp/user/*.pickle"):
            with open(file, 'rb') as user:
                while True:
                    try:
                        content = pickle.load(user)
                        objects.append(content)
                    except EOFError:
                        break

        for user in objects:
            if user.username == "TestUser":
                if user.password == "TestPassword":
                    logged_in_user = user
                    break

        self.assertEqual(logged_in_user.username, "TestUser")
        self.assertEqual(logged_in_user.password, "TestPassword")

    def test_log_in_as_admin(self):
        admin_obj = Admin("TestAdmin", "TestPassword")
        with open(f"C:/Users/DearUser/Desktop/metro-gp/admin/{admin_obj.id}.pickle" , 'wb') as admin:
            pickle.dump(admin_obj, admin)

        objects = []
        for file in glob.glob("C:/Users/DearUser/Desktop/metro-gp/admin/*.pickle"):
            with open(file, 'rb') as admin:
                while True:
                    try:
                        content = pickle.load(admin)
                        objects.append(content)
                    except EOFError:
                        break

        for admin in objects:
            if admin.username == "TestAdmin":
                if admin.password == "TestPassword":
                    logged_in_admin = admin
                    break

        self.assertEqual(logged_in_admin.username, "TestAdmin")
        self.assertEqual(logged_in_admin.password, "TestPassword")

    def test_deposit(self):
        user_obj = User("TestUser", "TestPassword")
        with open(f"C:/Users/DearUser/Desktop/metro-gp/user/{user_obj.id}.pickle" , 'wb') as user:
            pickle.dump(user_obj, user)
        with open(f"C:/Users/DearUser/Desktop/metro-gp/user/{user_obj.id}.pickle", "rb") as user:
            user_obj = pickle.load(user)

        initial_balance = user_obj.balance
        deposit_amount = 100
        user_obj.deposit(deposit_amount)

        with open(f"C:/Users/DearUser/Desktop/metro-gp/user/{user_obj.id}.pickle", "rb") as user:
            user_obj = pickle.load(user)

        self.assertEqual(user_obj.balance, initial_balance + deposit_amount)

    def test_withdraw(self):
        user_obj = User("TestUser", "TestPassword")
        user_obj.deposit(100)
        with open(f"C:/Users/DearUser/Desktop/metro-gp/user/{user_obj.id}.pickle" , 'wb') as user:
            pickle.dump(user_obj, user)

        user_obj.withdraw(50)
        with open(f"C:/Users/DearUser/Desktop/metro-gp/user/{user_obj.id}.pickle" , 'rb') as user:
            loaded_obj = pickle.load(user)

        self.assertEqual(loaded_obj.balance, 50)


class TestMenu(unittest.TestCase):
    def setUp(self):
        self.menu = Menu()
        self.user = User("test_user", "password")
        with open(f"C:/Users/DearUser/Desktop/metro-gp/user/{self.user.id}.pickle" , 'wb') as user:
            pickle.dump(self.user, user)

    def test_run(self):
        self.assertIsNotNone(self.menu.run())

    def test_register_user(self):
        user_id = self.user.id
        with open(f"C:/Users/DearUser/Desktop/metro-gp/user/{user_id}.pickle", 'rb') as user:
            user_obj = pickle.load(user)

        self.assertEqual(user_obj.username, "test_user")
        self.assertEqual(user_obj.password, "password")

    def tearDown(self):
        os.remove(f"C:/Users/DearUser/Desktop/metro-gp/user/{self.user.id}.pickle")

# class TestUser(unittest.TestCase):
#     def setUp(self):
#         self.user = User("test_user", "password")

#     def test_create_bank_account(self):
#         self.user.create_bank_account()
#         self.assertIsInstance(self.user.bank_account, BankAccount)

#     def test_buy_ticket(self):
#         ticket = Ticket(10, "Disposable", "None")
#         self.user.buy_ticket(ticket)
#         self.assertIn(ticket, self.user.tickets)

#     def test_show_ticket_list(self):
#         ticket = Ticket(10, "Disposable", "None")
#         self.user.buy_ticket(ticket)
#         ticket_list = self.user.show_ticket_list()
#         self.assertIn(ticket, ticket_list)

# if __name__ == '__main__':
#     unittest.main()
