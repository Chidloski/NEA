from userFunctions import passwordHashing, verifyPassword

password = "hellohello12"
hashed = passwordHashing(password)
print(hashed)

valid = verifyPassword(hashed, "hellohello")
print(valid)