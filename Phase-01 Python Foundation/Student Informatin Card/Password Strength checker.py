print("==================PASSWORD STRENGTH CHECKER=================\n")
Password = input("Enter your password:")

print("Password length:" , len(Password))
print("Contains Uppercase:" , Password.isupper())
print("Contains lowercase:" , Password.islower())
print("Contains Digit:" , Password.isdigit())
print("Contains special character:" , not Password.isalnum())

if len(Password) >= 8 and not Password.isalnum() and not Password.isupper() and not Password.islower() and not Password.isdigit():
    print("Strong Password")
else:
    print("Weak Password")

