from PyQt5 import QtCore, QtGui, QtWidgets
from widgets.utilityWidgets.functions.playFunctions import *

# Responsible for setting up all elements within the log in page
class Ui_PlayStage1(QtWidgets.QWidget):

    def setupUi(self, dashboard, baseWindow):

        self.opponentUser = False

        # sizing of the widget
        self.setObjectName("playStage1Page")
        self.resize(230, 560)
        self.setAutoFillBackground(False)

        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(24)
        font.setBold(True)

        self.PvPLabel = QtWidgets.QLabel(self)
        self.PvPLabel.setGeometry(QtCore.QRect(10, 10, 201, 20))
        
        self.PvPLabel.setFont(font)
        self.PvPLabel.setObjectName("PvPLabel")

        font.setPointSize(15)
        font.setBold(False)

        self.currentUserLabel = QtWidgets.QLabel(self)
        self.currentUserLabel.setGeometry(QtCore.QRect(10, 40, 201, 16))
        self.currentUserLabel.setFont(font)
        self.currentUserLabel.setObjectName("currentUserLabel")

        font.setPointSize(13)

        self.currentUserRatingLabel = QtWidgets.QLabel(self)
        self.currentUserRatingLabel.setGeometry(QtCore.QRect(20, 60, 191, 16))
        self.currentUserRatingLabel.setFont(font)
        self.currentUserRatingLabel.setObjectName("currentUserRatingLabel")

        font.setPointSize(15)

        self.opponentLabel = QtWidgets.QLabel(self)
        self.opponentLabel.setGeometry(QtCore.QRect(10, 90, 201, 16))
        self.opponentLabel.setFont(font)
        self.opponentLabel.setObjectName("opponentLabel")

        font.setPointSize(13)

        self.guestRadioButton = QtWidgets.QRadioButton(self)
        self.guestRadioButton.setGeometry(QtCore.QRect(20, 110, 191, 16))
        self.guestRadioButton.setIconSize(QtCore.QSize(12, 12))
        self.guestRadioButton.setObjectName("guestRadioButton")
        self.guestRadioButton.setFont(font)

        self.secondaryUserRadioButton = QtWidgets.QRadioButton(self)
        self.secondaryUserRadioButton.setGeometry(QtCore.QRect(20, 130, 191, 16))
        self.secondaryUserRadioButton.setIconSize(QtCore.QSize(12, 12))
        self.secondaryUserRadioButton.setObjectName("secondaryUserRadioButton")
        self.secondaryUserRadioButton.setFont(font)

        self.userTypeGroup = QtWidgets.QButtonGroup(self)
        self.userTypeGroup.addButton(self.guestRadioButton)
        self.userTypeGroup.addButton(self.secondaryUserRadioButton)

        font.setPointSize(12)

        self.secondaryUsernameInput = QtWidgets.QLineEdit(self)
        self.secondaryUsernameInput.setGeometry(QtCore.QRect(30, 160, 161, 21))
        self.secondaryUsernameInput.setFont(font)
        self.secondaryUsernameInput.setObjectName("secondaryUsernameInput")

        self.secondaryPasswordInput = QtWidgets.QLineEdit(self)
        self.secondaryPasswordInput.setGeometry(QtCore.QRect(30, 180, 161, 21))
        self.secondaryPasswordInput.setFont(font)
        self.secondaryPasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.secondaryPasswordInput.setObjectName("secondaryPasswordInput")

        font.setPointSize(13)

        self.secondaryUserLabel = QtWidgets.QLabel(self)
        self.secondaryUserLabel.setGeometry(QtCore.QRect(20, 160, 161, 21))
        self.secondaryUserLabel.setObjectName("secondaryUserLabel")
        self.secondaryUserLabel.setFont(font)
        self.secondaryUserLabel.setText("")
        self.secondaryUserLabel.setHidden(True)

        self.secondaryUserRatingLabel = QtWidgets.QLabel(self)
        self.secondaryUserRatingLabel.setGeometry(QtCore.QRect(30, 180, 161, 21))
        self.secondaryUserRatingLabel.setObjectName("secondaryUserLabel")
        self.secondaryUserRatingLabel.setFont(font)
        self.secondaryUserRatingLabel.setText("")
        self.secondaryUserRatingLabel.setHidden(True)

        self.loginButton = QtWidgets.QPushButton(self)
        self.loginButton.setGeometry(QtCore.QRect(60, 200, 100, 32))
        self.loginButton.setFont(font)
        self.loginButton.setObjectName("loginButton")

        self.loginButton.clicked.connect(lambda: secondaryLogIn(self, self.secondaryUsernameInput.text(), self.secondaryPasswordInput.text(), self.opponentUser, baseWindow))

        font.setPointSize(18)
        font.setBold(True)

        self.playButton = QtWidgets.QPushButton(self)
        self.playButton.setGeometry(QtCore.QRect(9, 250, 201, 41))
        self.playButton.setFont(font)
        self.playButton.setAutoDefault(False)
        self.playButton.setDefault(False)
        self.playButton.setFlat(False)
        self.playButton.setObjectName("playButton")

        self.playButton.clicked.connect(lambda: Play(baseWindow, dashboard, self, self.userTypeGroup.checkedButton(), self.opponentUser))

        font.setPointSize(24)

        self.tournamentLabel = QtWidgets.QLabel(self)
        self.tournamentLabel.setGeometry(QtCore.QRect(10, 320, 201, 20))
        self.tournamentLabel.setFont(font)
        self.tournamentLabel.setObjectName("tournamentLabel")

        font.setPointSize(13)
        font.setBold(False)

        self.roundRadioButton = QtWidgets.QRadioButton(self)
        self.roundRadioButton.setGeometry(QtCore.QRect(20, 350, 191, 16))
        self.roundRadioButton.setIconSize(QtCore.QSize(12, 12))
        self.roundRadioButton.setObjectName("roundRadioButton")
        self.roundRadioButton.setFont(font)

        self.knockoutRadioButton = QtWidgets.QRadioButton(self)
        self.knockoutRadioButton.setGeometry(QtCore.QRect(20, 370, 191, 16))
        self.knockoutRadioButton.setIconSize(QtCore.QSize(12, 12))
        self.knockoutRadioButton.setObjectName("knockoutRadioButton")
        self.knockoutRadioButton.setFont(font)

        self.tournamentTypeGroup = QtWidgets.QButtonGroup(self)
        self.tournamentTypeGroup.addButton(self.roundRadioButton)
        self.tournamentTypeGroup.addButton(self.knockoutRadioButton)

        font.setPointSize(12)

        self.numberOfPlayersInput = QtWidgets.QLineEdit(self)
        self.numberOfPlayersInput.setGeometry(QtCore.QRect(30, 400, 161, 21))
        self.numberOfPlayersInput.setFont(font)
        self.numberOfPlayersInput.setObjectName("numberOfPlayersInput")

        font.setPointSize(18)
        font.setBold(True)

        self.createButton = QtWidgets.QPushButton(self)
        self.createButton.setGeometry(QtCore.QRect(10, 440, 201, 41))
        self.createButton.setFont(font)
        self.createButton.setAutoDefault(False)
        self.createButton.setDefault(False)
        self.createButton.setFlat(False)
        self.createButton.setObjectName("createButton")

        font.setPointSize(12)
        font.setBold(False)

        self.errorLabel = QtWidgets.QLabel(self)
        self.errorLabel.setGeometry(QtCore.QRect(10, 230, 201, 16))
        self.errorLabel.setFont(font)
        self.errorLabel.setStyleSheet("color: rgb(175, 61, 50)")
        self.errorLabel.setText("")
        self.errorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.errorLabel.setObjectName("errorLabel")

        self.tournamentErrorLabel = QtWidgets.QLabel(self)
        self.tournamentErrorLabel.setGeometry(QtCore.QRect(10, 420, 201, 16))
        self.tournamentErrorLabel.setFont(font)
        self.tournamentErrorLabel.setStyleSheet("color: rgb(175, 61, 50)")
        self.tournamentErrorLabel.setText("")
        self.tournamentErrorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tournamentErrorLabel.setObjectName("tournamentErrorLabel")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.clearFocus()


    # ensures no radio button is stuck with the focus ring
    def clearFocus(self):
        self.guestRadioButton.clearFocus()
        self.secondaryUserRadioButton.clearFocus()
        self.roundRadioButton.clearFocus()
        self.knockoutRadioButton.clearFocus()

        self.guestRadioButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.secondaryUserRadioButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.roundRadioButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.knockoutRadioButton.setFocusPolicy(QtCore.Qt.NoFocus)

    def refreshRadioButtons(self):
        # Temporarily disable mutual exclusivity
        self.guestRadioButton.setAutoExclusive(False)
        self.secondaryUserRadioButton.setAutoExclusive(False)
        self.roundRadioButton.setAutoExclusive(False)
        self.knockoutRadioButton.setAutoExclusive(False)

        # Uncheck all radio buttons
        self.guestRadioButton.setChecked(False)
        self.secondaryUserRadioButton.setChecked(False)
        self.roundRadioButton.setChecked(False)
        self.knockoutRadioButton.setChecked(False)

        # Re-enable mutual exclusivity
        self.guestRadioButton.setAutoExclusive(True)
        self.secondaryUserRadioButton.setAutoExclusive(True)
        self.roundRadioButton.setAutoExclusive(True)
        self.knockoutRadioButton.setAutoExclusive(True)

    def populate(widget, userId):

        query = {"id": userId}

        data = getData("users", **query)

        data = data[0]

        widget.currentUserLabel.setText(data["username"])
        widget.currentUserRatingLabel.setText("Rating: " + str(data["rating"]))



    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.PvPLabel.setText(_translate("playStage1Page", "PvP"))
        self.currentUserLabel.setText(_translate("playStage1Page", "Current User"))
        self.currentUserRatingLabel.setText(_translate("playStage1Page", "Rating: 1000"))
        self.opponentLabel.setText(_translate("playStage1Page", "Opponent"))
        self.guestRadioButton.setText(_translate("playStage1Page", "Guest"))
        self.secondaryUserRadioButton.setText(_translate("playStage1Page", "Secondary User"))
        self.secondaryUsernameInput.setPlaceholderText(_translate("playStage1Page", "Username:"))
        self.secondaryPasswordInput.setPlaceholderText(_translate("playStage1Page", "Password:"))
        self.loginButton.setText(_translate("playStage1Page", "Log In"))
        self.playButton.setText(_translate("playStage1Page", "Play"))
        self.tournamentLabel.setText(_translate("playStage1Page", "Tournament"))
        self.roundRadioButton.setText(_translate("playStage1Page", "Round-Robin"))
        self.knockoutRadioButton.setText(_translate("playStage1Page", "Knockout"))
        self.numberOfPlayersInput.setPlaceholderText(_translate("playStage1Page", "Num of Players:"))
        self.createButton.setText(_translate("playStage1Page", "Create"))
