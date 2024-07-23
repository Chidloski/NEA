from PyQt5 import QtCore, QtGui, QtWidgets
import re
import os
import hashlib

def LogIn(self, baseWindow, user, password, outputButton):
    # in the future this function can be used to compare user and password to database
    # encrypted database??

    if (user == "sam" and password == "chidlow"):
        baseWindow.stackedWidget.setCurrentIndex(3)
    else:
        self.ForgotPasswordButton.setHidden(False)

def PasswordVisibility(displayText, actualText, target):
# function alternates the display of the password input from bullets to plaintext 

    if (displayText == actualText):
        # handles when echo mode = normal
        target.setEchoMode(QtWidgets.QLineEdit().Password)
    else:
        # handles when echo mode = password
        target.setEchoMode(QtWidgets.QLineEdit().Normal)

def goToRegisterPage(baseWindow, user, password, registerPage):
    registerPage.UsernameInput.setText(user)
    registerPage.PasswordInput.setText(password)

    baseWindow.stackedWidget.setCurrentIndex(1)

def Register(baseWindow, user, fullName, email, password, rePassword):
    pass

def goToForgotPasswordPage(baseWindow, user, forgotPasswordPage):
    forgotPasswordPage.UsernameInput.setText(user)

    baseWindow.stackedWidget.setCurrentIndex(2)

def ResetPassword(baseWindow, user, email, password, rePassword):
    pass

def emailValidation(email):
    # Define the regular expression for validating an email address
    email_regex = re.compile(
        r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    )
    
    # Use the regex to match the email address
    if re.match(email_regex, email):
        return True
    else:
        return False
    
def usernameValidation(username):
    # Define the regular expression for validating the username
    username_regex = re.compile(r"^[a-zA-Z0-9_.-]{5,16}$")
    
    # Check if the username matches the regex
    if re.match(username_regex, username):
        return True
    else:
        return False

def doPasswordsMatch(password, rePassword):
    if password == rePassword:
        return True
    
    else:
        return False
    
def passwordHashing(password):
    # Generate a random 16-byte salt
    salt = os.urandom(16)
    
    # Create the hash using SHA-256
    hash_obj = hashlib.sha256(salt + password.encode())
    password_hash = hash_obj.digest()
    
    # Combine the salt and the password hash
    salt_and_hash = salt + password_hash
    
    # Encode the result in hexadecimal
    return salt_and_hash.hex()

def verifyPassword(storedHash, password):
    # decodes from hex
    saltAndHash = bytes.fromhex(storedHash)

    # separates salt from hash
    salt = saltAndHash[:16]
    originalHashedPassword = saltAndHash[16:]

    # hashes the new password and incorporates the salt
    newHash = hashlib.sha256(salt + password.encode())
    newHashedPassword = newHash.digest()

    # returns comparison
    return originalHashedPassword == newHashedPassword