from PyQt5 import QtCore, QtGui, QtWidgets
from widgets.userWidgets.functions.userFunctions import Register, PasswordVisibility

# Responsible for setting up all elements within the log in page
class Ui_RegisterPage(QtWidgets.QWidget):

    def setupUi(self, stackedWidgetObject):

        # sizing of the widget
        self.setObjectName("registerPage")
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

        # declares the register label
        self.RegisterLabel = QtWidgets.QLabel(self)
        self.RegisterLabel.setGeometry(QtCore.QRect(350, 160, 200, 51))

        # changes font size for label definition
        font.setPointSize(24)

        # defines the font of login label
        self.RegisterLabel.setFont(font)
        self.RegisterLabel.setObjectName("RegisterLabel")

        # Changes font for next declaration
        font.setPointSize(13)
        font.setBold(False)

        # declares username input box
        self.UsernameInput = QtWidgets.QLineEdit(self)
        self.UsernameInput.setGeometry(QtCore.QRect(350, 210, 300, 30))

        # defines the settings of the username input
        self.UsernameInput.setFont(font)
        self.UsernameInput.setText("")
        self.UsernameInput.setPlaceholderText("Enter Username:")
        self.UsernameInput.setObjectName("UsernameInput")

        # declares email input box
        self.EmailInput = QtWidgets.QLineEdit(self)
        self.EmailInput.setGeometry(QtCore.QRect(350, 253, 300, 30))

        # defines the settings of the email input
        self.EmailInput.setFont(font)
        self.EmailInput.setText("")
        self.EmailInput.setPlaceholderText("Enter Email:")
        self.EmailInput.setObjectName("EmailInput")

        # declares fullName input box
        self.FullNameInput = QtWidgets.QLineEdit(self)
        self.FullNameInput.setGeometry(QtCore.QRect(350, 296, 300, 30))

        # defines the settings of the email input
        self.FullNameInput.setFont(font)
        self.FullNameInput.setText("")
        self.FullNameInput.setPlaceholderText("Enter Full Name:")
        self.FullNameInput.setObjectName("FullNameInput")

        # declares password input box
        self.PasswordInput = QtWidgets.QLineEdit(self)
        self.PasswordInput.setGeometry(QtCore.QRect(350, 339, 300, 30))

        # defines the default settings of the password input box
        self.PasswordInput.setFont(font)
        self.PasswordInput.setText("")
        # echo mode states whether the input is shown as bullets or text
        self.PasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordInput.setPlaceholderText("Enter Password:")
        self.PasswordInput.setObjectName("PasswordInput")

        # declares re-enter password input box
        self.RePasswordInput = QtWidgets.QLineEdit(self)
        self.RePasswordInput.setGeometry(QtCore.QRect(350, 382, 300, 30))

        # defines the default settings of the re-enter password input box
        self.RePasswordInput.setFont(font)
        self.RePasswordInput.setText("")
        # echo mode states whether the input is shown as bullets or text
        self.RePasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.RePasswordInput.setPlaceholderText("Re-enter Password:")
        self.RePasswordInput.setObjectName("RePasswordInput")

        # declares register button
        self.RegisterButton = QtWidgets.QPushButton(self)
        self.RegisterButton.setGeometry(QtCore.QRect(450, 421, 100, 32))

        font.setPointSize(14)
        font.setBold(True)

        self.RegisterButton.setFont(font)
        self.RegisterButton.setObjectName("RegisterButton")

        # calls register function which checks the input of username and password
        # passes in the self of the group window to allow access to the stacked widget
        self.RegisterButton.clicked.connect(lambda: Register(self, stackedWidgetObject, self.UsernameInput.text(), self.FullNameInput.text(), self.EmailInput.text(), self.PasswordInput.text(), self.RePasswordInput.text()))

        # Changes font for next declaration
        font.setPointSize(13)
        font.setBold(False)

        # declares the error label
        self.ErrorLabel = QtWidgets.QLabel(self)
        self.ErrorLabel.setGeometry(QtCore.QRect(350, 450, 300, 50))

        # defines the font of error label
        self.ErrorLabel.setFont(font)
        self.ErrorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ErrorLabel.setObjectName("ErrorLabel")
        self.ErrorLabel.setHidden(True)
        self.ErrorLabel.setStyleSheet("color: rgb(175, 61, 50)")

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
        self.passwordVisibilityButton.clicked.connect(lambda: PasswordVisibility(self.PasswordInput.displayText(), self.PasswordInput.text(), self.PasswordInput))

        self.rePasswordVisibilityButton = QtWidgets.QPushButton(self)
        self.rePasswordVisibilityButton.setGeometry(QtCore.QRect(613, 382, 40, 26))
        self.rePasswordVisibilityButton.setText("")

        self.rePasswordVisibilityButton.setIcon(icon)
        self.rePasswordVisibilityButton.setIconSize(QtCore.QSize(23, 17))
        self.rePasswordVisibilityButton.setObjectName("rePasswordVisibilityButton")

        # calls function which either sets text to bullets or shows real text
        self.rePasswordVisibilityButton.clicked.connect(lambda: PasswordVisibility(self.RePasswordInput.displayText(), self.RePasswordInput.text(), self.RePasswordInput))
        
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        
    
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.WelcomeLabel.setText(_translate("registerPage", "Chess Teacher"))
        self.RegisterLabel.setText(_translate("registerPage", "Register:"))
        self.RegisterButton.setText(_translate("registerPage", "Register"))
    