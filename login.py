import re

baseLogin = input("Enter login you are going to use in future: ")
basePassword = input("Enter password you are going to use in future: ")

def check_pass():
    if (len(baseLogin) >= 8 and
        re.search(r"[A-Z]", basePassword) and
        re.search(r"[a-z]", basePassword) and
        re.search(r"\d", basePassword) and
        re.search(r"[!@#$%^&*()_+<>?]", basePassword)):
        print("Password has all requirements!")
    else:
        print("Password is not hard enough.")
        exit()


check_pass()

inputLogin = input("Enter login: ")
inputPassword = input("Enter password: ")

if inputLogin == baseLogin and inputPassword == basePassword:
    print("You successfully logged in!")
elif inputLogin == baseLogin and inputPassword != basePassword:
    print("Your password is wrong!")
elif inputLogin != baseLogin and inputPassword == basePassword:
    print("Your login is wrong!")
else:
    print("Login and password is wrong you dumbass!")