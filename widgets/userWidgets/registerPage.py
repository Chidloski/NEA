from PyQt5 import QtCore, QtGui, QtWidgets
from widgets.userWidgets.functions.userFunctions import Register, PasswordVisibility
from widgets.labelClasses import AutoResizingLabel

# Responsible for setting up all elements within the log in page
class Ui_RegisterPage(QtWidgets.QWidget):

    def setupUi(self, stackedWidgetObject):

        # sizing of the widget
        self.setObjectName("registerPage")
        self.resize(100, 600)
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

        # declares the register label
        self.registerLabel = AutoResizingLabel(24, True, parent = self)
        self.registerLabel.setGeometry(QtCore.QRect(350, 160, 200, 51))

        # changes font size for label definition
        font.setPointSize(24)

        # defines the font of login label
        self.registerLabel.setFont(font)
        self.registerLabel.setObjectName("RegisterLabel")

        # Changes font for next declaration
        font.setPointSize(13)
        font.setBold(False)

        # declares username input box
        self.usernameInput = QtWidgets.QLineEdit(self)
        self.usernameInput.setGeometry(QtCore.QRect(350, 210, 300, 30))

        # defines the settings of the username input
        self.usernameInput.setFont(font)
        self.usernameInput.setText("")
        self.usernameInput.setPlaceholderText("Enter Username:")
        self.usernameInput.setObjectName("UsernameInput")

        # declares email input box
        self.emailInput = QtWidgets.QLineEdit(self)
        self.emailInput.setGeometry(QtCore.QRect(350, 253, 300, 30))

        # defines the settings of the email input
        self.emailInput.setFont(font)
        self.emailInput.setText("")
        self.emailInput.setPlaceholderText("Enter Email:")
        self.emailInput.setObjectName("EmailInput")

        # declares fullName input box
        self.fullNameInput = QtWidgets.QLineEdit(self)
        self.fullNameInput.setGeometry(QtCore.QRect(350, 296, 300, 30))

        # defines the settings of the email input
        self.fullNameInput.setFont(font)
        self.fullNameInput.setText("")
        self.fullNameInput.setPlaceholderText("Enter Full Name:")
        self.fullNameInput.setObjectName("FullNameInput")

        # declares password input box
        self.passwordInput = QtWidgets.QLineEdit(self)
        self.passwordInput.setGeometry(QtCore.QRect(350, 339, 300, 30))

        # defines the default settings of the password input box
        self.passwordInput.setFont(font)
        self.passwordInput.setText("")
        # echo mode states whether the input is shown as bullets or text
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInput.setPlaceholderText("Enter Password:")
        self.passwordInput.setObjectName("PasswordInput")

        # declares re-enter password input box
        self.rePasswordInput = QtWidgets.QLineEdit(self)
        self.rePasswordInput.setGeometry(QtCore.QRect(350, 382, 300, 30))

        # defines the default settings of the re-enter password input box
        self.rePasswordInput.setFont(font)
        self.rePasswordInput.setText("")
        # echo mode states whether the input is shown as bullets or text
        self.rePasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.rePasswordInput.setPlaceholderText("Re-enter Password:")
        self.rePasswordInput.setObjectName("RePasswordInput")

        # declares register button
        self.registerButton = QtWidgets.QPushButton(self)
        self.registerButton.setGeometry(QtCore.QRect(450, 421, 100, 32))

        font.setPointSize(14)
        font.setBold(True)

        self.registerButton.setFont(font)
        self.registerButton.setObjectName("RegisterButton")

        # calls register function which checks the input of username and password
        # passes in the self of the group window to allow access to the stacked widget
        self.registerButton.clicked.connect(lambda: Register(self, stackedWidgetObject, self.usernameInput.text(), self.fullNameInput.text(), self.emailInput.text(), self.passwordInput.text(), self.rePasswordInput.text()))

        # Changes font for next declaration
        font.setPointSize(13)
        font.setBold(False)

        # declares the error label
        self.errorLabel = AutoResizingLabel(13, False, parent = self, wordWrap = True)
        self.errorLabel.setGeometry(QtCore.QRect(350, 450, 300, 70))

        # defines the font of error label
        self.errorLabel.setFont(font)
        self.errorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.errorLabel.setObjectName("ErrorLabel")
        self.errorLabel.setHidden(True)
        self.errorLabel.setStyleSheet("color: rgb(175, 61, 50)")
        self.errorLabel.setWordWrap(True)

        # adds the "shut eye" icon to the button
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resources/UserIcons/hide.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)

        self.passwordVisibilityButton = QtWidgets.QPushButton(self)
        self.passwordVisibilityButton.setGeometry(QtCore.QRect(613, 339, 40, 26))
        self.passwordVisibilityButton.setText("")

        self.passwordVisibilityButton.setIcon(icon)
        self.passwordVisibilityButton.setIconSize(QtCore.QSize(23, 17))
        self.passwordVisibilityButton.setObjectName("passwordVisibilityButton")

        # calls function which either sets text to bullets or shows real text
        self.passwordVisibilityButton.clicked.connect(lambda: PasswordVisibility(self.passwordInput.displayText(), self.passwordInput.text(), self.passwordInput))

        self.rePasswordVisibilityButton = QtWidgets.QPushButton(self)
        self.rePasswordVisibilityButton.setGeometry(QtCore.QRect(613, 382, 40, 26))
        self.rePasswordVisibilityButton.setText("")

        self.rePasswordVisibilityButton.setIcon(icon)
        self.rePasswordVisibilityButton.setIconSize(QtCore.QSize(23, 17))
        self.rePasswordVisibilityButton.setObjectName("rePasswordVisibilityButton")

        # calls function which either sets text to bullets or shows real text
        self.rePasswordVisibilityButton.clicked.connect(lambda: PasswordVisibility(self.rePasswordInput.displayText(), self.rePasswordInput.text(), self.rePasswordInput))
        
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        
    
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.welcomeLabel.setText(_translate("registerPage", "Chess Teacher"))
        self.registerLabel.setText(_translate("registerPage", "Register:"))
        self.registerButton.setText(_translate("registerPage", "Register"))


    def resetUi(self):
        self.usernameInput.setText("")
        self.fullNameInput.setText("")
        self.emailInput.setText("")

        self.passwordInput.setText("")
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)

        self.rePasswordInput.setText("")
        self.rePasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)

        self.errorLabel.setHidden(True)
    