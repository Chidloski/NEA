from PyQt5 import QtCore, QtGui, QtWidgets
from widgets.utilityWidgets.functions.playFunctions import *

# Responsible for setting up all elements within the log in page
class Ui_PvpStage2(QtWidgets.QWidget):

    def setupUi(self, dashboard, baseWindow):
        # sizing of the widget
        self.setObjectName("pvpStage2Page")
        self.resize(230, 560)
        self.setAutoFillBackground(False)

        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(18)
        font.setBold(True)

        self.currentUserLabel = QtWidgets.QLabel(self)
        self.currentUserLabel.setGeometry(QtCore.QRect(10, 10, 201, 20))
        self.currentUserLabel.setFont(font)
        self.currentUserLabel.setObjectName("currentUserLabel")

        font.setPointSize(13)
        font.setBold(False)

        self.currentUserRatingLabel = QtWidgets.QLabel(self)
        self.currentUserRatingLabel.setGeometry(QtCore.QRect(20, 30, 191, 16))
        self.currentUserRatingLabel.setFont(font)
        self.currentUserRatingLabel.setObjectName("currentUserRatingLabel")

        self.currentUserRatingOutcome = QtWidgets.QLabel(self)
        self.currentUserRatingOutcome.setGeometry(QtCore.QRect(20, 60, 191, 16))
        self.currentUserRatingOutcome.setFont(font)
        self.currentUserRatingOutcome.setObjectName("currentUserRatingOutcome")

        font.setPointSize(10)

        self.currentUserRatingDelta = QtWidgets.QLabel(self)
        self.currentUserRatingDelta.setGeometry(QtCore.QRect(30, 80, 181, 16))
        self.currentUserRatingDelta.setFont(font)
        self.currentUserRatingDelta.setObjectName("currentUserRatingDelta")

        font.setPointSize(18)
        font.setBold(True)

        self.opponentUserLabel = QtWidgets.QLabel(self)
        self.opponentUserLabel.setGeometry(QtCore.QRect(10, 110, 201, 20))
        self.opponentUserLabel.setFont(font)
        self.opponentUserLabel.setObjectName("opponentUserLabel")

        font.setPointSize(13)
        font.setBold(False)

        self.opponentUserRatingLabel = QtWidgets.QLabel(self)
        self.opponentUserRatingLabel.setGeometry(QtCore.QRect(20, 130, 191, 16))
        self.opponentUserRatingLabel.setFont(font)
        self.opponentUserRatingLabel.setObjectName("opponentUserRatingLabel")

        self.opponentUserRatingOutcome = QtWidgets.QLabel(self)
        self.opponentUserRatingOutcome.setGeometry(QtCore.QRect(20, 160, 191, 16))
        self.opponentUserRatingOutcome.setFont(font)
        self.opponentUserRatingOutcome.setObjectName("opponentUserRatingOutcome")

        font.setPointSize(10)
        
        self.opponentUserRatingDelta = QtWidgets.QLabel(self)
        self.opponentUserRatingDelta.setGeometry(QtCore.QRect(30, 180, 181, 16))
        self.opponentUserRatingDelta.setFont(font)
        self.opponentUserRatingDelta.setObjectName("opponentUserRatingDelta")

        font.setPointSize(18)
        font.setBold(True)

        self.PGNLabel = QtWidgets.QLabel(self)
        self.PGNLabel.setGeometry(QtCore.QRect(10, 220, 201, 18))
        self.PGNLabel.setFont(font)
        self.PGNLabel.setObjectName("PGNLabel")

        font.setPointSize(8)
        font.setBold(False)

        self.moveset = QtWidgets.QLabel(self)
        self.moveset.setGeometry(QtCore.QRect(10, 240, 201, 201))
        self.moveset.setFont(font)
        self.moveset.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.moveset.setWordWrap(True)
        self.moveset.setObjectName("moveset")

        font.setPointSize(16)
        font.setBold(True)

        self.drawButton = QtWidgets.QPushButton(self)
        self.drawButton.setGeometry(QtCore.QRect(10, 460, 201, 41))
        self.drawButton.setFont(font)
        self.drawButton.setObjectName("drawButton")

        self.drawButton.clicked.connect(lambda: requestDraw(dashboard))

        self.resignButton = QtWidgets.QPushButton(self)
        self.resignButton.setGeometry(QtCore.QRect(10, 500, 201, 41))
        self.resignButton.setFont(font)
        self.resignButton.setObjectName("resignButton")

        self.resignButton.clicked.connect(lambda: resign(dashboard))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def resetUi(self):
        self.userId = None
        self.userRating = None
        self.userUsername = None

        self.opponentId = None
        self.opponentRating = None
        self.opponentUsername = None

        self.currentUserLabel.setText("White:")
        self.opponentUserLabel.setText("Black:")

        self.currentUserRatingLabel.setText("Rating: ")
        self.opponentUserRatingLabel.setText("Rating: ")

        self.currentUserRatingDeltaArray = None
        self.opponentUserRatingDeltaArray = None

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.currentUserLabel.setText(_translate("pvpStage2Page", "current user:"))
        self.currentUserRatingLabel.setText(_translate("pvpStage2Page", "Rating"))
        self.currentUserRatingOutcome.setText(_translate("pvpStage2Page", "Rating Change:"))
        self.currentUserRatingDelta.setText(_translate("pvpStage2Page", "Win +5 / Draw +0 / Loss -1"))
        self.opponentUserLabel.setText(_translate("pvpStage2Page", "current user:"))
        self.opponentUserRatingLabel.setText(_translate("pvpStage2Page", "Rating"))
        self.opponentUserRatingOutcome.setText(_translate("pvpStage2Page", "Rating Change:"))
        self.opponentUserRatingDelta.setText(_translate("pvpStage2Page", "Win +5 / Draw +0 / Loss -1"))
        self.PGNLabel.setText(_translate("pvpStage2Page", "PGN:"))
        self.moveset.setText(_translate("pvpStage2Page", ""))
        self.drawButton.setText(_translate("pvpStage2Page", "Offer Draw"))
        self.resignButton.setText(_translate("pvpStage2Page", "Resign"))

