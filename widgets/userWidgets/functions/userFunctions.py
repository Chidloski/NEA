from PyQt5 import QtCore, QtGui, QtWidgets
import re
from playerDB.jsonFunctions import *
from playerDB.passwordFunctions import *

# checks username and password against database and cycles to next widget if there is a match
def LogIn(self, baseWindow, user, password):

    record = getData("users", username = user)


    if len(record) == 0:
        self.errorLabel.setText("Incorrect username")
        self.errorLabel.setHidden(False)
        self.forgotPasswordButton.setHidden(False)

    else:
        id = record[0]["id"]

        query = {"id": id}

        passwordRecord = getData("passwords", **query)

        hashedPassword = passwordRecord[0]["hash"]

        if verifyPassword(hashedPassword, password):
            self.errorLabel.setHidden(True)

            self.usernameInput.setText("")
            self.passwordInput.setText("")

            baseWindow.userId = id
            baseWindow.stackedWidget.setCurrentIndex(3)
            baseWindow.dashboard.playWidget.resetUi(id)
            baseWindow.dashboard.puzzleWidget.resetUi(id)
            baseWindow.dashboard.accountBoard.populate(id)

            query = {"id": id}
            userData = getData("users", **query)
            pieceIndex = userData[0]["pieces"]
            themeIndex = userData[0]["theme"]
            fontType = userData[0]["font"]

            pieceQuery = {"id": pieceIndex}
            pieceData = getData("pieces", **pieceQuery)
            pieceFolder = pieceData[0]["folder"]
            baseWindow.dashboard.changePieces(pieceFolder)

            themeQuery = {"id": themeIndex}
            themeData = getData("themes", **themeQuery)
            themeDict = themeData[0]
            baseWindow.dashboard.themeDict = themeDict

            styleSheet = """
                lightSquare {
                background-color: rgb(""" + themeDict["light"] + """);
                color: rgb(""" + themeDict["dark"] + """);
                }

                darkSquare {
                background-color: rgb(""" + themeDict["dark"] + """);
                color: rgb(""" + themeDict["light"] + """);
                };"""
            
            baseWindow.dashboard.changeTheme(styleSheet, themeDict)

            baseWindow.dashboard.changeFont(fontType)

            baseWindow.dashboard.menu.playSection.simulateClick()

            

        else:
            self.errorLabel.setText("Incorrect password")
            self.errorLabel.setHidden(False)
            self.forgotPasswordButton.setHidden(False)



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
    registerPage.usernameInput.setText(user)
    registerPage.passwordInput.setText(password)

    baseWindow.logInWidget.errorLabel.setHidden(True)

    # cycles to register widget
    baseWindow.stackedWidget.setCurrentIndex(1)



# ensures all inputs are correct before adding data to table and cycling to login page
def Register(self, baseWindow, user, fullName, email, password, rePassword):
    if len(user) == 0 or len(email) == 0 or len(fullName) == 0 or len(password) == 0 or len(rePassword) == 0:
        self.errorLabel.setText("Please ensure all fields are filled")
        self.errorLabel.setHidden(False)

    elif usernameValidation(user) == False:
        self.errorLabel.setText("Username between 5-16 characters. Allowed special characters: _, -, .")
        self.errorLabel.setHidden(False)

    elif emailValidation(email) == False:
        self.errorLabel.setText("Invalid email address")
        self.errorLabel.setHidden(False)

    elif passwordValidation(password) == False:
        self.errorLabel.setText("Ensure password is at least 5 characters")
        self.errorLabel.setHidden(False)
    
    elif doPasswordsMatch(password, rePassword) == False:
        self.errorLabel.setText("Passwords do not match")
        self.errorLabel.setHidden(False)

    elif isUnique("email", email) == False:
        self.errorLabel.setText("Email already taken")
        self.errorLabel.setHidden(False)

    elif isUnique("username", user) == False:
        self.errorLabel.setText("Username already taken")
        self.errorLabel.setHidden(False)

    else:
        self.errorLabel.setHidden(True)

        self.usernameInput.setText("")
        self.emailInput.setText("")
        self.fullNameInput.setText("")
        self.passwordInput.setText("")
        self.rePasswordInput.setText("")

        userData = {
            "username": user,
            "email": email,
            "fullName": fullName,
            "rating": 800,
            "puzzleRating": 800,
            "match1": -1,
            "match2": -1,
            "match3": -1,
            "theme": 0,
            "pieces": 0,
            "avatar": 0,
            "font": "Fira Code"
        }

        userId = insert("users", userData)

        hashedPassword = passwordHashing(password)

        passwordData = {
            "hash": hashedPassword,
            "id": userId
        }

        _ = insert("passwords", passwordData)

        baseWindow.stackedWidget.setCurrentIndex(0)



def goToForgotPasswordPage(baseWindow, user, forgotPasswordPage):
    # pre-populates some fields in the forgot password widget
    forgotPasswordPage.usernameInput.setText(user)

    # cycles to the correct widget
    baseWindow.stackedWidget.setCurrentIndex(2)


# goes through all validation steps before hashing and storing new password
def ResetPassword(self, baseWindow, user, email, password, rePassword):

    if len(user) == 0 or len(email) == 0 or len(password) == 0:
        self.errorLabel.setText("Please ensure all fields are filled")
        self.errorLabel.setHidden(False)

    elif doPasswordsMatch(password, rePassword) == False:
        self.errorLabel.setText("Passwords do not match")
        self.errorLabel.setHidden(False)

    else:
        data = getData("users", username = user, email = email)

        if len(data) == 0:
            self.errorLabel.setText("Invalid email or username")
            self.errorLabel.setHidden(False)

        else:
            self.errorLabel.setHidden(True)

            self.usernameInput.setText("")
            self.emailInput.setText("")
            self.passwordInput.setText("")
            self.rePasswordInput.setText("")

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
    


