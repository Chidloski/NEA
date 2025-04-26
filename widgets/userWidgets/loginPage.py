from PyQt5 import QtCore, QtGui, QtWidgets
from widgets.userWidgets.functions.userFunctions import LogIn, PasswordVisibility, goToRegisterPage, goToForgotPasswordPage
from widgets.labelClasses import AutoResizingLabel

# Responsible for setting up all elements within the log in page
class Ui_LogInPage(QtWidgets.QWidget):

    def setupUi(self, stackedWidgetObject, registerWidgetObject, forgotPasswordWidgetObject):

        # sizing of the widget
        self.setObjectName("logInPage")
        self.resize(1000, 600)
        self.setAutoFillBackground(False)

        # declares welcome label element
        self.welcomeLabel = AutoResizingLabel(70, True, parent = self)
        self.welcomeLabel.setGeometry(QtCore.QRect(200, 50, 600, 120))

        # sets font
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(70)
        font.setBold(True)

        # populates the welcome label element
        self.welcomeLabel.setFont(font)
        self.welcomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.welcomeLabel.setObjectName("WelcomeLabel")

        # declares the login button
        self.loginLabel = AutoResizingLabel(24, True, parent = self)
        self.loginLabel.setGeometry(QtCore.QRect(350, 160, 101, 51))

        # changes font size for label definition
        font.setPointSize(24)

        # defines the font of login label
        self.loginLabel.setFont(font)
        self.loginLabel.setObjectName("LoginLabel")

        # declares username input box
        self.usernameInput = QtWidgets.QLineEdit(self)
        self.usernameInput.setGeometry(QtCore.QRect(350, 210, 300, 30))

        # Changes font for next declaration
        font.setPointSize(13)
        font.setBold(False)

        # defines the settings of the username input
        self.usernameInput.setFont(font)
        self.usernameInput.setText("")
        self.usernameInput.setPlaceholderText("Enter Username:")
        self.usernameInput.setObjectName("UsernameInput")

        # declares password input box
        self.passwordInput = QtWidgets.QLineEdit(self)
        self.passwordInput.setGeometry(QtCore.QRect(350, 253, 300, 30))

        # changes font
        font.setPointSize(13)

        # defines the default settings of the password input box
        self.passwordInput.setFont(font)
        self.passwordInput.setText("")
        # echo mode states whether the input is shown as bullets or text
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInput.setPlaceholderText("Enter Password:")
        self.passwordInput.setObjectName("PasswordInput")

        font.setPointSize(14)
        font.setBold(True)

        # declares log in button
        self.loginButton = QtWidgets.QPushButton(self)
        self.loginButton.setGeometry(QtCore.QRect(425, 292, 150, 32))

        self.loginButton.setFont(font)
        self.loginButton.setObjectName("LoginButton")

        # calls log in function which checks the input of username and password
        # passes in the base window to allow access to the stacked widget
        self.loginButton.clicked.connect(lambda: LogIn(self, stackedWidgetObject, self.usernameInput.text(), self.passwordInput.text()))

        # declares createUser button
        self.createUserButton = QtWidgets.QPushButton(self)
        self.createUserButton.setGeometry(QtCore.QRect(425, 324, 150, 32))

        self.createUserButton.setFont(font)
        self.createUserButton.setObjectName("LoginButton")

        # calls go to register page function which passes username and input to new page
        # passes in the base window to allow access to the stacked widget
        self.createUserButton.clicked.connect(lambda: goToRegisterPage(stackedWidgetObject, self.usernameInput.text(), self.passwordInput.text(), registerWidgetObject))

        # declares forgotPassword button
        self.forgotPasswordButton = QtWidgets.QPushButton(self)
        self.forgotPasswordButton.setGeometry(QtCore.QRect(425, 356, 150, 32))

        self.forgotPasswordButton.setFont(font)
        self.forgotPasswordButton.setObjectName("LoginButton")

        # button is initially hidden
        self.forgotPasswordButton.setHidden(True)

        # calls log in function which checks the input of username and password
        # passes in the self of the group window to allow access to the stacked widget
        self.forgotPasswordButton.clicked.connect(lambda: goToForgotPasswordPage(stackedWidgetObject, self.usernameInput.text(), forgotPasswordWidgetObject))

        # Changes font for next declaration
        font.setPointSize(13)
        font.setBold(False)

        # declares the error label
        self.errorLabel = AutoResizingLabel(13, False, parent = self, wordWrap = True)
        self.errorLabel.setGeometry(QtCore.QRect(350, 395, 300, 70))

        # defines the font of error label
        self.errorLabel.setFont(font)
        self.errorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.errorLabel.setObjectName("ErrorLabel")
        self.errorLabel.setHidden(True)
        self.errorLabel.setStyleSheet("color: rgb(175, 61, 50)")
        self.errorLabel.setWordWrap(True)

        self.passwordVisibilityButton = QtWidgets.QPushButton(self)
        self.passwordVisibilityButton.setGeometry(QtCore.QRect(613, 253, 40, 26))
        self.passwordVisibilityButton.setText("")

        # adds the "shut eye" icon to the button
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resources/UserIcons/hide.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)

        self.passwordVisibilityButton.setIcon(icon)
        self.passwordVisibilityButton.setIconSize(QtCore.QSize(23, 17))
        self.passwordVisibilityButton.setObjectName("passwordVisibilityButton")

        # calls function which either sets text to bullets or shows real text
        self.passwordVisibilityButton.clicked.connect(lambda: PasswordVisibility(self.passwordInput.displayText(), self.passwordInput.text(), self.passwordInput))
        
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        
    
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.welcomeLabel.setText(_translate("logInPage", "Chess Teacher"))
        self.loginLabel.setText(_translate("logInPage", "Login:"))
        self.loginButton.setText(_translate("logInPage", "Login"))
        self.createUserButton.setText(_translate("logInPage", "Create User"))
        self.forgotPasswordButton.setText(_translate("logInPage", "Reset Password"))


    def resetUi(self):
        self.usernameInput.setText("")

        self.passwordInput.setText("")
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)

        self.forgotPasswordButton.setHidden(True)

        self.errorLabel.setHidden(True)
    