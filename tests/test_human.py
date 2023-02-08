 
import unittest
from bank import BankAccount
from metro import User, Admin
from metro import ChargebleTicket, ExpirableTicket, DisposableTicket

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("test_us", "2324#hffd")

    def test_init(self):
        self.assertEqual(self.user.username, "test_us")
        self.assertEqual(self.user.password, "2324#hffd")
        self.assertIsInstance(self.user.account, BankAccount)
        self.assertEqual(self.user.account.balance, 10)
        self.assertEqual(self.user.ticket_list, [])

    def test_make_deposit(self):
        self.user.make_deposit(100)
        self.assertEqual(self.user.account.balance, 110)

    def test_make_withdraw(self):
        self.user.make_withdraw(5)
        self.assertEqual(self.user.account.balance, 5)

    def test_buy_ticket(self):
        ticket = Ticket(location="New York")
        self.user.buy_ticket(ticket)
        self.assertEqual(len(self.user.ticket_list), 1)
        self.assertEqual(self.user.ticket_list[0].location, "New York")

    def test_use_ticket_bynumber(self):
        ticket = Ticket(location="New York")
        self.user.buy_ticket(ticket)
        self.user.use_ticket_bynumber(1)
        self.assertEqual(len(self.user.ticket_list), 0)

    def test_use_ticket_byid(self):
        ticket = Ticket(location="New York")
        self.user.buy_ticket(ticket)
        self.user.use_ticket_byid(str(ticket.ticket_id))
        self.assertEqual(len(self.user.ticket_list), 0)

    def test_charge_chargeble_ticket(self):
        ticket = ChargebleTicket(location="New York")
        self.user.buy_ticket(ticket)
        self.user.charge_chargeble_ticket(1, 20)
        self.assertEqual(self.user.ticket_list[0].amount_left, 20)

    def test_show_ticket_list(self):
        ticket = Ticket(location="New York")
        self.user.buy_ticket(ticket)
        ticket_list = list(self.user.show_ticket_list())
        self.assertEqual(len(ticket_list), 1)
        self.assertEqual(ticket_list[0].location, "New York")

    def test_show_account_information(self):
        self.assertEqual(self.user.show_account_information(),
                         "username:test_user\nuser_id:" + str(self.user.id) + "\n")


class TestAdmin(unittest.TestCase):
    def setUp(self):
        self.admin = Admin('parande', 'passd#!234')
        self.user = User("userop", "password#123")
        self.ticket = DisposableTicket()

    def test_create_new_admin(self):
        # create_new_admin is not implemented, check it raises NotImplementedError
        with self.assertRaises(NotImplementedError):
            self.admin.create_new_admin()

    def test_make_ticket(self):
        self.admin.make_ticket(self.ticket)
        self.assertIn(self.ticket, self.admin.ticket_list)

    def test_find_user(self):
        user = User('test_user', 'password')
        user.update_user()
        found_user = self.admin.find_user(f'{user.id}.pickle', 'user')
        self.assertEqual(user.id, found_user.id)
        self.assertEqual(user.username, found_user.username)
        self.assertEqual(user.password, found_user.password)
        self.assertEqual(user.account.title, found_user.account.title)
        self.assertEqual(user.account.balance, found_user.account.balance)
        os.remove(f'../users/{user.id}.pickle')

    def test_find_ticket(self):
        self.ticket.update_ticket()
        found_ticket = self.admin.find_ticket(f'{self.ticket.ticket_id}.pickle', 'ticket')
        self.assertEqual(self.ticket.ticket_id, found_ticket.ticket_id)
        self.assertEqual(self.ticket.expiration_date, found_ticket.expiration_date)
        self.assertEqual(self.ticket.ticket_type, found_ticket.ticket_type)
        self.assertEqual(self.ticket.valid, found_ticket.valid)
        self.assertEqual(self.ticket.start_date, found_ticket.start_date)
        # os.remove(f'C:/Users/DearUser/Desktop/metro-gp/tickets/{self.ticket.ticket_id}.pickle')

    def test_save_user(self):
        self.admin.save_user()
        with open(f'../admins/{self.admin.id}.pickle', 'rb') as f:
            saved_admin = pickle.load(f)
        self.assertEqual(self.admin.id, saved_admin.id)
        self.assertEqual(self.admin.username, saved_admin.username)
        self.assertEqual(self.admin.password, saved_admin.password)
        self.assertEqual(self.admin.account.title, saved_admin.account.title)
        self.assertEqual(self.admin.account.balance, saved_admin.account.balance)
        # os.remove(f'C:/Users/DearUser/Desktop/metro-gp/admin/{self.admin.id}.pickle')

    def test_ban_user(self):
        self.user.update_user()
        self.admin.ban_user("user")
        path = "../users"
        filename = f"{self.user.id}.pickle"
        banned_user = self.admin.find_user(filename, path)
        self.assertTrue(banned_user.banned)
        # os.remove(f"C:/Users/DearUser/Desktop/metro-gp/user/{self.user.id}.pickle")

    def test_delete_ticket_by_id(self):
        # create an admin instance
        admin = Admin()

        # create two tickets
        ticket1 = Ticket("issue1", "description1")
        ticket2 = Ticket("issue2", "description2")

        # add the tickets to the admin's ticket list
        admin.add_ticket(ticket1)
        admin.add_ticket(ticket2)

        # check that the tickets have been added
        self.assertEqual(len(admin.tickets), 2)

        # delete the first ticket by id
        admin.delete_ticket_by_id(ticket1.id)

        # check that the first ticket has been deleted
        self.assertEqual(len(admin.tickets), 1)
        self.assertNotIn(ticket1, admin.tickets)
        self.assertIn(ticket2, admin.tickets)

    def test_delete_ticket_by_id_with_invalid_id(self):
        # create an admin instance
        admin = Admin()

        # create two tickets
        ticket1 = Ticket("issue1", "description1")
        ticket2 = Ticket("issue2", "description2")

        # add the tickets to the admin's ticket list
        admin.add_ticket(ticket1)
        admin.add_ticket(ticket2)

        # check that the tickets have been added
        self.assertEqual(len(admin.tickets), 2)

        # try to delete a ticket with an invalid id
        admin.delete_ticket_by_id("invalid_id")

        # check that no tickets have been deleted
        self.assertEqual(len(admin.tickets), 2)
        self.assertIn(ticket1, admin.tickets)
        self.assertIn(ticket2, admin.tickets)

if __name__ == '__main__':
    unittest.main()
