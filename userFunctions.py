from PyQt5 import QtCore, QtGui, QtWidgets

def LogIn(self, user, password, outputButton):
    # in the future this function can be used to compare user and password to database
    # encrypted database??

    if (user == "sam" and password == "chidlow"):
        self.stackedWidget.setCurrentIndex(1)
    else:
        outputButton.setText("Log in Fail")

def PasswordVisibility(self, displayText, actualText, target):
# function alternates the display of the password input from bullets to plaintext 

    if (displayText == actualText):
        # handles when echo mode = normal
        target.setEchoMode(QtWidgets.QLineEdit().Password)
    else:
        # handles when echo mode = password
        target.setEchoMode(QtWidgets.QLineEdit().Normal)

    



