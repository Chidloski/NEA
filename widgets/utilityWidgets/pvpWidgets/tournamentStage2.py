from PyQt5 import QtCore, QtGui, QtWidgets
from widgets.utilityWidgets.functions.tournamentFunctions import tournamentSecondaryLogIn, goToStage1FromTournaments, goToTournamentStage3
from widgets.labelClasses import AutoResizingLabel

# makes a clickable label
class clickableLabel(QtWidgets.QLabel):

    # adds click functionality to QLabel
    clicked = QtCore.pyqtSignal(str)

    # initialises the QLabel parent
    def __init__(self, *args, **kwargs):
        QtWidgets.QLabel.__init__(self, *args, **kwargs)

    def mousePressEvent(self, event):
        # after each mouse press event, clickstate changes to clicked
        self.clickState = "Clicked"

    def mouseReleaseEvent(self, event):
            self.clicked.emit(self.clickState)


class Ui_TournamentStage2(QtWidgets.QWidget):

    def setupUi(self, dashboard, baseWindow):
        
        # holds the size of the tournament
        self.capacity = 0

        # holds the current player being logged in
        self.index = 0

        self.tournamentType = ""

        # sizing of the widget
        self.setObjectName("tournamentStage2Page")
        self.resize(230, 560)
        self.setAutoFillBackground(False)

        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(24)
        font.setBold(True)

        self.titleLabel = AutoResizingLabel(24, True, parent = self)
        self.titleLabel.setGeometry(QtCore.QRect(10, 10, 201, 31))
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")

        font.setPointSize(18)
        font.setBold(True)

        self.playerLogInLabel = AutoResizingLabel(18, True, parent = self)
        self.playerLogInLabel.setGeometry(QtCore.QRect(30, 300, 161, 31))
        self.playerLogInLabel.setFont(font)
        self.playerLogInLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.playerLogInLabel.setObjectName("playerLogInLabel")

        font.setPointSize(12)
        font.setBold(False)

        self.guestRadioButton = QtWidgets.QRadioButton(self)
        self.guestRadioButton.setGeometry(QtCore.QRect(20, 330, 181, 20))
        self.guestRadioButton.setFont(font)
        self.guestRadioButton.setObjectName("guestRadioButton")
        self.guestRadioButton.toggled.connect(lambda: self.switchInputs(1))

        self.secondaryUserRadioButton = QtWidgets.QRadioButton(self)
        self.secondaryUserRadioButton.setGeometry(QtCore.QRect(20, 350, 181, 20))
        self.secondaryUserRadioButton.setFont(font)
        self.secondaryUserRadioButton.setObjectName("secondaryUserButton")
        self.secondaryUserRadioButton.toggled.connect(lambda: self.switchInputs(0))

        self.userTypeGroup = QtWidgets.QButtonGroup(self)
        self.userTypeGroup.addButton(self.guestRadioButton)
        self.userTypeGroup.addButton(self.secondaryUserRadioButton)

        font.setPointSize(18)
        font.setBold(True)

        self.cycleRightButton = clickableLabel(self)
        self.cycleRightButton.setGeometry(QtCore.QRect(190, 300, 31, 31))
        self.cycleRightButton.setFont(font)
        self.cycleRightButton.setAlignment(QtCore.Qt.AlignCenter)
        self.cycleRightButton.setObjectName("cycleRightButton")
        self.cycleRightButton.clicked.connect(lambda: self.cycleUser(1))

        self.cycleLeftButton = clickableLabel(self)
        self.cycleLeftButton.setGeometry(QtCore.QRect(0, 300, 31, 31))
        self.cycleLeftButton.setFont(font)
        self.cycleLeftButton.setAlignment(QtCore.Qt.AlignCenter)
        self.cycleLeftButton.setObjectName("cycleLeftButton")
        self.cycleLeftButton.clicked.connect(lambda: self.cycleUser(-1))

        font.setPointSize(12)
        font.setBold(False)

        self.usernameInput = QtWidgets.QLineEdit(self)
        self.usernameInput.setGeometry(QtCore.QRect(20, 380, 181, 21))
        self.usernameInput.setFont(font)
        self.usernameInput.setObjectName("usernameInput")

        self.passwordInput = QtWidgets.QLineEdit(self)
        self.passwordInput.setGeometry(QtCore.QRect(20, 400, 181, 21))
        self.passwordInput.setFont(font)
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInput.setObjectName("passwordInput")

        self.guestNameInput = QtWidgets.QLineEdit(self)
        self.guestNameInput.setGeometry(QtCore.QRect(20, 380, 181, 21))
        self.guestNameInput.setFont(font)
        self.guestNameInput.setObjectName("guestNameInput")
        self.guestNameInput.setHidden(True)

        font.setPointSize(15)

        self.userTypeLabel = AutoResizingLabel(15, False, parent = self)
        self.userTypeLabel.setGeometry(QtCore.QRect(20, 350, 181, 31))
        self.userTypeLabel.setFont(font)
        self.userTypeLabel.setObjectName("userTypeLabel")
        self.userTypeLabel.setHidden(True)

        self.userLabel = AutoResizingLabel(15, False, parent = self)
        self.userLabel.setGeometry(QtCore.QRect(30, 385, 171, 31))
        self.userLabel.setFont(font)
        self.userLabel.setObjectName("userLabel")
        self.userLabel.setHidden(True)

        font.setPointSize(12)

        self.logInButton = QtWidgets.QPushButton(self)
        self.logInButton.setGeometry(QtCore.QRect(60, 420, 100, 32))
        self.logInButton.setFont(font)
        self.logInButton.setObjectName("logInButton")
        self.logInButton.clicked.connect(lambda: tournamentSecondaryLogIn(self, self.index))

        self.errorLabel = AutoResizingLabel(12, False, parent = self)
        self.errorLabel.setGeometry(QtCore.QRect(10, 450, 201, 16))
        self.errorLabel.setFont(font)
        self.errorLabel.setStyleSheet("color: rgb(175, 61, 50)")
        self.errorLabel.setText("")
        self.errorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.errorLabel.setObjectName("errorLabel")
        self.errorLabel.setHidden(True)

        font.setPointSize(18)
        font.setBold(True)

        self.playButton = QtWidgets.QPushButton(self)
        self.playButton.setGeometry(QtCore.QRect(10, 470, 201, 41))
        self.playButton.setFont(font)
        self.playButton.setObjectName("playButton")
        self.playButton.clicked.connect(lambda: goToTournamentStage3(dashboard, self.tournamentType, self.userDetails, self.capacity))

        self.backButton = QtWidgets.QPushButton(self)
        self.backButton.setGeometry(QtCore.QRect(10, 510, 201, 41))
        self.backButton.setFont(font)
        self.backButton.setObjectName("backButton")
        self.backButton.clicked.connect(lambda: goToStage1FromTournaments(dashboard))

        font.setPointSize(15)
        font.setBold(False)

        self.oneLabel = AutoResizingLabel(15, False, parent = self)
        self.oneLabel.setGeometry(QtCore.QRect(10, 50, 16, 16))
        self.oneLabel.setFont(font)
        self.oneLabel.setObjectName("oneLabel")
        self.oneLabel.setHidden(True)

        self.oneActive = False
        self.oneFull = False

        self.twoLabel = AutoResizingLabel(15, False, parent = self)
        self.twoLabel.setGeometry(QtCore.QRect(10, 80, 16, 16))
        self.twoLabel.setFont(font)
        self.twoLabel.setObjectName("twoLabel")
        self.twoLabel.setHidden(True)

        self.twoActive = False
        self.twoFull = False

        self.threeLabel = AutoResizingLabel(15, False, parent = self)
        self.threeLabel.setGeometry(QtCore.QRect(10, 110, 16, 16))
        self.threeLabel.setFont(font)
        self.threeLabel.setObjectName("threeLabel")
        self.threeLabel.setHidden(True)

        self.threeActive = False
        self.threeFull = False

        self.fourLabel = AutoResizingLabel(15, False, parent = self)
        self.fourLabel.setGeometry(QtCore.QRect(10, 140, 16, 16))
        self.fourLabel.setFont(font)
        self.fourLabel.setObjectName("fourLabel")
        self.fourLabel.setHidden(True)

        self.fourActive = False
        self.fourFull = False

        self.fiveLabel = AutoResizingLabel(15, False, parent = self)
        self.fiveLabel.setGeometry(QtCore.QRect(10, 170, 16, 16))
        self.fiveLabel.setFont(font)
        self.fiveLabel.setObjectName("fiveLabel")
        self.fiveLabel.setHidden(True)

        self.fiveActive = False
        self.fiveFull = False

        self.sixLabel = AutoResizingLabel(15, False, parent = self)
        self.sixLabel.setGeometry(QtCore.QRect(10, 200, 16, 16))
        self.sixLabel.setFont(font)
        self.sixLabel.setObjectName("sixLabel")
        self.sixLabel.setHidden(True)

        self.sixActive = False
        self.sixFull = False

        self.sevenLabel = AutoResizingLabel(15, False, parent = self)
        self.sevenLabel.setGeometry(QtCore.QRect(10, 230, 16, 16))
        self.sevenLabel.setFont(font)
        self.sevenLabel.setObjectName("sevenLabel")
        self.sevenLabel.setHidden(True)

        self.sevenActive = False
        self.sevenFull = False

        self.eightLabel = AutoResizingLabel(15, False, parent = self)
        self.eightLabel.setGeometry(QtCore.QRect(10, 260, 16, 16))
        self.eightLabel.setFont(font)
        self.eightLabel.setObjectName("eightLabel")
        self.eightLabel.setHidden(True)

        self.eightActive = False
        self.eightFull = False

        self.player1Label = AutoResizingLabel(15, False, parent = self)
        self.player1Label.setGeometry(QtCore.QRect(40, 50, 161, 16))
        self.player1Label.setFont(font)
        self.player1Label.setObjectName("player1Label")
        self.player1Label.setHidden(True)

        self.player1id = -1
        self.player1username = ""
        self.player1rating = -1

        self.player2Label = AutoResizingLabel(15, False, parent = self)
        self.player2Label.setGeometry(QtCore.QRect(40, 80, 161, 16))
        self.player2Label.setFont(font)
        self.player2Label.setObjectName("player2Label")
        self.player2Label.setHidden(True)

        self.player2id = -1
        self.player2username = ""
        self.player2rating = -1

        self.player3Label = AutoResizingLabel(15, False, parent = self)
        self.player3Label.setGeometry(QtCore.QRect(40, 110, 161, 16))
        self.player3Label.setFont(font)
        self.player3Label.setObjectName("player3Label")
        self.player3Label.setHidden(True)

        self.player3id = -1
        self.player3username = ""
        self.player3rating = -1

        self.player4Label = AutoResizingLabel(15, False, parent = self)
        self.player4Label.setGeometry(QtCore.QRect(40, 140, 161, 16))
        self.player4Label.setFont(font)
        self.player4Label.setObjectName("player4Label")
        self.player4Label.setHidden(True)

        self.player4id = -1
        self.player4username = ""
        self.player4rating = -1

        self.player5Label = AutoResizingLabel(15, False, parent = self)
        self.player5Label.setGeometry(QtCore.QRect(40, 170, 161, 16))
        self.player5Label.setFont(font)
        self.player5Label.setObjectName("player5Label")
        self.player5Label.setHidden(True)

        self.player5id = -1
        self.player5username = ""
        self.player5rating = -1

        self.player6Label = AutoResizingLabel(15, False, parent = self)
        self.player6Label.setGeometry(QtCore.QRect(40, 200, 161, 16))
        self.player6Label.setFont(font)
        self.player6Label.setObjectName("player6Label")
        self.player6Label.setHidden(True)

        self.player6id = -1
        self.player6username = ""
        self.player6rating = -1

        self.player7Label = AutoResizingLabel(15, False, parent = self)
        self.player7Label.setGeometry(QtCore.QRect(40, 230, 161, 16))
        self.player7Label.setFont(font)
        self.player7Label.setObjectName("player7Label")
        self.player7Label.setHidden(True)

        self.player7id = -1
        self.player7username = ""
        self.player7rating = -1

        self.player8Label = AutoResizingLabel(15, False, parent = self)
        self.player8Label.setGeometry(QtCore.QRect(40, 260, 161, 16))
        self.player8Label.setFont(font)
        self.player8Label.setObjectName("player8Label")
        self.player8Label.setHidden(True)

        self.player8id = -1
        self.player8username = ""
        self.player8rating = -1

        self.userElements = [[self.oneLabel, self.player1Label],
                        [self.twoLabel, self.player2Label],
                        [self.threeLabel, self.player3Label],
                        [self.fourLabel, self.player4Label],
                        [self.fiveLabel, self.player5Label],
                        [self.sixLabel, self.player6Label],
                        [self.sevenLabel, self.player7Label],
                        [self.eightLabel, self.player8Label]]
        
        # stores which users are active
        self.userValues = [[self.oneActive, self.oneFull], [self.twoActive, self.twoFull], 
                      [self.threeActive, self.threeFull], [self.fourActive, self.fourFull], 
                      [self.fiveActive, self.fiveFull], [self.sixActive, self.sixFull], 
                      [self.sevenActive, self.sevenFull], [self.eightActive, self.eightFull]]
        
        # stores the details of users
        self.userDetails = [[self.player1id, self.player1username, self.player1rating],
                            [self.player2id, self.player2username, self.player2rating],
                            [self.player3id, self.player3username, self.player3rating],
                            [self.player4id, self.player4username, self.player4rating],
                            [self.player5id, self.player5username, self.player5rating],
                            [self.player6id, self.player6username, self.player6rating],
                            [self.player7id, self.player7username, self.player7rating],
                            [self.player8id, self.player8username, self.player8rating]]
        

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.clearFocus()

        self.secondaryUserRadioButton.setChecked(True)



    # ensures no radio button is stuck with the focus ring
    def clearFocus(self):
        self.guestRadioButton.clearFocus()
        self.secondaryUserRadioButton.clearFocus()

        self.guestRadioButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.secondaryUserRadioButton.setFocusPolicy(QtCore.Qt.NoFocus)


    # set the correct amount of players to be active
    def setActivePlayers(self, capacity):
        for i in range(0, capacity):
            for y in self.userElements[i]:
                y.setHidden(False)

            self.userValues[i][0] = True
        

    def cycleUser(self, action):
        print(self.capacity)
        self.index = (self.index + action) % self.capacity

        self.playerLogInLabel.setText(f"Player {self.index + 1}")

        # if user is already logged in at this index
        if self.userValues[self.index][1] == True:
            self.secondaryUserRadioButton.setHidden(True)
            self.guestRadioButton.setHidden(True)

            self.usernameInput.setHidden(True)
            self.passwordInput.setHidden(True)
            self.guestNameInput.setHidden(True)

            self.userTypeLabel.setHidden(False)
            self.userLabel.setHidden(False)

            if self.userDetails[self.index][0] == "guest":
                self.userTypeLabel.setText("Guest:")

            else:
                self.userTypeLabel.setText("User:")
            
            self.userLabel.setText(self.userDetails[self.index][1])

            self.logInButton.setText("Log out")

        else:
            self.secondaryUserRadioButton.setHidden(False)
            self.guestRadioButton.setHidden(False)

            self.userTypeLabel.setHidden(True)
            self.userLabel.setHidden(True)

            self.secondaryUserRadioButton.setChecked(True)
            self.usernameInput.setHidden(False)
            self.passwordInput.setHidden(False)

            self.usernameInput.setText("")
            self.passwordInput.setText("")
            self.guestNameInput.setText("")

            self.logInButton.setText("Log In")

        self.errorLabel.setHidden(True)


    # switch the inputs from secondary user to guest
    def switchInputs(self, type):
        self.usernameInput.setHidden(type)
        self.passwordInput.setHidden(type)
        self.guestNameInput.setHidden(type - 1)
    

    def resetUi(self):
        self.index = 0
        self.capacity = 0
        self.tournamentType = ""

        self.logInButton.setText("Log In")
        self.usernameInput.setText("")
        self.passwordInput.setText("")
        self.guestNameInput.setText("")

        self.playerLogInLabel.setText("Player 1")

        self.oneActive = False
        self.oneFull = False

        self.twoLabel.setHidden(True)

        self.twoActive = False
        self.twoFull = False

        self.threeLabel.setHidden(True)

        self.threeActive = False
        self.threeFull = False

        self.fourLabel.setHidden(True)

        self.fourActive = False
        self.fourFull = False

        self.fiveLabel.setHidden(True)

        self.fiveActive = False
        self.fiveFull = False

        self.sixLabel.setHidden(True)

        self.sixActive = False
        self.sixFull = False

        self.sevenLabel.setHidden(True)

        self.sevenActive = False
        self.sevenFull = False

        self.eightLabel.setHidden(True)

        self.eightActive = False
        self.eightFull = False

        self.player1Label.setHidden(True)
        self.player1Label.setText("")

        self.player1id = -1
        self.player1username = ""
        self.player1rating = -1

        self.player2Label.setHidden(True)
        self.player2Label.setText("")

        self.player2id = -1
        self.player2username = ""
        self.player2rating = -1

        self.player3Label.setHidden(True)
        self.player3Label.setText("")

        self.player3id = -1
        self.player3username = ""
        self.player3rating = -1

        self.player4Label.setHidden(True)
        self.player4Label.setText("")

        self.player4id = -1
        self.player4username = ""
        self.player4rating = -1

        self.player5Label.setHidden(True)
        self.player5Label.setText("")

        self.player5id = -1
        self.player5username = ""
        self.player5rating = -1

        self.player6Label.setHidden(True)
        self.player6Label.setText("")

        self.player6id = -1
        self.player6username = ""
        self.player6rating = -1

        self.player7Label.setHidden(True)
        self.player7Label.setText("")

        self.player7id = -1
        self.player7username = ""
        self.player7rating = -1

        self.player8Label.setHidden(True)
        self.player8Label.setText("")

        self.player8id = -1
        self.player8username = ""
        self.player8rating = -1

        self.userElements = [[self.oneLabel, self.player1Label],
                        [self.twoLabel, self.player2Label],
                        [self.threeLabel, self.player3Label],
                        [self.fourLabel, self.player4Label],
                        [self.fiveLabel, self.player5Label],
                        [self.sixLabel, self.player6Label],
                        [self.sevenLabel, self.player7Label],
                        [self.eightLabel, self.player8Label]]
        
        self.userValues = [[self.oneActive, self.oneFull], [self.twoActive, self.twoFull], 
                      [self.threeActive, self.threeFull], [self.fourActive, self.fourFull], 
                      [self.fiveActive, self.fiveFull], [self.sixActive, self.sixFull], 
                      [self.sevenActive, self.sevenFull], [self.eightActive, self.eightFull]]
        
        self.userDetails = [[self.player1id, self.player1username, self.player1rating],
                            [self.player2id, self.player2username, self.player2rating],
                            [self.player3id, self.player3username, self.player3rating],
                            [self.player4id, self.player4username, self.player4rating],
                            [self.player5id, self.player5username, self.player5rating],
                            [self.player6id, self.player6username, self.player6rating],
                            [self.player7id, self.player7username, self.player7rating],
                            [self.player8id, self.player8username, self.player8rating]]

        self.clearFocus()

        self.secondaryUserRadioButton.setChecked(True)
        self.secondaryUserRadioButton.setHidden(False)
        self.guestRadioButton.setHidden(False)
        self.usernameInput.setHidden(False)
        self.passwordInput.setHidden(False)
        self.guestNameInput.setHidden(True)
        self.userTypeLabel.setHidden(True)
        self.userLabel.setHidden(True)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.titleLabel.setText(_translate("tournamentStage2Page", "Round Robin"))
        self.playerLogInLabel.setText(_translate("tournamentStage2Page", "Player 1"))
        self.guestRadioButton.setText(_translate("tournamentStage2Page", "Guest"))
        self.secondaryUserRadioButton.setText(_translate("tournamentStage2Page", "Secondary User"))
        self.cycleRightButton.setText(_translate("tournamentStage2Page", ">"))
        self.cycleLeftButton.setText(_translate("tournamentStage2Page", "<"))
        self.usernameInput.setPlaceholderText(_translate("tournamentStage2Page", "Username:"))
        self.passwordInput.setPlaceholderText(_translate("tournamentStage2Page", "Password:"))
        self.guestNameInput.setPlaceholderText(_translate("tournamentStage2Page", "Name:"))
        self.userTypeLabel.setText(_translate("tournamentStage2Page", "User:"))
        self.userTypeLabel.setText(_translate("tournamentStage2Page", "Player"))
        self.logInButton.setText(_translate("tournamentStage2Page", "Log In"))
        self.errorLabel.setText(_translate("tournamentStage2Page", "Error:"))
        self.playButton.setText(_translate("tournamentStage2Page", "Play"))
        self.backButton.setText(_translate("tournamentStage2Page", "Back"))
        self.oneLabel.setText(_translate("tournamentStage2Page", "1."))
        self.twoLabel.setText(_translate("tournamentStage2Page", "2."))
        self.threeLabel.setText(_translate("tournamentStage2Page", "3."))
        self.fourLabel.setText(_translate("tournamentStage2Page", "4."))
        self.fiveLabel.setText(_translate("tournamentStage2Page", "5."))
        self.sixLabel.setText(_translate("tournamentStage2Page", "6."))
        self.sevenLabel.setText(_translate("tournamentStage2Page", "7."))
        self.eightLabel.setText(_translate("tournamentStage2Page", "8."))
        self.player1Label.setText(_translate("tournamentStage2Page", "Player 1"))
        self.player2Label.setText(_translate("tournamentStage2Page", "Player 2"))
        self.player3Label.setText(_translate("tournamentStage2Page", "Player 3"))
        self.player4Label.setText(_translate("tournamentStage2Page", "Player 4"))
        self.player5Label.setText(_translate("tournamentStage2Page", "Player 5"))
        self.player6Label.setText(_translate("tournamentStage2Page", "Player 6"))
        self.player7Label.setText(_translate("tournamentStage2Page", "Player 7"))
        self.player8Label.setText(_translate("tournamentStage2Page", "Player 8"))

