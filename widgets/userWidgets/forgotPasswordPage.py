from PyQt5 import QtCore, QtGui, QtWidgets
from widgets.userWidgets.functions.userFunctions import ResetPassword, PasswordVisibility
from widgets.labelClasses import AutoResizingLabel

# Responsible for setting up all elements within the log in page
class Ui_ForgotPasswordPage(QtWidgets.QWidget):

    def setupUi(self, stackedWidgetObject):

        # sizing of the widget
        self.setObjectName("forgotPasswordPage")
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

        # declares the reset password button
        self.resetPasswordLabel = AutoResizingLabel(24, True, parent = self)
        self.resetPasswordLabel.setGeometry(QtCore.QRect(350, 160, 220, 51))

        # changes font size for label definition
        font.setPointSize(24)

        # defines the font of reset password label
        self.resetPasswordLabel.setFont(font)
        self.resetPasswordLabel.setObjectName("ResetPasswordLabel")

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

        # declares password input box
        self.passwordInput = QtWidgets.QLineEdit(self)
        self.passwordInput.setGeometry(QtCore.QRect(350, 296, 300, 30))

        # defines the default settings of the password input box
        self.passwordInput.setFont(font)
        self.passwordInput.setText("")
        # echo mode states whether the input is shown as bullets or text
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInput.setPlaceholderText("Enter Password:")
        self.passwordInput.setObjectName("PasswordInput")

        # declares re-enter password input box
        self.rePasswordInput = QtWidgets.QLineEdit(self)
        self.rePasswordInput.setGeometry(QtCore.QRect(350, 339, 300, 30))

        # defines the default settings of the re-enter password input box
        self.rePasswordInput.setFont(font)
        self.rePasswordInput.setText("")
        # echo mode states whether the input is shown as bullets or text
        self.rePasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.rePasswordInput.setPlaceholderText("Re-enter Password:")
        self.rePasswordInput.setObjectName("RePasswordInput")

        # declares reset password button
        self.resetPasswordButton = QtWidgets.QPushButton(self)
        self.resetPasswordButton.setGeometry(QtCore.QRect(450, 378, 100, 32))

        font.setPointSize(14)
        font.setBold(True)

        self.resetPasswordButton.setFont(font)
        self.resetPasswordButton.setObjectName("ResetPasswordButton")

        # calls log in function which checks the input of username and password
        # passes in the self of the group window to allow access to the stacked widget
        self.resetPasswordButton.clicked.connect(lambda: ResetPassword(self, stackedWidgetObject, self.usernameInput.text(), self.emailInput.text(), self.passwordInput.text(), self.rePasswordInput.text()))

        # Changes font for next declaration
        font.setPointSize(13)
        font.setBold(False)

        # declares the error label
        self.errorLabel = AutoResizingLabel(13, False, parent = self, wordWrap = True)
        self.errorLabel.setGeometry(QtCore.QRect(350, 407, 300, 70))

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
        self.passwordVisibilityButton.setGeometry(QtCore.QRect(613, 296, 40, 26))
        self.passwordVisibilityButton.setText("")

        self.passwordVisibilityButton.setIcon(icon)
        self.passwordVisibilityButton.setIconSize(QtCore.QSize(23, 17))
        self.passwordVisibilityButton.setObjectName("passwordVisibilityButton")

        # calls function which either sets text to bullets or shows real text
        self.passwordVisibilityButton.clicked.connect(lambda: PasswordVisibility(self.passwordInput.displayText(), self.passwordInput.text(), self.passwordInput))

        self.rePasswordVisibilityButton = QtWidgets.QPushButton(self)
        self.rePasswordVisibilityButton.setGeometry(QtCore.QRect(613, 339, 40, 26))
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
        self.welcomeLabel.setText(_translate("forgotPasswordPage", "Chess Teacher"))
        self.resetPasswordLabel.setText(_translate("forgotPasswordPage", "Reset Password:"))
        self.resetPasswordButton.setText(_translate("forgotPasswordPage", "Reset"))


    def resetUi(self):
        self.usernameInput.setText("")
        self.emailInput.setText("")

        self.passwordInput.setText("")
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)

        self.rePasswordInput.setText("")
        self.rePasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)

        self.errorLabel.setHidden(True)
    