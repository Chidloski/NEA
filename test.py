from widgets.userWidgets.functions.userFunctions import passwordHashing, verifyPassword

password = "hellohello12"
hashed = passwordHashing(password)
print(hashed)

valid = verifyPassword(hashed, "hellohello")
print(valid)

print(10**4)