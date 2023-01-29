import pickle
import glob


class BankAccount:
    def __init__(self, title, balance):
        self.balance = balance
        self.title = title

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            self.balance -= 5
            print("Insufficient Funds: Charging a $5 fee!")
        return self

    def display_account_info(self,name):
        self.balance -= 1
        print(f"User:{name}'s {self.title} and account balance is ${round(self.balance,2)}.\nCharging 1$ for taking balance!")
        return self

class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password
        self.account = BankAccount(title="Main_Account", balance = 0)

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

    def make_deposit(self, amount, num):
        self.account.deposit(amount)
        return self

    def make_withdraw(self, amount,num):
        self.account.withdraw(amount)
        return self

    def display_account_info(self,num):
        self.account.display_account_info(self.name)
        return self



class Menu:

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
                name = input('Enter username: ')
                password = input('Enter password: ')
                user_obj = User(name, password)
                with open(f"user{Menu.user_count_increment()}.pickle" , 'wb') as user:
                    pickle.dump(user_obj, user)
                print('You Are Now Part of METRO')

            elif user_input_menu == '2':
                objects = []
                for file in glob.glob("*.pickle"):
                    with open(file, 'rb') as user:
                        while True:
                            try:
                                content = pickle.load(user)
                                objects.append(content)
                            except EOFError:
                                break
                            print(objects,objects[0].username)
                logged_in_person = []
                for user in objects:
                    name = input('Enter username: ')
                    if user.username == name:
                         password = input('Enter password: ')
                         if user.password == password:
                             print('You Have Successfuly Logged in')
                             input('C...')
                             logged_in_person.append(user)
                             break
                         else:
                             print("Wrong Password")
                             input('C...')
                             break
                    else:
                         print( "No Such Person")
                         break

                print(logged_in_user)
                        # if user.username == name and user.password == password:
                        #     print('you have successfuly loged in')
            elif user_input_menu == '4':
                Menu.user_count_save_for_future()
                break





if __name__ == '__main__':
    Menu.run()




