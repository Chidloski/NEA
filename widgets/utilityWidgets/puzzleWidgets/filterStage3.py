from PyQt5 import QtCore, QtGui, QtWidgets
from playerDB.jsonFunctions import *
from widgets.utilityWidgets.functions.puzzleFunctions import switchPuzzles, goToPuzzleWidget
from widgets.labelClasses import AutoResizingLabel


class Ui_filterStage3(QtWidgets.QWidget):

    def setupUi(self, dashboard):
        self.setObjectName("filterStage3")
        self.resize(230, 560)

        self.index = 0

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

        self.dailyPuzzleLabel = AutoResizingLabel(18, False, parent = self)
        self.dailyPuzzleLabel.setGeometry(QtCore.QRect(10, 100, 201, 21))
        self.dailyPuzzleLabel.setFont(font)
        self.dailyPuzzleLabel.setObjectName("dailyPuzzleLabel")

        self.outcomeLabel = AutoResizingLabel(18, False, parent = self)
        self.outcomeLabel.setGeometry(QtCore.QRect(10, 290, 201, 21))
        self.outcomeLabel.setFont(font)
        self.outcomeLabel.setObjectName("outcomeLabel")

        font.setPointSize(13)

        self.puzzleRatingLabel = AutoResizingLabel(13, False, parent = self)
        self.puzzleRatingLabel.setGeometry(QtCore.QRect(20, 130, 191, 21))
        self.puzzleRatingLabel.setFont(font)
        self.puzzleRatingLabel.setObjectName("puzzleRatingLabel")

        self.userOutcomeLabel = AutoResizingLabel(13, False, parent = self)
        self.userOutcomeLabel.setGeometry(QtCore.QRect(20, 320, 191, 21))
        self.userOutcomeLabel.setFont(font)
        self.userOutcomeLabel.setObjectName("userOutcomeLabel")

        self.solutionLabel = AutoResizingLabel(13, False, parent = self)
        self.solutionLabel.setGeometry(QtCore.QRect(20, 340, 191, 21))
        self.solutionLabel.setFont(font)
        self.solutionLabel.setObjectName("solutionLabel")

        self.pgnSolutionLabel = AutoResizingLabel(13, False, parent = self)
        self.pgnSolutionLabel.setGeometry(QtCore.QRect(30, 360, 181, 46))
        self.pgnSolutionLabel.setFont(font)
        self.pgnSolutionLabel.setWordWrap(True)
        self.pgnSolutionLabel.setObjectName("pgnSolutionLabel")

        font.setPointSize(18)
        font.setBold(True)

        self.backMoveButton = QtWidgets.QPushButton(self)
        self.backMoveButton.setGeometry(QtCore.QRect(30, 415, 71, 41))
        self.backMoveButton.setFont(font)
        self.backMoveButton.setObjectName("backMoveButton")
        self.backMoveButton.clicked.connect(lambda: self.resetPuzzle(dashboard))

        self.forwardMoveButton = QtWidgets.QPushButton(self)
        self.forwardMoveButton.setGeometry(QtCore.QRect(120, 415, 71, 41))
        self.forwardMoveButton.setFont(font)
        self.forwardMoveButton.setObjectName("forwardMoveButton")
        self.forwardMoveButton.clicked.connect(lambda: self.nextMove(dashboard))

        font.setPointSize(16)

        self.quitButton = QtWidgets.QPushButton(self)
        self.quitButton.setGeometry(QtCore.QRect(10, 510, 201, 41))
        self.quitButton.setFont(font)
        self.quitButton.setObjectName("quitButton")
        self.quitButton.clicked.connect(lambda: goToPuzzleWidget(dashboard))

        font.setPointSize(8)
        font.setBold(False)

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

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.currentUserLabel.setText(_translate("filterStage3", "Current User:"))
        self.currentUserPuzzleRatingLabel.setText(_translate("filterStage3", "Rating: 800 -> 900"))
        self.dailyPuzzleLabel.setText(_translate("filterStage3", "Puzzle:"))
        self.outcomeLabel.setText(_translate("filterStage3", "Outcome:"))
        self.puzzleRatingLabel.setText(_translate("filterStage3", "Rating: 800"))
        self.userOutcomeLabel.setText(_translate("filterStage3", "Completed!"))
        self.solutionLabel.setText(_translate("filterStage3", "Solution:"))
        self.pgnSolutionLabel.setText(_translate("filterStage3", "Qd4+ ... ... ... ... ... Rf1"))
        self.backMoveButton.setText(_translate("filterStage3", "<<-"))
        self.forwardMoveButton.setText(_translate("filterStage3", "->"))
        self.quitButton.setText(_translate("filterStage3", "Quit"))
        self.puzzle1Button.setText(_translate("filterStage3", "1000"))
        self.puzzle2Button.setText(_translate("filterStage3", "1000"))
        self.puzzle3Button.setText(_translate("filterStage3", "1000"))
        self.puzzle4Button.setText(_translate("filterStage3", "1000"))
        self.puzzle5Button.setText(_translate("filterStage3", "1000"))


    # populate the solution and update button colours
    def populate(self, dashboard, outcome, index):
        dashboard.puzzleChessBoard.resetUi()
        dashboard.puzzleChessBoard.coverScreen.setHidden(False)

        self.puzzleDict = dashboard.puzzleWidget.filterPuzzles[index]
        
        # run the until the start of the puzzle
        dashboard.puzzleChessBoard.runFen(self.puzzleDict["fen"])
        dashboard.puzzleChessBoard.runPgnTurn(dashboard.puzzleChessBoard.moveNumber, [self.puzzleDict["robotMove"]])

        self.index = 0

        userRecord = getData("users", id = dashboard.baseWindow.userId)
        userRecord = userRecord[0]

        self.currentUserLabel.setText(dashboard.filterStage2Widget.currentUserLabel.text())
        self.currentUserPuzzleRatingLabel.setText(f"Rating: {userRecord['puzzleRating']}")

        self.pgnSolutionLabel.setText(' '.join(self.puzzleDict["solution"]))

        # set the correct puzzle button in both filterStage2 and stage3 to the correct colour
        if outcome == "Completed!":
            self.userOutcomeLabel.setStyleSheet("color: rgb(50, 175, 61)")
            getattr(self, f"puzzle{index + 1}Button").setStyleSheet("color: rgb(50, 175, 61)")
            getattr(dashboard.filterStage2Widget, f"puzzle{index + 1}Button").setStyleSheet("color: rgb(50, 175, 61)")

        else:
            self.userOutcomeLabel.setStyleSheet("color: rgb(175, 61, 50)")
            getattr(self, f"puzzle{index + 1}Button").setStyleSheet("color: rgb(175, 61, 50)")
            getattr(dashboard.filterStage2Widget, f"puzzle{index + 1}Button").setStyleSheet("color: rgb(175, 61, 50)")

        self.userOutcomeLabel.setText(outcome)

        dashboard.puzzleStackedWidget.setCurrentIndex(4)


    # go back to start of puzzle
    def resetPuzzle(self, dashboard):
        dashboard.puzzleChessBoard.resetUi()
        dashboard.puzzleChessBoard.coverScreen.setHidden(False)

        dashboard.puzzleChessBoard.runFen(self.puzzleDict["fen"])
        dashboard.puzzleChessBoard.runPgnTurn(dashboard.puzzleChessBoard.moveNumber, [self.puzzleDict["robotMove"]])

        self.index = 0

    
    # run a move in the puzzle
    def nextMove(self, dashboard):
        if self.index < len(self.puzzleDict["solution"]):
            dashboard.puzzleChessBoard.runPgnTurn(dashboard.puzzleChessBoard.moveNumber, self.puzzleDict["solution"], self.index)

            self.index += 1
