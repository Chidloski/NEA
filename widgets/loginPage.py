from PyQt5 import QtCore, QtGui, QtWidgets
from userFunctions import LogIn, PasswordVisibility, goToRegisterPage, goToForgotPasswordPage

# Responsible for setting up all elements within the log in page
class Ui_LogInPage(QtWidgets.QWidget):

    def setupUi(self, stackedWidgetObject, registerWidgetObject, forgotPasswordWidgetObject):

        # sizing of the widget
        self.setObjectName("logInPage")
        self.resize(100, 600)
        self.setAutoFillBackground(False)

        # declares welcome label element
        self.WelcomeLabel = QtWidgets.QLabel(self)
        self.WelcomeLabel.setGeometry(QtCore.QRect(200, 50, 600, 120))

        # sets font
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(70)
        font.setBold(True)

        # populates the welcome label element
        self.WelcomeLabel.setFont(font)
        self.WelcomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.WelcomeLabel.setObjectName("WelcomeLabel")

        # declares the login button
        self.LoginLabel = QtWidgets.QLabel(self)
        self.LoginLabel.setGeometry(QtCore.QRect(350, 160, 101, 51))

        # changes font size for label definition
        font.setPointSize(24)

        # defines the font of login label
        self.LoginLabel.setFont(font)
        self.LoginLabel.setObjectName("LoginLabel")

        # declares username input box
        self.UsernameInput = QtWidgets.QLineEdit(self)
        self.UsernameInput.setGeometry(QtCore.QRect(350, 210, 300, 30))

        # Changes font for next declaration
        font.setPointSize(13)
        font.setBold(False)

        # defines the settings of the username input
        self.UsernameInput.setFont(font)
        self.UsernameInput.setText("")
        self.UsernameInput.setPlaceholderText("Enter Username:")
        self.UsernameInput.setObjectName("UsernameInput")

        # declares password input box
        self.PasswordInput = QtWidgets.QLineEdit(self)
        self.PasswordInput.setGeometry(QtCore.QRect(350, 253, 300, 30))

        # changes font
        font.setPointSize(13)

        # defines the default settings of the password input box
        self.PasswordInput.setFont(font)
        self.PasswordInput.setText("")
        # echo mode states whether the input is shown as bullets or text
        self.PasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordInput.setPlaceholderText("Enter Password:")
        self.PasswordInput.setObjectName("PasswordInput")

        font.setPointSize(14)
        font.setBold(True)

        # declares log in button
        self.LoginButton = QtWidgets.QPushButton(self)
        self.LoginButton.setGeometry(QtCore.QRect(425, 292, 150, 32))

        self.LoginButton.setFont(font)
        self.LoginButton.setObjectName("LoginButton")

        # calls log in function which checks the input of username and password
        # passes in the base window to allow access to the stacked widget
        self.LoginButton.clicked.connect(lambda: LogIn(self, stackedWidgetObject, self.UsernameInput.text(), self.PasswordInput.text()))

        # declares createUser button
        self.CreateUserButton = QtWidgets.QPushButton(self)
        self.CreateUserButton.setGeometry(QtCore.QRect(425, 324, 150, 32))

        self.CreateUserButton.setFont(font)
        self.CreateUserButton.setObjectName("LoginButton")

        # calls go to register page function which passes username and input to new page
        # passes in the base window to allow access to the stacked widget
        self.CreateUserButton.clicked.connect(lambda: goToRegisterPage(stackedWidgetObject, self.UsernameInput.text(), self.PasswordInput.text(), registerWidgetObject))

        # declares forgotPassword button
        self.ForgotPasswordButton = QtWidgets.QPushButton(self)
        self.ForgotPasswordButton.setGeometry(QtCore.QRect(425, 356, 150, 32))

        self.ForgotPasswordButton.setFont(font)
        self.ForgotPasswordButton.setObjectName("LoginButton")

        # button is initially hidden
        self.ForgotPasswordButton.setHidden(True)

        # calls log in function which checks the input of username and password
        # passes in the self of the group window to allow access to the stacked widget
        self.ForgotPasswordButton.clicked.connect(lambda: goToForgotPasswordPage(stackedWidgetObject, self.UsernameInput.text(), forgotPasswordWidgetObject))

        # Changes font for next declaration
        font.setPointSize(13)
        font.setBold(False)

        # declares the error label
        self.ErrorLabel = QtWidgets.QLabel(self)
        self.ErrorLabel.setGeometry(QtCore.QRect(350, 395, 300, 50))

        # defines the font of error label
        self.ErrorLabel.setFont(font)
        self.ErrorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ErrorLabel.setObjectName("ErrorLabel")
        self.ErrorLabel.setHidden(True)
        self.ErrorLabel.setStyleSheet("color: rgb(175, 61, 50)")

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
        self.passwordVisibilityButton.clicked.connect(lambda: PasswordVisibility(self.PasswordInput.displayText(), self.PasswordInput.text(), self.PasswordInput))
        
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        
    
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.WelcomeLabel.setText(_translate("logInPage", "Chess Teacher"))
        self.LoginLabel.setText(_translate("logInPage", "Login:"))
        self.LoginButton.setText(_translate("logInPage", "Login"))
        self.CreateUserButton.setText(_translate("logInPage", "Create User"))
        self.ForgotPasswordButton.setText(_translate("logInPage", "Reset Password"))
    