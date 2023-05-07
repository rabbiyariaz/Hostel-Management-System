import register_login
from start import choice_for_regis_or_login, choose_user
from register_login import *
from admin_functions import admin_menu
from hostelite_functions import hostelite_menu

user = choose_user()
if user in [1, 2]:
    mood = choice_for_regis_or_login()
    if mood == 1:
        register(user)
    elif mood == 2:
        user_login = login(user)
        if user_login == 1:
            admin_menu(register_login.user_id)
        elif user_login == 2:
            hostelite_menu(register_login.user_id)
        else:
            print("You cannot choose more than three times.")
    else:
        print("You enter wrong admin/login choice.")
else:
    print("You enter wrong user choice 3 times .")

