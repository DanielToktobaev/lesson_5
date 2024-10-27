loginMain = "Daniel"
passwordMain = "22.01.2009@Daniel"

inputLogin = input("Enter login: ")
inputPassword = input("Enter password: ")

if inputLogin == loginMain and inputPassword == passwordMain:
    print("You successfully logged in!")
else:
    print("Login or password is wrong! Try again.")