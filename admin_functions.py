from read_csv_create_dataframe import read_csv_file, upload_data_to_file, upload_room_data_in_write_mood
from register_login import register, get_email, get_name, get_password

wrong_input = False
value_error_input = False
total_users = 0
user_id = 0
starting_room_number = 400

def print_error_if_any():
    global wrong_input, value_error_input
    if wrong_input:
        print("Please choose only from above list.")
        wrong_input = False
    if value_error_input:
        print("Please enter choice in integer format.")
        value_error_input = False
def get_choice(choice_list, function_name):
    global wrong_input, value_error_input
    if function_name == go_back:
        print("Press '0' to go back: ", end="")
    else:
        print("Enter your choice: ", end="")
    try:
        choice = int(input())
    except ValueError:
        value_error_input = True
        if function_name == admin_menu:
            function_name(user_id)
        function_name()
    else:
        if choice not in choice_list:
            wrong_input = True
            if function_name == admin_menu:
                function_name(user_id)
            function_name()
        return choice
def go_back():
    print_error_if_any()
    choice = get_choice([0], go_back)
    if choice == 0:
        admin_menu(user_id)
def show_current_user_info():
    data_list = read_csv_file("admin_registeration.csv")
    user_data = data_list[user_id]
    print(f"Your current info: {user_data}")
def show_success_message(colum_name):
    print(f"{first_last_name()} your {colum_name} has been changed successfully!!!")
    show_current_user_info()
    go_back()
def first_last_name():
    data_list_to_dict = read_csv_file("admin_registeration.csv")
    return f'{data_list_to_dict[user_id]["first_name"]} {data_list_to_dict[user_id]["last_name"]}!'

def display_data():
    global total_users
    count = 1
    data_list_to_dict = read_csv_file("student_registeration.csv")
    print("\tFIRST NAME\tLAST NAME\tEMAIL\t\t\t\tPASSWORD")
    for i in data_list_to_dict:
        print(
            f"{count}. \t{i['first_name']}\t\t{i['last_name']}\t\t{i['email']}\t{i['password']}")  # extract data from dictionary
        count += 1
    total_users = count - 1

def add_hostelite():
    register(2)
    go_back()

def display_hostelite_data():
    display_data()
    go_back()

def delete_hostelite():
    display_data()
    print(f"Which user {first_last_name()} you  want to delete or press '0' to go back.")
    print_error_if_any()
    choice_list = [0]
    for i in range(total_users):
        choice_list.append(i+1)
    choice_to_delete = get_choice(choice_list, delete_hostelite)
    if choice_to_delete == 0:
        admin_menu(user_id)
    elif choice_to_delete <= total_users:
        data_list_to_dict = read_csv_file("student_registeration.csv")
        if len(data_list_to_dict) > 1:
            del data_list_to_dict[-1]
        else:
            print("You can't delete all users.There must be at least one user")
        upload_data_to_file("student_registeration.csv", data_list_to_dict)
        delete_hostelite()
def allocate_rooms():
    global starting_room_number
    data_list = read_csv_file("student_registeration.csv")
    room_data = []
    for i in range(len(data_list)):
        room_info = {"room_number": starting_room_number,
                     "name": f"{data_list[i]['first_name']} {data_list[i]['last_name']}",
                     "email": data_list[i]['email']
                     }
        room_data.append(room_info)
        if i % 2 == 1:
            starting_room_number += 1
    upload_room_data_in_write_mood(room_data)

def view_room_allotment_info():
    allocate_rooms()
    room_data = read_csv_file("room_allotment.csv")
    print("\tROOM NO\t\tNAME\t\t\t\tEMAIL")
    for i in room_data:
        print(f"\t{i['room_number']}\t\t\t{i['name']}\t\t\t{i['email']}")
    go_back()

def view_complains():
    count = 1
    data_list_to_dict = read_csv_file("complaints.csv")
    print("\tNAME\t\t\tEMAIL ADDRESS\t\tCOMPLAIN")
    for i in data_list_to_dict:
        print(f"{count}. \t{i['name']}\t\t{i['email']}\t\t{i['complain']}")  # extract data from dictionary
        count += 1
    print()
    go_back()
def change_settings(column_name, value):
    data_dict_in_list = read_csv_file("admin_registeration.csv")
    data_dict_in_list[user_id][f"{column_name}"] = value
    upload_data_to_file("admin_registeration.csv", data_dict_in_list)
    show_success_message(column_name)
def profile_setting():
    show_current_user_info()
    print("1. Change first name\n2. Change last name\n3. Change your email\n4. Change your password\n5. Go back")
    print_error_if_any()
    choice = get_choice([1, 2, 3, 4, 5], profile_setting)
    if choice == 5:
        admin_menu(user_id)
    elif choice == 1:
        f_name = get_name("first name")
        change_settings("first_name", f_name)
    elif choice == 2:
        l_name = get_name("last name")
        change_settings("last_name", l_name)
    elif choice == 3:
        email = get_email("admin")
        change_settings("email", email)
    elif choice == 4:
        pswd = get_password()
        change_settings("password", pswd)
def logout():
    print(f'{first_last_name()} have been logout successfully.')
    exit(1)

def admin_menu(u_id):
    global user_id
    user_id = u_id
    print(
        f"Welcome {first_last_name()}\n1. Add hostelite\n2. Display hostelite data\n3. Delete hostelite data \n4. Room allotment info\n5. View Complains\n6. Admin profile settings \n7. Logout ")
    print_error_if_any()
    choice = get_choice([1, 2, 3, 4, 5, 6, 7], admin_menu)

    if choice == 1:
        add_hostelite()
    elif choice == 2:
        display_hostelite_data()
    elif choice == 3:
        delete_hostelite()
    elif choice == 4:
        view_room_allotment_info()
    elif choice == 5:
        view_complains()
    elif choice == 6:
        profile_setting()
    elif choice == 7:
        logout()
