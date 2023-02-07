from user import User
import logging
import pickle
import os
admin_logger = logging.getLogger('Admin_logger')
admin_logger.setLevel(logging.INFO)
admin_f_h = logging.FileHandler('Admins.log')
admin_f_f = logging.Formatter('%(asctime)s - %(message)s')
admin_f_h.setFormatter(admin_f_f)
admin_f_h.setLevel(level=logging.INFO)
admin_logger.addHandler(admin_f_h)

class Admin(User):
    ticket_list = []
    def __init__(self, username, password):
        super().__init__(username, password)

    def create_new_admin(self):
        pass

    def make_ticket(self, ticket):
        self.__class__.ticket_list.append(ticket)

    def find_user(self, filename, search_path):
        result = []
        for root, dirname, files in os.walk(search_path):
            if filename in files:
                result.append(os.path.join(root, filename))
        with open(f'{result[0]}', 'rb') as f:
            user = pickle.load(f)
        return user

    def ban_user(self, user : User):
        user.banned_user = True
        # self.__class__.ticket_list.append()

    def delete_ticket_by_id(self, ticket_id):
        os.chdir('tickets')
        os.system(f'del {ticket_id}.pickle' if os.name =='nt' else f"rm {ticket_id}.pickle")
        input()

# obj = Admin('admin', 'admin')
# with open(f'{obj.id}.pickle', 'wb') as f:
#     pickle.dump(obj,  f)
