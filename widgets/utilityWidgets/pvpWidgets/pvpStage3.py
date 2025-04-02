from PyQt5 import QtCore, QtGui, QtWidgets
from widgets.utilityWidgets.functions.playFunctions import goToStage2, goToStage1
from widgets.labelClasses import AutoResizingLabel, AutoResizingRadioButton

class Ui_PvpStage3(QtWidgets.QWidget):

    def setupUi(self, dashboard, baseWindow):
        # sizing of the widget
        self.setObjectName("pvpStage3Page")
        self.resize(230, 560)
        self.setAutoFillBackground(False)

        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(18)
        font.setBold(True)

        self.currentUserLabel = AutoResizingLabel(18, True, parent = self)
        self.currentUserLabel.setGeometry(QtCore.QRect(10, 10, 201, 16))
        self.currentUserLabel.setFont(font)
        self.currentUserLabel.setObjectName("currentUserLabel")

        font.setPointSize(13)
        font.setBold(False)

        self.currentUserRatingChange = AutoResizingLabel(13, False, parent = self)
        self.currentUserRatingChange.setGeometry(QtCore.QRect(30, 50, 181, 16))
        self.currentUserRatingChange.setFont(font)
        self.currentUserRatingChange.setObjectName("currentUserRatingChange")

        self.currentUserRating = AutoResizingLabel(13, False, parent = self)
        self.currentUserRating.setGeometry(QtCore.QRect(20, 30, 181, 16))
        self.currentUserRating.setFont(font)
        self.currentUserRating.setObjectName("currentUserRating")

        font.setPointSize(18)
        font.setBold(True)

        self.opponentLabel = AutoResizingLabel(18, True, parent = self)
        self.opponentLabel.setGeometry(QtCore.QRect(10, 110, 201, 16))
        self.opponentLabel.setFont(font)
        self.opponentLabel.setObjectName("opponentLabel")

        font.setPointSize(13)
        font.setBold(False)

        self.opponentUserRating = AutoResizingLabel(13, False, parent = self)
        self.opponentUserRating.setGeometry(QtCore.QRect(20, 130, 181, 16))
        self.opponentUserRating.setFont(font)
        self.opponentUserRating.setObjectName("opponentUserRating")

        self.opponentUserRatingChange = AutoResizingLabel(13, False, parent = self)
        self.opponentUserRatingChange.setGeometry(QtCore.QRect(30, 150, 181, 16))
        self.opponentUserRatingChange.setFont(font)
        self.opponentUserRatingChange.setObjectName("opponentUserRatingChange")

        font.setPointSize(18)
        font.setBold(True)

        self.PGNLabel = AutoResizingLabel(18, True, parent = self)
        self.PGNLabel.setGeometry(QtCore.QRect(10, 210, 201, 16))
        self.PGNLabel.setFont(font)
        self.PGNLabel.setObjectName("PGNLabel")

        font.setPointSize(8)
        font.setBold(False)

        self.moveset = AutoResizingLabel(8, False, wordWrap=True, parent = self)
        self.moveset.setGeometry(QtCore.QRect(10, 230, 201, 201))
        self.moveset.setFont(font)
        self.moveset.setObjectName("moveset")
        self.moveset.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.moveset.setWordWrap(True)

        font.setPointSize(13)

        self.copyMovesetButton = QtWidgets.QPushButton(self)
        self.copyMovesetButton.setGeometry(QtCore.QRect(40, 430, 141, 32))
        self.copyMovesetButton.setFont(font)
        self.copyMovesetButton.setObjectName("copyMovesetButton")

        font.setPointSize(16)
        font.setBold(True)

        self.rematchButton = QtWidgets.QPushButton(self)
        self.rematchButton.setGeometry(QtCore.QRect(10, 460, 201, 41))
        self.rematchButton.setFont(font)
        self.rematchButton.setObjectName("rematchButton")

        self.rematchButton.clicked.connect(lambda: goToStage2(dashboard, dashboard.pvpStage2Widget.userId, dashboard.pvpStage2Widget.opponentId))

        self.newMatchButton = QtWidgets.QPushButton(self)
        self.newMatchButton.setGeometry(QtCore.QRect(10, 500, 201, 41))
        self.newMatchButton.setFont(font)
        self.newMatchButton.setObjectName("newMatchButton")

        self.newMatchButton.clicked.connect(lambda: goToStage1(dashboard))



        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def resetUi(self):
        self.currentUserLabel.setText("")
        self.opponentLabel.setText("")

        self.currentRating = None
        self.opponentRating = None

        self.currentUserRatingChange.setText("")
        self.opponentUserRatingChange.setText("")

        self.moveset.setText("")

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.currentUserLabel.setText(_translate("pvpStage3Page", "Current User:"))
        self.currentUserRatingChange.setText(_translate("pvpStage3Page", "1000 -> 998"))
        self.currentUserRating.setText(_translate("pvpStage3Page", "Rating:"))
        self.opponentLabel.setText(_translate("pvpStage3Page", "Opponent:"))
        self.opponentUserRating.setText(_translate("pvpStage3Page", "Rating:"))
        self.opponentUserRatingChange.setText(_translate("pvpStage3Page", "1000 -> 998"))
        self.PGNLabel.setText(_translate("pvpStage3Page", "PGN:"))
        self.moveset.setText(_translate("pvpStage3Page", "TextLabel"))
        self.copyMovesetButton.setText(_translate("pvpStage3Page", "Copy Moveset"))
        self.rematchButton.setText(_translate("pvpStage3Page", "Rematch"))
        self.newMatchButton.setText(_translate("pvpStage3Page", "New Match"))
