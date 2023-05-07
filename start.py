count_for_wrong_user = 1
count_for_wrong_regis_login = 1
choice_1 = 0
choice_2 = 0
def choice_for_regis_or_login():
    global count_for_wrong_regis_login, choice_2
    print("1.Register\n2.Login")
    while count_for_wrong_regis_login <= 3:
        try:
            choice = int(input("Enter Register/login choice : "))
            choice_2 = choice
        except ValueError:
            print("You must enter integer value.")
            count_for_wrong_regis_login += 1
            choice_for_regis_or_login()
            return choice_2
        else:
            if choice == 1:
                return 1
            elif choice == 2:
                return 2
            else:
                print("You must enter within range .")
                count_for_wrong_regis_login += 1
    return 0
def choose_user():

    global count_for_wrong_user, choice_1
    print("1.ADMIN\n2.Hostelite")

    while count_for_wrong_user <= 3:
        try:
            choice = int(input("Enter user choice : "))
            choice_1 = choice
        except ValueError:
            print(f"Enter the integer number.")
            count_for_wrong_user += 1
            choose_user()
            return choice_1
        else:
            if choice == 1 or choice == 2:
                return choice
            else:
                print("Your choice must be 1 or 2.")
                count_for_wrong_user += 1
    return 0
