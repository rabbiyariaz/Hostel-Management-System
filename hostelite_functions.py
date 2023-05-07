from read_csv_create_dataframe import read_csv_file, upload_data_to_file
from register_login import get_name, get_email, get_password

wrong_input = False
value_error_input = False
user_id = 0

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
        if function_name == hostelite_menu:
            function_name(user_id)
        function_name()
    else:
        if choice not in choice_list:
            wrong_input = True
            if function_name == hostelite_menu:
                function_name(user_id)
            function_name()
        return choice
def go_back():
    print_error_if_any()
    choice = get_choice([0], go_back)
    if choice == 0:
        hostelite_menu(user_id)
def show_current_user_info():
    data_list = read_csv_file("student_registeration.csv")
    user_data = data_list[user_id]
    print(f"Your current info: {user_data}")
def show_success_message(colum_name):
    print(f"{first_last_name()} your {colum_name} has been changed successfully!!!")
    show_current_user_info()
    go_back()
def first_last_name():
    data_list_to_dict = read_csv_file("student_registeration.csv")
    return f'{data_list_to_dict[user_id]["first_name"]} {data_list_to_dict[user_id]["last_name"]}!'

def mess_menu():
    print(
        "1.Roti = Rs20\n2.Chicken = Rs200\n3.Biryani = Rs250\n4.Daal = Rs150\n5.Cold Drink = Rs70\n6.Vegetable = Rs150")
    x = int(input('Enter the number of the item you want: '))
    y = int(input('Enter the number of items: '))
    total = 0
    if x == 1:
        total = 20
    elif x == 2:
        total = 200
    elif x == 3:
        total = 250
    elif x == 4:
        total = 150
    elif x == 5:
        total = 70
    elif x == 5:
        total = 150
    else:
        print('You entered the wrong number! Enter again.')
        mess_menu()
    print('Your total bill is', total * y)


def prohibited_materials():
    print(
        "Following items and activities are not allowed in hostel premises:\n\n1.Firearms and daggers.\n2.Alcohols, toxic drugs, sheesha, gutkha and hashish/heroin.\n3.Crackers, explosives and ammunition.\n4.Objectionable material in the shape of videos, books or photographs.\n5.Involvement in undesireable political and sectarian activities.\n6.Joining banned organizations or involvement in antistate activities.\n")
    go_back()
def register_complain():
    complain = input("Write down your complain.\n")
    while len(complain) < 10:
        complain = input("Your complain must have 10 characters at least.Write down your complain.\n")
    complaint_list_data = read_csv_file("complaints.csv")
    user_list_data = read_csv_file("student_registeration.csv")
    complaint_info = {"name": f'{first_last_name()}', "email": user_list_data[user_id]['email'], "complain": complain }
    complaint_list_data.append(complaint_info)
    upload_data_to_file("complaints.csv", complaint_list_data)
    print(f"{first_last_name()} your complain has been submitted successfully!!!")
    go_back()
def view_your_room_info():
    room_data = read_csv_file("room_allotment.csv")
    data_list = read_csv_file("student_registeration.csv")
    my_email = data_list[user_id]['email']
    my_room_number = 0
    room_mate_name = ""
    room_mate_email = ""

    for i in room_data:
        if i['email'] == my_email:
            my_room_number = i['room_number']
    count = 0
    for i in room_data:
        if i['room_number'] == my_room_number:
            count += 1
            room_mate_name = i['name']
            room_mate_email = i['email']

    if my_room_number == 0:
        print("Your room is not allocated yet. Soon room will be allocated to you.")
    else:
        print(f"Your room number is {my_room_number}")
        if room_mate_name != "" and count == 2:
            print(f"Your room mate info\nNAME: '{room_mate_name}'\nEMAIL: '{room_mate_email}'")
        else:
            print("You don't have any room mate yet.Please wait until new student enroll.")
    go_back()
def complain_submission():
    print("1. Enter complain\n2. Go back")
    print_error_if_any()
    choice = get_choice([1, 2], complain_submission)
    if choice == 1:
        register_complain()
    elif choice == 2:
        hostelite_menu(user_id)
def change_settings(column_name, value):
    data_dict_in_list = read_csv_file("student_registeration.csv")
    data_dict_in_list[user_id][f"{column_name}"] = value
    upload_data_to_file("student_registeration.csv", data_dict_in_list)
    show_success_message(column_name)

def profile_setting():
    show_current_user_info()
    print("1. Change first name\n2. Change last name\n3. Change your email\n4. Change your password\n5. Go back")
    print_error_if_any()
    choice = get_choice([1, 2, 3, 4, 5], profile_setting)
    if choice == 5:
        hostelite_menu(user_id)
    elif choice == 1:
        f_name = get_name("first name")
        change_settings("first_name", f_name)
    elif choice == 2:
        l_name = get_name("last name")
        change_settings("last_name", l_name)
    elif choice == 3:
        email = get_email("student")
        change_settings("email", email)
    elif choice == 4:
        pswd = get_password()
        change_settings("password", pswd)

def logout():
    print(f'{first_last_name()} you have been logout successfully.')
    exit(1)
def hostelite_menu(u_id):
    global user_id, wrong_input, value_error_input
    user_id = u_id
    print(f"Welcome {first_last_name()}\n1. Mess menu\n2. Prohibited material\n3. View your room info\n4. Complain submission\n5. Profile Settings\n6. Logout ")

    print_error_if_any()
    choice = get_choice([1, 2, 3, 4, 5, 6], hostelite_menu)
    if choice == 1:
        mess_menu()
    elif choice == 2:
        prohibited_materials()
    elif choice == 3:
        view_your_room_info()
    elif choice == 4:
        complain_submission()
    elif choice == 5:
        profile_setting()
    elif choice == 6:
        logout()
