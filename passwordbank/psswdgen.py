
pwd = input("What is your user password?: ")

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open("passwords.txt" , "a") as file:
        file.write(name + "|" + pwd + "\n")




def view():
    with open("passwords.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            data = line.rstrip()
            user, passw = data.split("|")
            print(f'Username: {user}, Password: {passw}')



while True:
    mode = input("Would you like to add a new passowrd? (add) , view existing passwords (view)")
    if mode == "q":
        break

    if mode.lower() == "add":
        add()
    elif mode.lower() == "view":
        view()



    else:
        print("Invalid Syntax")
        continue