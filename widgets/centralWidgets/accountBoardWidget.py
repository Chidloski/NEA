from PyQt5 import QtCore, QtGui, QtWidgets
from playerDB.jsonFunctions import *
from widgets.centralWidgets.chessFunctions.chessBoardClasses import lightSquare, darkSquare
from PyQt5.QtGui import QPixmap
from widgets.labelClasses import AutoResizingLabel, AutoResizingClickableLabel, AutoResizingRadioButton
import re


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



class Ui_accountBoard(QtWidgets.QWidget):

    def setupUi(self, dashboard):
        self.setObjectName("accountBoard")
        self.resize(560, 560)

        self.avatarIndex = 0
        self.themeIndex = 0
        self.pieceIndex = 0
        self.userId = -1

        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(28)
        font.setBold(True)

        self.accountManagementLabel = AutoResizingLabel(28, True, parent=self)
        self.accountManagementLabel.setGeometry(QtCore.QRect(130, 10, 311, 31))
        self.accountManagementLabel.setFont(font)
        self.accountManagementLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.accountManagementLabel.setObjectName("accountManagementLabel")

        font.setPointSize(28)
        font.setBold(True)

        self.thematicsLabel = AutoResizingLabel(28, True, parent=self)
        self.thematicsLabel.setGeometry(QtCore.QRect(200, 220, 161, 31))
        self.thematicsLabel.setFont(font)
        self.thematicsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.thematicsLabel.setObjectName("thematicsLabel")

        self.avatarLabel = AutoResizingLabel(28, True, parent=self)
        self.avatarLabel.setGeometry(QtCore.QRect(80, 60, 111, 101))
        self.avatarLabel.setFont(font)
        self.avatarLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.avatarLabel.setObjectName("avatarLabel")
        self.avatarLabel.setScaledContents(True)

        font.setBold(False)

        font.setPointSize(13)

        self.usernameInput = QtWidgets.QLineEdit(self)
        self.usernameInput.setGeometry(QtCore.QRect(350, 60, 151, 21))
        self.usernameInput.setFont(font)
        self.usernameInput.setObjectName("usernameInput")
        self.usernameInput.setHidden(True)

        self.nameInput = QtWidgets.QLineEdit(self)
        self.nameInput.setGeometry(QtCore.QRect(350, 90, 151, 21))
        self.nameInput.setFont(font)
        self.nameInput.setObjectName("nameInput")
        self.nameInput.setHidden(True)

        self.emailInput = QtWidgets.QLineEdit(self)
        self.emailInput.setGeometry(QtCore.QRect(350, 120, 151, 21))
        self.emailInput.setFont(font)
        self.emailInput.setObjectName("emailInput")
        self.emailInput.setHidden(True)

        self.usernameInputLabel = AutoResizingLabel(13, False, parent=self)
        self.usernameInputLabel.setGeometry(QtCore.QRect(240, 63, 101, 16))
        self.usernameInputLabel.setFont(font)
        self.usernameInputLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.usernameInputLabel.setObjectName("usernameInputLabel")

        self.nameInputLabel = AutoResizingLabel(13, False, parent=self)
        self.nameInputLabel.setGeometry(QtCore.QRect(240, 93, 101, 16))
        self.nameInputLabel.setFont(font)
        self.nameInputLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.nameInputLabel.setObjectName("nameInputLabel")

        self.emailInputLabel = AutoResizingLabel(13, False, parent=self)
        self.emailInputLabel.setGeometry(QtCore.QRect(240, 123, 101, 16))
        self.emailInputLabel.setFont(font)
        self.emailInputLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.emailInputLabel.setObjectName("emailInputLabel")

        self.usernameLabel = AutoResizingLabel(13, False, parent=self)
        self.usernameLabel.setGeometry(QtCore.QRect(350, 63, 171, 16))
        self.usernameLabel.setFont(font)
        self.usernameLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.usernameLabel.setObjectName("usernameLabel")

        self.nameLabel = AutoResizingLabel(13, False, parent=self)
        self.nameLabel.setGeometry(QtCore.QRect(350, 93, 171, 16))
        self.nameLabel.setFont(font)
        self.nameLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.nameLabel.setObjectName("nameLabel")

        self.emailLabel = AutoResizingLabel(13, False, parent=self)
        self.emailLabel.setGeometry(QtCore.QRect(350, 123, 171, 16))
        self.emailLabel.setFont(font)
        self.emailLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.emailLabel.setObjectName("emailLabel")

        self.errorLabel = AutoResizingLabel(13, False, parent=self)
        self.errorLabel.setGeometry(240, 143, 210, 32)
        self.errorLabel.setFont(font)
        self.errorLabel.setStyleSheet("color: rgb(175, 61, 50)")
        self.errorLabel.setText("")
        self.errorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.errorLabel.setObjectName("errorLabel")
        self.errorLabel.setHidden(True)

        font.setPointSize(16)

        self.avatarCycleLeftLabel = AutoResizingClickableLabel(16, False, parent=self)
        self.avatarCycleLeftLabel.setGeometry(QtCore.QRect(50, 103, 21, 16))
        self.avatarCycleLeftLabel.setFont(font)
        self.avatarCycleLeftLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.avatarCycleLeftLabel.setObjectName("avatarCycleLeftLabel")
        self.avatarCycleLeftLabel.clicked.connect(lambda: self.cycle(-1, self.avatarIndex, 5, "avatar"))
        self.avatarCycleLeftLabel.setHidden(True)

        self.avatarCycleRightLabel = AutoResizingClickableLabel(16, False, parent=self)
        self.avatarCycleRightLabel.setGeometry(QtCore.QRect(200, 103, 21, 16))
        self.avatarCycleRightLabel.setFont(font)
        self.avatarCycleRightLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.avatarCycleRightLabel.setObjectName("avatarCycleRightLabel")
        self.avatarCycleRightLabel.clicked.connect(lambda: self.cycle(1, self.avatarIndex, 5, "avatar"))
        self.avatarCycleRightLabel.setHidden(True)

        font.setPointSize(14)

        self.accountEditButton = QtWidgets.QPushButton(self)
        self.accountEditButton.setGeometry(QtCore.QRect(190, 170, 181, 32))
        self.accountEditButton.setFont(font)
        self.accountEditButton.setObjectName("accountEditButton")
        self.accountEditButton.clicked.connect(lambda: self.editAccountDetails(self.userId))

        self.tile1Label = lightSquare(self)
        self.tile1Label.setGeometry(QtCore.QRect(50, 260, 71, 71))
        self.tile1Label.setStyleSheet("background-color: rgb(184, 184, 184)")
        self.tile1Label.setText("")
        self.tile1Label.setObjectName("tile1Label")

        self.tile5Label = lightSquare(self)
        self.tile5Label.setGeometry(QtCore.QRect(121, 331, 71, 71))
        self.tile5Label.setStyleSheet("background-color: rgb(184, 184, 184)")
        self.tile5Label.setText("")
        self.tile5Label.setObjectName("tile5Label")

        self.tile9Label = lightSquare(self)
        self.tile9Label.setGeometry(QtCore.QRect(192, 402, 71, 71))
        self.tile9Label.setStyleSheet("background-color: rgb(184, 184, 184)")
        self.tile9Label.setText("")
        self.tile9Label.setObjectName("tile9Label")

        self.tile7Label = lightSquare(self)
        self.tile7Label.setGeometry(QtCore.QRect(50, 402, 71, 71))
        self.tile7Label.setStyleSheet("background-color: rgb(184, 184, 184)")
        self.tile7Label.setText("")
        self.tile7Label.setObjectName("tile7Label")

        self.tile3Label = lightSquare(self)
        self.tile3Label.setGeometry(QtCore.QRect(192, 260, 71, 71))
        self.tile3Label.setStyleSheet("background-color: rgb(184, 184, 184)")
        self.tile3Label.setText("")
        self.tile3Label.setObjectName("tile3Label")

        self.tile2Label = darkSquare(self)
        self.tile2Label.setGeometry(QtCore.QRect(121, 260, 71, 71))
        self.tile2Label.setStyleSheet("background-color: rgb(133, 133, 133)")
        self.tile2Label.setText("")
        self.tile2Label.setObjectName("tile2Label")

        self.tile6Label = darkSquare(self)
        self.tile6Label.setGeometry(QtCore.QRect(192, 331, 71, 71))
        self.tile6Label.setStyleSheet("background-color: rgb(133, 133, 133)")
        self.tile6Label.setText("")
        self.tile6Label.setObjectName("tile6Label")

        self.tile4Label = darkSquare(self)
        self.tile4Label.setGeometry(QtCore.QRect(50, 331, 71, 71))
        self.tile4Label.setStyleSheet("background-color: rgb(133, 133, 133)")
        self.tile4Label.setText("")
        self.tile4Label.setObjectName("tile4Label")

        self.tile8Label = darkSquare(self)
        self.tile8Label.setGeometry(QtCore.QRect(121, 402, 71, 71))
        self.tile8Label.setStyleSheet("background-color: rgb(133, 133, 133)")
        self.tile8Label.setText("")
        self.tile8Label.setObjectName("tile8Label")

        font.setPointSize(16)

        self.themeCycleLeftLabel = AutoResizingClickableLabel(16, False, parent=self)
        self.themeCycleLeftLabel.setGeometry(QtCore.QRect(100, 480, 21, 16))
        self.themeCycleLeftLabel.setFont(font)
        self.themeCycleLeftLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.themeCycleLeftLabel.setObjectName("themeCycleLeftLabel")
        self.themeCycleLeftLabel.clicked.connect(lambda: self.cycle(-1, self.themeIndex, 5, "theme"))
        self.themeCycleLeftLabel.setHidden(True)

        self.pieceCycleLeftLabel = AutoResizingClickableLabel(16, False, parent=self)
        self.pieceCycleLeftLabel.setGeometry(QtCore.QRect(100, 500, 21, 16))
        self.pieceCycleLeftLabel.setFont(font)
        self.pieceCycleLeftLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pieceCycleLeftLabel.setObjectName("piecesCycleLabel")
        self.pieceCycleLeftLabel.clicked.connect(lambda: self.cycle(-1, self.pieceIndex, 5, "piece"))
        self.pieceCycleLeftLabel.setHidden(True)

        self.themeCycleRightLabel = AutoResizingClickableLabel(16, False, parent=self)
        self.themeCycleRightLabel.setGeometry(QtCore.QRect(190, 480, 21, 16))
        self.themeCycleRightLabel.setFont(font)
        self.themeCycleRightLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.themeCycleRightLabel.setObjectName("themeCycleRightLabel")
        self.themeCycleRightLabel.clicked.connect(lambda: self.cycle(1, self.themeIndex, 5, "theme"))
        self.themeCycleRightLabel.setHidden(True)

        self.pieceCycleRightLabel = AutoResizingClickableLabel(16, False, parent=self)
        self.pieceCycleRightLabel.setGeometry(QtCore.QRect(190, 500, 21, 16))
        self.pieceCycleRightLabel.setFont(font)
        self.pieceCycleRightLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pieceCycleRightLabel.setObjectName("pieceCycleRightLabel")
        self.pieceCycleRightLabel.clicked.connect(lambda: self.cycle(1, self.pieceIndex, 5, "piece"))
        self.pieceCycleRightLabel.setHidden(True)

        font.setPointSize(13)

        self.themeLabel = AutoResizingLabel(13, False, parent=self)
        self.themeLabel.setGeometry(QtCore.QRect(125, 480, 61, 16))
        self.themeLabel.setFont(font)
        self.themeLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.themeLabel.setObjectName("themeLabel")
        self.themeLabel.setHidden(True)

        self.pieceLabel = AutoResizingLabel(13, False, parent=self)
        self.pieceLabel.setGeometry(QtCore.QRect(125, 500, 61, 16))
        self.pieceLabel.setFont(font)
        self.pieceLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.pieceLabel.setObjectName("pieceLabel")
        self.pieceLabel.setHidden(True)

        font.setPointSize(14)

        self.thematicsEditButton = QtWidgets.QPushButton(self)
        self.thematicsEditButton.setGeometry(QtCore.QRect(190, 520, 181, 32))
        self.thematicsEditButton.setFont(font)
        self.thematicsEditButton.setObjectName("thematicsEditButton")
        self.thematicsEditButton.clicked.connect(lambda: self.editThematics(self.userId, dashboard))

        font.setPointSize(20)
        font.setBold(True)

        self.fontsLabel = AutoResizingLabel(20, True, parent=self)
        self.fontsLabel.setGeometry(QtCore.QRect(330, 260, 101, 21))
        self.fontsLabel.setFont(font)
        self.fontsLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.fontsLabel.setObjectName("fontsLabel")

        font.setBold(False)
        font.setPointSize(16)
        font.setFamily("Fira Code")

        self.firaCodeRadioButton = AutoResizingRadioButton(16, False, parent=self)
        self.firaCodeRadioButton.setGeometry(QtCore.QRect(340, 290, 181, 20))
        self.firaCodeRadioButton.setFont(font)
        self.firaCodeRadioButton.setObjectName("firaCodeRadioButton")
        self.firaCodeRadioButton.setEnabled(False)
        self.firaCodeRadioButton.fontType = "Fira Code"

        font.setFamily("Arial")
        
        self.arialRadioButton = AutoResizingRadioButton(16, False, parent=self)
        self.arialRadioButton.setGeometry(QtCore.QRect(340, 320, 181, 20))
        self.arialRadioButton.setFont(font)
        self.arialRadioButton.setObjectName("arialRadioButton")
        self.arialRadioButton.setEnabled(False)
        self.arialRadioButton.fontType = "Arial"

        font.setFamily("Helvetica")

        self.helveticaRadioButton = AutoResizingRadioButton(16, False, parent=self)
        self.helveticaRadioButton.setGeometry(QtCore.QRect(340, 350, 181, 20))
        self.helveticaRadioButton.setFont(font)
        self.helveticaRadioButton.setObjectName("helveticaRadioButton")
        self.helveticaRadioButton.setEnabled(False)
        self.helveticaRadioButton.fontType = "Helvetica"

        font.setFamily("Times New Roman")

        self.timesNewRomanRadioButton = AutoResizingRadioButton(16, False, parent=self)
        self.timesNewRomanRadioButton.setGeometry(QtCore.QRect(340, 380, 181, 20))
        self.timesNewRomanRadioButton.setFont(font)
        self.timesNewRomanRadioButton.setObjectName("timesNewRomanRadioButton")
        self.timesNewRomanRadioButton.setEnabled(False)
        self.timesNewRomanRadioButton.fontType = "Times New Roman"

        font.setFamily("Wingdings 3")

        self.wingdingsRadioButton = AutoResizingRadioButton(16, False, parent=self)
        self.wingdingsRadioButton.setGeometry(QtCore.QRect(340, 410, 181, 20))
        self.wingdingsRadioButton.setFont(font)
        self.wingdingsRadioButton.setObjectName("wingdingsRadioButton")
        self.wingdingsRadioButton.setEnabled(False)
        self.wingdingsRadioButton.fontType = "Wingdings 3"

        font.setFamily("OpenDyslexic3")

        self.dyslexicFontRadioButton = AutoResizingRadioButton(16, False, parent=self)
        self.dyslexicFontRadioButton.setGeometry(QtCore.QRect(340, 440, 181, 20))
        self.dyslexicFontRadioButton.setFont(font)
        self.dyslexicFontRadioButton.setObjectName("dyslexicFontRadioButton")
        self.dyslexicFontRadioButton.setEnabled(False)
        self.dyslexicFontRadioButton.fontType = "OpenDyslexic3"

        self.fontTypeGroup = QtWidgets.QButtonGroup(self)
        self.fontTypeGroup.addButton(self.firaCodeRadioButton)
        self.fontTypeGroup.addButton(self.arialRadioButton)
        self.fontTypeGroup.addButton(self.helveticaRadioButton)
        self.fontTypeGroup.addButton(self.timesNewRomanRadioButton)
        self.fontTypeGroup.addButton(self.wingdingsRadioButton)
        self.fontTypeGroup.addButton(self.dyslexicFontRadioButton)

        font.setFamily("Fira Code")

        self.kingLabel = QtWidgets.QLabel(self)
        self.kingLabel.setGeometry(QtCore.QRect(55, 270, 60, 60))
        self.kingLabel.setText("")
        self.kingLabel.setPixmap(QtGui.QPixmap("Resources/ChessIcons/WhiteKing.png"))
        self.kingLabel.setScaledContents(True)
        self.kingLabel.setObjectName("kingLabel")

        self.queenLabel = QtWidgets.QLabel(self)
        self.queenLabel.setGeometry(QtCore.QRect(126, 270, 60, 60))
        self.queenLabel.setText("")
        self.queenLabel.setPixmap(QtGui.QPixmap("Resources/ChessIcons/WhiteQueen.png"))
        self.queenLabel.setScaledContents(True)
        self.queenLabel.setObjectName("queenLabel")

        self.rookLabel = QtWidgets.QLabel(self)
        self.rookLabel.setGeometry(QtCore.QRect(197, 270, 60, 60))
        self.rookLabel.setText("")
        self.rookLabel.setPixmap(QtGui.QPixmap("Resources/ChessIcons/WhiteRook.png"))
        self.rookLabel.setScaledContents(True)
        self.rookLabel.setObjectName("rookLabel")

        self.bishopLabel = QtWidgets.QLabel(self)
        self.bishopLabel.setGeometry(QtCore.QRect(55, 412, 60, 60))
        self.bishopLabel.setText("")
        self.bishopLabel.setPixmap(QtGui.QPixmap("Resources/ChessIcons/BlackBishop.png"))
        self.bishopLabel.setScaledContents(True)
        self.bishopLabel.setObjectName("bishopLabel")

        self.knightLabel = QtWidgets.QLabel(self)
        self.knightLabel.setGeometry(QtCore.QRect(126, 412, 60, 60))
        self.knightLabel.setText("")
        self.knightLabel.setPixmap(QtGui.QPixmap("Resources/ChessIcons/BlackKnight.png"))
        self.knightLabel.setScaledContents(True)
        self.knightLabel.setObjectName("knightLabel")

        self.pawnLabel = QtWidgets.QLabel(self)
        self.pawnLabel.setGeometry(QtCore.QRect(197, 412, 60, 60))
        self.pawnLabel.setText("")
        self.pawnLabel.setPixmap(QtGui.QPixmap("Resources/ChessIcons/BlackPawn.png"))
        self.pawnLabel.setScaledContents(True)
        self.pawnLabel.setObjectName("pawnLabel")

        self.retranslateUi()

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.accountManagementLabel.setText(_translate("accountBoard", "Account Management"))
        self.thematicsLabel.setText(_translate("accountBoard", "Thematics"))
        self.avatarLabel.setText(_translate("accountBoard", "Image here"))
        self.usernameInput.setPlaceholderText(_translate("accountBoard", "Username:"))
        self.nameInput.setPlaceholderText(_translate("accountBoard", "Full Name:"))
        self.emailInput.setPlaceholderText(_translate("accountBoard", "Email:"))
        self.usernameInputLabel.setText(_translate("accountBoard", "Username:"))
        self.nameInputLabel.setText(_translate("accountBoard", "Full Name:"))
        self.emailInputLabel.setText(_translate("accountBoard", "Email:"))
        self.usernameLabel.setText(_translate("accountBoard", "Username:"))
        self.nameLabel.setText(_translate("accountBoard", "Full Name"))
        self.emailLabel.setText(_translate("accountBoard", "Email"))
        self.avatarCycleLeftLabel.setText(_translate("accountBoard", "<"))
        self.avatarCycleRightLabel.setText(_translate("accountBoard", ">"))
        self.accountEditButton.setText(_translate("accountBoard", "Change Details"))
        self.themeCycleLeftLabel.setText(_translate("accountBoard", "<"))
        self.pieceCycleLeftLabel.setText(_translate("accountBoard", "<"))
        self.themeCycleRightLabel.setText(_translate("accountBoard", ">"))
        self.pieceCycleRightLabel.setText(_translate("accountBoard", ">"))
        self.themeLabel.setText(_translate("accountBoard", "Theme"))
        self.pieceLabel.setText(_translate("accountBoard", "Pieces"))
        self.thematicsEditButton.setText(_translate("accountBoard", "Change Thematics"))
        self.fontsLabel.setText(_translate("accountBoard", "Fonts:"))
        self.firaCodeRadioButton.setText(_translate("accountBoard", "Fira Code"))
        self.arialRadioButton.setText(_translate("accountBoard", "Ariel"))
        self.helveticaRadioButton.setText(_translate("accountBoard", "Helvetica"))
        self.timesNewRomanRadioButton.setText(_translate("accountBoard", "Times New Roman"))
        self.wingdingsRadioButton.setText(_translate("accountBoard", "Wingdings"))
        self.dyslexicFontRadioButton.setText(_translate("accountBoard", "Dyslexia-Friendly"))


    def cycle(self, direction, currentIndex, size, type):
        currentIndex = (currentIndex + direction) % size

        if type == "avatar":
            self.populateAvatar(currentIndex)
            self.avatarIndex = currentIndex

        elif type == "theme":
            self.populateTheme(currentIndex)
            self.themeIndex = currentIndex

        else:
            self.populatePieces(currentIndex)
            self.pieceIndex = currentIndex


    def populateTheme(self, index):
        query = {"id": index}
        themeDetails = getData("themes", **query)

        print(themeDetails)

        themeDetails = themeDetails[0]

        lightColour = "rgb(" + themeDetails["light"] + ");"
        darkColour = "rgb(" + themeDetails["dark"] + ");"

        self.tile1Label.setStyleSheet("background-color: " + lightColour)
        self.tile3Label.setStyleSheet("background-color: " + lightColour)
        self.tile5Label.setStyleSheet("background-color: " + lightColour)
        self.tile7Label.setStyleSheet("background-color: " + lightColour)
        self.tile9Label.setStyleSheet("background-color: " + lightColour)

        self.tile2Label.setStyleSheet("background-color: " + darkColour)
        self.tile4Label.setStyleSheet("background-color: " + darkColour)
        self.tile6Label.setStyleSheet("background-color: " + darkColour)
        self.tile8Label.setStyleSheet("background-color: " + darkColour)


    def populateAvatar(self, index):
        self.avatarLabel.setPixmap(QPixmap("Resources/UserIcons/avatar" + str(index) + ".png"))


    def populatePieces(self, index):
        query = {"id": index}
        pieceFolder = getData("pieces", **query)

        pieceFolder = pieceFolder[0]["folder"]

        self.kingLabel.setPixmap(QPixmap("Resources/ChessIcons/" + pieceFolder + "/WhiteKing.png"))
        self.queenLabel.setPixmap(QPixmap("Resources/ChessIcons/" + pieceFolder + "/WhiteQueen.png"))
        self.rookLabel.setPixmap(QPixmap("Resources/ChessIcons/" + pieceFolder + "/WhiteRook.png"))
        self.bishopLabel.setPixmap(QPixmap("Resources/ChessIcons/" + pieceFolder + "/BlackBishop.png"))
        self.knightLabel.setPixmap(QPixmap("Resources/ChessIcons/" + pieceFolder + "/BlackKnight.png"))
        self.pawnLabel.setPixmap(QPixmap("Resources/ChessIcons/" + pieceFolder + "/BlackPawn.png"))


    def populateFonts(self, type):
        if type == "Wingdings 3":
            font = "wingdings"

        elif type == "OpenDyslexic3":
            font = "dyslexicFont"

        else:
            fontWords = type.split()
            font = fontWords[0].lower() + ''.join(word.title() for word in fontWords[1:])

        getattr(self, f"{font}RadioButton").setChecked(True)


    def editThematics(self, userId, dashboard):
        if self.thematicsEditButton.text() == "Change Thematics":
            self.thematicsEditButton.setText("Save Changes")

            self.firaCodeRadioButton.setEnabled(True)
            self.arialRadioButton.setEnabled(True)
            self.helveticaRadioButton.setEnabled(True)
            self.timesNewRomanRadioButton.setEnabled(True)
            self.wingdingsRadioButton.setEnabled(True)
            self.dyslexicFontRadioButton.setEnabled(True)

            self.themeCycleLeftLabel.setHidden(False)
            self.themeCycleRightLabel.setHidden(False)
            self.themeLabel.setHidden(False)

            self.pieceCycleLeftLabel.setHidden(False)
            self.pieceCycleRightLabel.setHidden(False)
            self.pieceLabel.setHidden(False)

        else:
            query = {"id": userId}
            userData = getData("users", **query)
            userData = userData[0]

            userData["theme"] = self.themeIndex
            userData["pieces"] = self.pieceIndex
            userData["font"] = self.fontTypeGroup.checkedButton().fontType

            update("users", userData, userId)

            self.thematicsEditButton.setText("Change Thematics")

            self.firaCodeRadioButton.setEnabled(False)
            self.arialRadioButton.setEnabled(False)
            self.helveticaRadioButton.setEnabled(False)
            self.timesNewRomanRadioButton.setEnabled(False)
            self.wingdingsRadioButton.setEnabled(False)
            self.dyslexicFontRadioButton.setEnabled(False)

            self.themeCycleLeftLabel.setHidden(True)
            self.themeCycleRightLabel.setHidden(True)
            self.themeLabel.setHidden(True)

            self.pieceCycleLeftLabel.setHidden(True)
            self.pieceCycleRightLabel.setHidden(True)
            self.pieceLabel.setHidden(True)

            pieceQuery = {"id": self.pieceIndex}
            pieceFolder = getData("pieces", **pieceQuery)
            pieceFolder = pieceFolder[0]["folder"]

            themeQuery = {"id": self.themeIndex}
            themeDict = getData("themes", **themeQuery)
            themeDict = themeDict[0]

            stylesheet = """
                lightSquare {
                background-color: rgb(""" + themeDict["light"] + """);
                color: rgb(""" + themeDict["dark"] + """);
                }

                darkSquare {
                background-color: rgb(""" + themeDict["dark"] + """);
                color: rgb(""" + themeDict["light"] + """);
                };"""


            dashboard.changeTheme(stylesheet, themeDict)
            dashboard.changePieces(pieceFolder)
            dashboard.changeFont(self.fontTypeGroup.checkedButton().fontType)

    

    def editAccountDetails(self, userId):
        if self.accountEditButton.text() == "Change Details":
            self.usernameInput.setHidden(False)
            self.nameInput.setHidden(False)
            self.emailInput.setHidden(False)

            self.usernameLabel.setHidden(True)
            self.nameLabel.setHidden(True)
            self.emailLabel.setHidden(True)

            self.avatarCycleLeftLabel.setHidden(False)
            self.avatarCycleRightLabel.setHidden(False)

            self.accountEditButton.setText("Save Details")

            print(self.emailInput.text())

        else:
            if len(self.usernameInput.text()) == 0 or len(self.nameInput.text()) == 0 or len(self.emailInput.text()) == 0:
                self.errorLabel.setText("Please ensure all fields are filled")
                self.errorLabel.setHidden(False)

            elif self.emailValidation(self.emailInput.text()) == False:
                self.errorLabel.setText("Invalid email address")
                self.errorLabel.setHidden(False)

            elif self.usernameValidation(self.usernameInput.text()) == False:
                self.errorLabel.setText("Username between 5-16 characters \n Allowed special characters: _, -, .")
                self.errorLabel.setHidden(False)

            elif isUnique("email", self.emailInput.text(), userId) == False:
                self.errorLabel.setText("Email already taken")
                self.errorLabel.setHidden(False)

            elif isUnique("username", self.usernameInput.text(), userId) == False:
                self.errorLabel.setText("Username already taken")
                self.errorLabel.setHidden(False)

            else:
                query = {"id": userId}
                userData = getData("users", **query)

                userData = userData[0]

                userData["username"] = self.usernameInput.text()
                userData["fullName"] = self.nameInput.text()
                userData["email"] = self.emailInput.text()
                userData["avatar"] = self.avatarIndex

                self.usernameLabel.setText(self.usernameInput.text())
                self.nameLabel.setText(self.nameInput.text())
                self.emailLabel.setText(self.emailInput.text())

                update("users", userData, userId)

                self.usernameInput.setHidden(True)
                self.nameInput.setHidden(True)
                self.emailInput.setHidden(True)

                self.usernameLabel.setHidden(False)
                self.nameLabel.setHidden(False)
                self.emailLabel.setHidden(False)

                self.avatarCycleLeftLabel.setHidden(True)
                self.avatarCycleRightLabel.setHidden(True)

                self.errorLabel.setText("")
                self.errorLabel.setHidden(True)

                self.accountEditButton.setText("Change Details")


    def emailValidation(self, email):
        # Define the regular expression for validating an email address
        email_regex = re.compile(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        )
        
        # Use the regex to match the email address
        if re.match(email_regex, email):
            return True
        else:
            return False



    def usernameValidation(self, username):
        # Define the regular expression for validating the username
        username_regex = re.compile(r"^[a-zA-Z0-9_.-]{5,16}$")
        
        # Check if the username matches the regex
        if re.match(username_regex, username):
            return True
        else:
            return False
        


    def resetUi(self):
        self.avatarIndex = 0
        self.themeIndex = 0
        self.pieceIndex = 0
        self.userId = -1

        self.avatarCycleLeftLabel.setHidden(True)
        self.avatarCycleRightLabel.setHidden(True)

        self.usernameInput.setHidden(True)
        self.nameInput.setHidden(True)
        self.emailInput.setHidden(True)

        self.usernameInputLabel.setHidden(False)
        self.nameInputLabel.setHidden(False)
        self.emailInputLabel.setHidden(False)

        self.themeLabel.setHidden(True)
        self.themeCycleLeftLabel.setHidden(True)
        self.themeCycleRightLabel.setHidden(True)

        self.pieceLabel.setHidden(True)
        self.pieceCycleLeftLabel.setHidden(True)
        self.pieceCycleRightLabel.setHidden(True)

        self.firaCodeRadioButton.setEnabled(False)
        self.arialRadioButton.setEnabled(False)
        self.helveticaRadioButton.setEnabled(False)
        self.timesNewRomanRadioButton.setEnabled(False)
        self.wingdingsRadioButton.setEnabled(False)
        self.dyslexicFontRadioButton.setEnabled(False)

        self.accountEditButton.setText("Change Details")
        self.thematicsEditButton.setText("Change Thematics")



    def populate(self, userId):
        query = {"id": userId}
        userData = getData("users", **query)
        userData = userData[0]

        self.userId = userId

        self.themeIndex = userData["theme"]
        self.pieceIndex = userData["pieces"]
        self.avatarIndex = userData["avatar"]
        self.fontType = userData["font"]

        self.usernameInput.setText(userData["username"])
        self.nameInput.setText(userData["fullName"])
        self.emailInput.setText(userData["email"])

        self.usernameLabel.setText(userData["username"])
        self.nameLabel.setText(userData["fullName"])
        self.emailLabel.setText(userData["email"])

        self.populateTheme(self.themeIndex)
        self.populatePieces(self.pieceIndex)
        self.populateAvatar(self.avatarIndex)
        self.populateFonts(self.fontType)
