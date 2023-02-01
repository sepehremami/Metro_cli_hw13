import pickle
import glob
import uuid
from ticket import ExpirableTicket, Ticket
from clear import clear
from pprint import pprint


class BankAccount:
    def __init__(self, title, balance):
        self.balance = balance
        self.title = title

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        assert self.balance > amount, "Insufficient Funds"
        self.balance -= amount

    def display_account_info(self, name):

        assert (self.balance - 1) > 0 , "Insufficient Funds"
        self.balance -= 1
        return f"User:{name}'s {self.title} and account balance is ${round(self.balance,2)}.\nCharging 1$ for taking balance!"


class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password
        self.account = BankAccount(title="Main_Account", balance = 10)
        self.ticket_list = []
        self.__id = uuid.uuid1()

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

    def use_ticket(self, ticket):
        pass

    def show_ticket_list(self):
        for ticket in enumerate(self.ticket_list):
            yield ticket



class Menu:
    login_menu= {
        '1' : 'Bank Account Management',
        '2' : 'Buy Ticket',
        '3' : 'Log out'}

    bank_acount_menu = {
        '1' : 'Deposit',
        '2' : 'Withdraw',
        '3' : 'Show Balance',
        '4' : 'Go back...'}

    buy_ticket_menu = {
        '1' : 'Chargeble',
        '2' : 'Disposable(you can use it only once)',
        '3' : 'Date Expirable',
        '4' : 'Show Ticket List'}

    with open('count.txt', 'rb') as f:
        a = f.read().decode('ASCII').strip()
    user_count = int(a)

    @classmethod
    def user_count_increment(cls):
        cls.user_count += 1
        return cls.user_count

    @classmethod
    def user_count_save_for_future(cls):
        with open('count.txt', 'w') as file:
            file.write(str(Menu.user_count))

    @staticmethod
    def run():
        while True:
            clear()
            print('menu')
            print()
            print('Select one of the below')
            user_options= {
                '1' : 'Register New User',
                '2' : 'Log in as User',
                '3' : 'Log in as Administrator',
                '4' : 'Exit'
                }

            for k , v in enumerate(user_options.items()):
                print(v)

            user_input_menu = input('Choose: ')

            if user_input_menu == '1':
                clear()
                name = input('Enter username: ')
                password = input('Enter password: ')
                user_obj = User(name, password)
                with open(f"{user_obj.id}.pickle" , 'wb') as user:
                    pickle.dump(user_obj, user)
                print('You Are Now Part of METRO')
                print(f'Your Metro ID: {user_obj.id}')
                input('C...')

            elif user_input_menu == '2':
                clear()
                objects = []
                user_id = input('Enter Unique ID(Forgot password?(y)): ')
                log_in_flag = False
                logged_in_person = None
                if user_id == 'y':
                    clear()
                    for file in glob.glob("*.pickle"):
                        with open(file, 'rb') as user:
                            while True:
                                try:
                                    content = pickle.load(user)
                                    objects.append(content)
                                except EOFError:
                                    break
                    # print(objects, type(objects[1].username) )
                    name = input('Enter username: ')
                    password = input('Enter password: ')
                    for user in objects:
                        # print(user.username , user.password)
                        if user.username == name:
                            if user.password == password:
                                print(f'Your id is:\n{user.id}')
                                input('C...')
                                clear()
                                break
                            else:
                                print("Wrong Password")
                                input('C...')
                                break

                else:
                    try:
                        with open(f"{user_id}.pickle", 'rb') as user:
                            user_obj = pickle.load(user)

                        logged_in_person = user_obj
                        log_in_flag = True
                    except FileNotFoundError:
                        print("User not found!")
                        input('C..')



                # print(logged_in_person)
                while log_in_flag:
                    clear()
                    print(Menu.login_menu)
                    login_user_input = input("What do you desire? ")
                    if login_user_input == '1':
                        print(Menu.bank_acount_menu)
                        user_input = input("Choose: ")
                        if user_input == '1':
                            clear()
                            amount = input('The amount you want to deposit? ')
                            print('Shaparak')
                            input()
                            logged_in_person.make_deposit(float(amount))
                            print(logged_in_person.account.balance)
                            input('C...')

                        elif user_input =='2':
                            pass

                        elif user_input == '3':
                            clear()
                            try:
                                print(logged_in_person.account.display_account_info(logged_in_person.username))
                                input('C...')
                            except AssertionError as e:
                                print (e)
                                input('C...')


                    # injash beautifule(?!)
                    elif login_user_input == '2':
                        pprint(Menu.buy_ticket_menu, indent=2)
                        user_ticket_choice  = input('choose: ')
                        if user_ticket_choice == '3':



                            try:
                                logged_in_person.make_withdraw(55)
                                ex_ticket = ExpirableTicket()
                                logged_in_person.buy_ticket(ex_ticket)
                                print(logged_in_person.ticket_list)
                                input("C...")
                            except AssertionError as e:
                                print(e)
                                input('C...')



                        elif user_ticket_choice == '4':
                            for i in (logged_in_person.show_ticket_list()):
                                print(i)
                            input('C...')

                    elif login_user_input == '3':
                        with open(f'{logged_in_person.id}.pickle', 'wb') as user:
                            pickle.dump(logged_in_person, user)
                        break


# fc0ff53e-a0a8-11ed-a272-a41731ccaf53
# shervin; fd6f9216-a168-11ed-a1bf-a41731ccaf53



                        # if user.username == name and user.password == password:
                        #     print('you have successfuly loged in')
            elif user_input_menu == '4':
                Menu.user_count_save_for_future()
                break

# if self.__check_minimum_balance(amount):
# raise BankAccount.MinBalanceError("NOT Enough balance to withdraw!")
# self.__balance -= amount
# self.__balance -= self.WAGE_AMOUNT


if __name__ == '__main__':
    Menu.run()




