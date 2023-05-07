from read_csv_create_dataframe import read_csv_file, upload_data_to_file

MUST_IN_EMAIL = ["@gmail.com", "@yahoo.com", "@outlook.com"]
user_name = "student"
user_id = 0
user = 0


def login(u):
    global user_name, user_id
    if u == 1:
        user_name = "admin"
    count_for_wrong_login = 1
    while count_for_wrong_login <= 3:
        user_num = 0
        email = input(f"Enter your {user_name} email: ").lower()
        password = input("Enter your password: ")
        list_data = read_csv_file(f"{user_name}_registeration.csv")
        for row in list_data:
            user_num += 1
            if row["email"] == email and row["password"] == password:
                user_id = user_num - 1
                return 1 if user_name == "admin" else 2
            if count_for_wrong_login == 3:
                return 0
        count_for_wrong_login += 1


def upload_data(f_name, l_name, mail, pswd):
    data_dict_in_list = read_csv_file(f"{user_name}_registeration.csv")
    # creating a list of dictionary that includes first name, last name,email,password
    info = {"first_name": f_name, "last_name": l_name, "email": mail, "password": pswd}
    data_dict_in_list.append(info)
    upload_data_to_file(f"{user_name}_registeration.csv", data_dict_in_list)
    print(f"{f_name} {l_name}! you have been registered successfully ")

def get_name(choice):
    count_for_name = 1
    name = input(f"Enter your {choice}  : ").title()
    while len(name) < 1:
        name = input(f"Enter your {choice} : ").title()
        count_for_name += 1
        if count_for_name % 3 == 0:
            print("Your name must have some length. ", end="")
    return name

def check_already_mail(mail):
    data_dict_in_list = read_csv_file(f"{user_name}_registeration.csv")
    for i in data_dict_in_list:
        if i["email"] == mail:
            print(f"Someone already registered with {mail} Please try again.")
            mail = get_email(user_name)
            break
    return mail

def get_email(u_name):
    global user_name
    user_name = u_name
    count_for_email = 1
    e_mail = input("Enter your mail : ").lower()
    while len(e_mail) < 12:
        if count_for_email % 3 == 0:
            print("Your mail must have proper length.", end="")
        e_mail = input("Enter your mail : ").lower()
        count_for_email += 1

    while not (e_mail[-10:] in MUST_IN_EMAIL or e_mail[-12:] in MUST_IN_EMAIL):
        e_mail = input("Enter right mail : ").lower()
        while len(e_mail) < 12:
            e_mail = input("Please enter right email of proper length. ").lower()
    mail = check_already_mail(e_mail)
    return mail

def get_password():
    count_for_password = 1
    password = input("Enter the password : ")
    while len(password) < 8:
        count_for_password += 1
        if count_for_password % 3 == 0:
            print("Your password must have proper length.", end="")
        password = input("Enter the password: ")
    confirm_password = input("Enter the confirm password: ")
    while password != confirm_password:
        password = input("Password not match.Enter the password again: ")
        while len(password) < 8:
            print("Your password must have proper length.", end="")
            password = input("Enter the password again: ")
        confirm_password = input("Enter the confirm password: ")
    return password

def register(u):
    global user_name, user
    user = u
    if user == 1:
        user_name = "admin"

    first_name = get_name("first_name")
    last_name = get_name("last_name")
    email = get_email(user_name)
    password = get_password()
    upload_data(first_name, last_name, email, password)
