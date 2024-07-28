from PyQt5 import QtCore, QtGui, QtWidgets
import re
import os
import hashlib
from playerDB.jsonFunctions import *
from playerDB.passwordFunctions import *

# checks username and password against database and cycles to next widget if there is a match
def LogIn(self, baseWindow, user, password):

    record = getData("users", username = user)

    if len(record) == 0:
        self.ErrorLabel.setText("Incorrect username")
        self.ErrorLabel.setHidden(False)
        self.ForgotPasswordButton.setHidden(False)

    else:
        id = record[0]["id"]

        query = {"id": id}

        passwordRecord = getData("passwords", **query)

        hashedPassword = passwordRecord[0]["hash"]

        if verifyPassword(hashedPassword, password):
            baseWindow.userId = id
            baseWindow.stackedWidget.setCurrentIndex(3)

        else:
            self.ErrorLabel.setText("Incorrect password")
            self.ErrorLabel.setHidden(False)
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
    # pre populates fields in the register page
    registerPage.UsernameInput.setText(user)
    registerPage.PasswordInput.setText(password)

    # cycles to register widget
    baseWindow.stackedWidget.setCurrentIndex(1)



# ensures all inputs are correct before adding data to table and cycling to login page
def Register(self, baseWindow, user, fullName, email, password, rePassword):
    if len(user) == 0 or len(email) == 0 or len(fullName) == 0 or len(password) == 0 or len(rePassword) == 0:
        self.ErrorLabel.setText("Please ensure all fields are filled")
        self.ErrorLabel.setHidden(False)

    elif usernameValidation(user) == False:
        self.ErrorLabel.setText("Username between 5-16 characters \n Allowed special characters: _, -, .")
        self.ErrorLabel.setHidden(False)

    elif emailValidation(email) == False:
        self.ErrorLabel.setText("Invalid email address")
        self.ErrorLabel.setHidden(False)

    elif passwordValidation(password) == False:
        self.ErrorLabel.setText("Ensure password is at least 5 characters")
        self.ErrorLabel.setHidden(False)
    
    elif doPasswordsMatch(password, rePassword) == False:
        self.ErrorLabel.setText("Passwords do not match")
        self.ErrorLabel.setHidden(False)

    elif isUnique("email", email) == False:
        self.ErrorLabel.setText("Email already taken")
        self.ErrorLabel.setHidden(False)

    elif isUnique("username", user) == False:
        self.ErrorLabel.setText("Username already taken")
        self.ErrorLabel.setHidden(False)

    else:
        userData = {
            "username": user,
            "email": email,
            "fullName": fullName,
            "rating": 800,
            "match1": -1,
            "match2": -1,
            "match3": -1
        }

        insert("users", userData)

        hashedPassword = passwordHashing(password)

        passwordData = {
            "hash": hashedPassword
        }

        insert("passwords", passwordData)

        baseWindow.stackedWidget.setCurrentIndex(0)



def goToForgotPasswordPage(baseWindow, user, forgotPasswordPage):
    # pre-populates some fields in the forgot password widget
    forgotPasswordPage.UsernameInput.setText(user)

    # cycles to the correct widget
    baseWindow.stackedWidget.setCurrentIndex(2)


# goes through all validation steps before hashing and storing new password
def ResetPassword(self, baseWindow, user, email, password, rePassword):

    if len(user) == 0 or len(email) == 0 or len(password) == 0:
        self.ErrorLabel.setText("Please ensure all fields are filled")
        self.ErrorLabel.setHidden(False)

    elif doPasswordsMatch(password, rePassword) == False:
        self.ErrorLabel.setText("Passwords do not match")
        self.ErrorLabel.setHidden(False)

    else:
        data = getData("users", username = user, email = email)

        if len(data) == 0:
            self.ErrorLabel.setText("Invalid email or username")
            self.ErrorLabel.setHidden(False)

        else:
            id = data[0]["id"]

            hashedPassword = passwordHashing(password)

            passwordRecord = {
                "id": id,
                "hash": hashedPassword
            }

            update("passwords", passwordRecord, id)

            baseWindow.stackedWidget.setCurrentIndex(0)



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



def passwordValidation(password):
    # Define the regular expression for validating the password
    password_regex = re.compile(r"^[a-zA-Z0-9!@£$%^&*()_+=-€#~`,./<>?;':|{}]{5,}$")
    
    # Check if the password matches the regex
    if re.match(password_regex, password):
        return True
    else:
        return False


def doPasswordsMatch(password, rePassword):
    if password == rePassword:
        return True
    
    else:
        return False
    


