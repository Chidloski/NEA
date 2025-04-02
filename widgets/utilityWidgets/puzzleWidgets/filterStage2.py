from PyQt5 import QtCore, QtGui, QtWidgets
from playerDB.jsonFunctions import *
from widgets.utilityWidgets.functions.playFunctions import ratingChange
from widgets.utilityWidgets.functions.puzzleFunctions import switchPuzzles, goToPuzzleWidget
from widgets.labelClasses import AutoResizingLabel


class Ui_filterStage2(QtWidgets.QWidget):

    def setupUi(self, dashboard):
        self.setObjectName("filterStage2")
        self.resize(230, 560)

        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(18)

        self.currentUserLabel = AutoResizingLabel(18, False, parent = self)
        self.currentUserLabel.setGeometry(QtCore.QRect(10, 10, 201, 21))
        self.currentUserLabel.setFont(font)
        self.currentUserLabel.setObjectName("currentUserLabel")

        font.setPointSize(13)

        self.currentUserPuzzleRatingLabel = AutoResizingLabel(13, False, parent = self)
        self.currentUserPuzzleRatingLabel.setGeometry(QtCore.QRect(20, 30, 191, 21))
        self.currentUserPuzzleRatingLabel.setFont(font)
        self.currentUserPuzzleRatingLabel.setObjectName("currentUserPuzzleRatingLabel")

        font.setPointSize(18)

        self.puzzleLabel = AutoResizingLabel(18, False, parent = self)
        self.puzzleLabel.setGeometry(QtCore.QRect(10, 110, 201, 21))
        self.puzzleLabel.setFont(font)
        self.puzzleLabel.setObjectName("puzzleLabel")

        font.setPointSize(13)

        self.puzzleRatingLabel = AutoResizingLabel(13, False, parent = self)
        self.puzzleRatingLabel.setGeometry(QtCore.QRect(20, 140, 191, 21))
        self.puzzleRatingLabel.setFont(font)
        self.puzzleRatingLabel.setObjectName("puzzleRatingLabel")

        self.movesLabel = AutoResizingLabel(13, False, parent = self)
        self.movesLabel.setGeometry(QtCore.QRect(20, 160, 191, 21))
        self.movesLabel.setFont(font)
        self.movesLabel.setObjectName("movesLabel")

        self.outcomeDeltaLabel = AutoResizingLabel(13, False, parent = self)
        self.outcomeDeltaLabel.setGeometry(QtCore.QRect(20, 190, 191, 21))
        self.outcomeDeltaLabel.setFont(font)
        self.outcomeDeltaLabel.setObjectName("outcomeDeltaLabel")

        self.deltaLabel = AutoResizingLabel(13, False, parent = self)
        self.deltaLabel.setGeometry(QtCore.QRect(30, 210, 181, 21))
        self.deltaLabel.setFont(font)
        self.deltaLabel.setObjectName("deltaLabel")

        font.setPointSize(8)

        self.puzzle1Button = QtWidgets.QPushButton(self)
        self.puzzle1Button.setGeometry(QtCore.QRect(93, 250, 50, 32))
        self.puzzle1Button.setFont(font)
        self.puzzle1Button.setObjectName("puzzle1Button")
        self.puzzle1Button.active = False
        self.puzzle1Button.setHidden(True)
        self.puzzle1Button.clicked.connect(lambda: switchPuzzles(dashboard, 0))

        self.puzzle2Button = QtWidgets.QPushButton(self)
        self.puzzle2Button.setGeometry(QtCore.QRect(52, 250, 50, 32))
        self.puzzle2Button.setFont(font)
        self.puzzle2Button.setObjectName("puzzle2Button")
        self.puzzle2Button.active = False
        self.puzzle2Button.setHidden(True)
        self.puzzle2Button.clicked.connect(lambda: switchPuzzles(dashboard, 1))

        self.puzzle3Button = QtWidgets.QPushButton(self)
        self.puzzle3Button.setGeometry(QtCore.QRect(134, 250, 50, 32))
        self.puzzle3Button.setFont(font)
        self.puzzle3Button.setObjectName("puzzle3Button")
        self.puzzle3Button.active = False
        self.puzzle3Button.setHidden(True)
        self.puzzle3Button.clicked.connect(lambda: switchPuzzles(dashboard, 2))

        self.puzzle4Button = QtWidgets.QPushButton(self)
        self.puzzle4Button.setGeometry(QtCore.QRect(11, 250, 50, 32))
        self.puzzle4Button.setFont(font)
        self.puzzle4Button.setObjectName("puzzle4Button")
        self.puzzle4Button.active = False
        self.puzzle4Button.setHidden(True)
        self.puzzle4Button.clicked.connect(lambda: switchPuzzles(dashboard, 3))

        self.puzzle5Button = QtWidgets.QPushButton(self)
        self.puzzle5Button.setGeometry(QtCore.QRect(175, 250, 50, 32))
        self.puzzle5Button.setFont(font)
        self.puzzle5Button.setObjectName("puzzle5Button")
        self.puzzle5Button.active = False
        self.puzzle5Button.setHidden(True)
        self.puzzle5Button.clicked.connect(lambda: switchPuzzles(dashboard, 4))

        font.setPointSize(16)
        font.setBold(True)

        self.quitButton = QtWidgets.QPushButton(self)
        self.quitButton.setGeometry(QtCore.QRect(10, 511, 201, 41))
        self.quitButton.setFont(font)
        self.quitButton.setObjectName("quitButton")
        self.quitButton.clicked.connect(lambda: goToPuzzleWidget(dashboard))


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.currentUserLabel.setText(_translate("filterStage2", "User:"))
        self.currentUserPuzzleRatingLabel.setText(_translate("filterStage2", "Puzzle Rating: 800"))
        self.puzzleLabel.setText(_translate("filterStage2", "Puzzle:"))
        self.puzzleRatingLabel.setText(_translate("filterStage2", "Rating: 800"))
        self.movesLabel.setText(_translate("filterStage2", "Moves to Make: 3"))
        self.outcomeDeltaLabel.setText(_translate("filterStage2", "Possible Outcomes:"))
        self.deltaLabel.setText(_translate("filterStage2", "Success +0 / Loss -0"))
        self.puzzle1Button.setText(_translate("filterStage2", "1000"))
        self.puzzle2Button.setText(_translate("filterStage2", "2100"))
        self.puzzle3Button.setText(_translate("filterStage2", "1500"))
        self.puzzle4Button.setText(_translate("filterStage2", "1800"))
        self.puzzle5Button.setText(_translate("filterStage2", "2200"))
        self.quitButton.setText(_translate("filterStage2", "Quit"))


    def populate(self, dashboard, index):
        self.index = index

        userQuery = {"id": dashboard.baseWindow.userId}
        userData = getData("users", **userQuery)
        userData = userData[0]

        username = userData["username"]
        self.userPuzzleRating = userData["puzzleRating"]

        self.currentUserLabel.setText(f"User: {username}")
        self.currentUserPuzzleRatingLabel.setText(f"Puzzle Rating: {self.userPuzzleRating}")

        self.puzzleDict = dashboard.puzzleWidget.filterPuzzles[index]

        self.puzzleRatingLabel.setText(f"Rating: {self.puzzleDict['rating']}")
        self.movesLabel.setText(f"Moves to Make: {(len(self.puzzleDict['solution']) // 2) + 1}")

        self.ratingDelta = [ratingChange(self.userPuzzleRating, self.puzzleDict['rating'], 1, 100), ratingChange(self.userPuzzleRating, self.puzzleDict['rating'], 0, 100)]
        self.deltaLabel.setText(f"Success {'+' if self.ratingDelta[0] >= 0 else ''}{self.ratingDelta[0]} / Loss {'+' if self.ratingDelta[1] >= 0 else ''}{self.ratingDelta[1]}")

        self.currentMove = 0
        self.solution = self.puzzleDict["solution"]

        # run fen, run robot move, cover screen
        dashboard.puzzleChessBoard.runFen(self.puzzleDict["fen"])
        dashboard.puzzleChessBoard.runPgnTurn(dashboard.puzzleChessBoard.moveNumber, [self.puzzleDict["robotMove"]])

        dashboard.puzzleChessBoard.coverScreen.setHidden(True)