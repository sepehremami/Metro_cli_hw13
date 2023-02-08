import logging

user_logger = logging.getLogger('User_logger')
user_logger.setLevel(logging.INFO)
user_f_h = logging.FileHandler('Users.log')
user_f_f = logging.Formatter('%(asctime)s - %(message)s')
user_f_h.setFormatter(user_f_f)
user_f_h.setLevel(level=logging.INFO)
user_logger.addHandler(user_f_h)

admin_logger = logging.getLogger('Admin_logger')
admin_logger.setLevel(logging.INFO)
admin_f_h = logging.FileHandler('Admins.log')
admin_f_f = logging.Formatter('%(asctime)s - %(message)s')
admin_f_h.setFormatter(admin_f_f)
admin_f_h.setLevel(level=logging.INFO)
admin_logger.addHandler(admin_f_h)

error_logger = logging.getLogger('Error_logger')
error_f_h = logging.FileHandler('Errors.log')
error_f_f = logging.Formatter('%(asctime)s - %(message)s')
error_f_h.setFormatter(error_f_f)
error_logger.addHandler(error_f_h)
