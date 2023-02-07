from user import User

class Admin(User):
    ticket_list = []
    def __init__(self, username, password):
        super().__init__(username, password)

    def create_new_admin(self):
        pass

    def make_ticket(self, ticket):
        if ticket == '3':
            ticket_obj = ExpirableTicket()

        elif ticket == '2':
            pass

        elif ticket =='1':
            pass

        self.__class__.ticket_list.append(ticket_obj)

    def delete_ticket_by_id(self, ticket_id):
        os.chdir('tickets')
        os.system(f'del {ticket_id}.pickle' if os.name =='nt' else f"rm {ticket_id}.pickle")
        input()
