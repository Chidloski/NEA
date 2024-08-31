from PyQt5 import QtCore, QtGui, QtWidgets
from widgets.utilityWidgets.functions.puzzleFunctions import goToPuzzleWidget


class Ui_dailyStage3(QtWidgets.QWidget):

    def setupUi(self, dashboard):
        self.setObjectName("dailyStage3")
        self.resize(230, 560)

        self.moveList = ""
        self.solution = ""

        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(18)

        self.currentUserLabel = QtWidgets.QLabel(self)
        self.currentUserLabel.setGeometry(QtCore.QRect(10, 10, 201, 21))
        self.currentUserLabel.setFont(font)
        self.currentUserLabel.setObjectName("currentUserLabel")

        font.setPointSize(13)

        self.currentUserRatingLabel = QtWidgets.QLabel(self)
        self.currentUserRatingLabel.setGeometry(QtCore.QRect(20, 30, 191, 21))
        self.currentUserRatingLabel.setFont(font)
        self.currentUserRatingLabel.setObjectName("currentUserRatingLabel")

        font.setPointSize(18)

        self.dailyPuzzleLabel = QtWidgets.QLabel(self)
        self.dailyPuzzleLabel.setGeometry(QtCore.QRect(10, 90, 201, 21))
        self.dailyPuzzleLabel.setFont(font)
        self.dailyPuzzleLabel.setObjectName("dailyPuzzleLabel")

        font.setPointSize(13)

        self.tournamentLabel = QtWidgets.QLabel(self)
        self.tournamentLabel.setGeometry(QtCore.QRect(20, 120, 191, 21))
        self.tournamentLabel.setFont(font)
        self.tournamentLabel.setObjectName("tournamentLabel")

        font.setPointSize(13)

        self.matchupLabel = QtWidgets.QLabel(self)
        self.matchupLabel.setGeometry(QtCore.QRect(20, 140, 191, 21))
        self.matchupLabel.setFont(font)
        self.matchupLabel.setObjectName("matchupLabel")

        self.puzzleRatingLabel = QtWidgets.QLabel(self)
        self.puzzleRatingLabel.setGeometry(QtCore.QRect(20, 160, 191, 21))
        self.puzzleRatingLabel.setFont(font)
        self.puzzleRatingLabel.setObjectName("puzzleRatingLabel")

        font.setPointSize(18)

        self.outcomeLabel = QtWidgets.QLabel(self)
        self.outcomeLabel.setGeometry(QtCore.QRect(10, 210, 201, 21))
        self.outcomeLabel.setFont(font)
        self.outcomeLabel.setObjectName("outcomeLabel")

        font.setPointSize(13)

        self.userOutcomeLabel = QtWidgets.QLabel(self)
        self.userOutcomeLabel.setGeometry(QtCore.QRect(20, 240, 191, 21))
        self.userOutcomeLabel.setFont(font)
        self.userOutcomeLabel.setObjectName("userOutcomeLabel")

        self.solutionLabel = QtWidgets.QLabel(self)
        self.solutionLabel.setGeometry(QtCore.QRect(20, 260, 191, 21))
        self.solutionLabel.setFont(font)
        self.solutionLabel.setObjectName("solutionLabel")

        self.pgnSolutionLabel = QtWidgets.QLabel(self)
        self.pgnSolutionLabel.setGeometry(QtCore.QRect(30, 280, 181, 41))
        self.pgnSolutionLabel.setFont(font)
        self.pgnSolutionLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.pgnSolutionLabel.setWordWrap(True)
        self.pgnSolutionLabel.setObjectName("pgnSolutionLabel")

        font.setPointSize(18)
        font.setBold(True)

        self.backButton = QtWidgets.QPushButton(self)
        self.backButton.setGeometry(QtCore.QRect(10, 510, 201, 41))
        self.backButton.setFont(font)
        self.backButton.setObjectName("backButton")
        self.backButton.clicked.connect(lambda: goToPuzzleWidget(dashboard))

        self.backMoveButton = QtWidgets.QPushButton(self)
        self.backMoveButton.setGeometry(QtCore.QRect(30, 320, 71, 41))
        self.backMoveButton.setFont(font)
        self.backMoveButton.setObjectName("backMoveButton")
        self.backMoveButton.clicked.connect(lambda: self.reRunPgn(dashboard))

        self.index = 0

        self.forwardMoveButton = QtWidgets.QPushButton(self)
        self.forwardMoveButton.setGeometry(QtCore.QRect(120, 320, 71, 41))
        self.forwardMoveButton.setFont(font)
        self.forwardMoveButton.setObjectName("forwardMoveButton")
        self.forwardMoveButton.clicked.connect(lambda: self.nextMove(dashboard))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.currentUserLabel.setText(_translate("dailyStage3", "Current User:"))
        self.currentUserRatingLabel.setText(_translate("dailyStage3", "Rating: 800 -> 820"))
        self.dailyPuzzleLabel.setText(_translate("dailyStage3", "Daily Puzzle:"))
        self.tournamentLabel.setText(_translate("dailyStage3", "Tournament"))
        self.matchupLabel.setText(_translate("dailyStage3", "Niemann Vs Carlsen"))
        self.puzzleRatingLabel.setText(_translate("dailyStage3", "Rating: "))
        self.outcomeLabel.setText(_translate("dailyStage3", "Outcome:"))
        self.userOutcomeLabel.setText(_translate("dailyStage3", "Win / Loss"))
        self.solutionLabel.setText(_translate("dailyStage3", "Solution:"))
        self.pgnSolutionLabel.setText(_translate("dailyStage3", "e4 e5"))
        self.backButton.setText(_translate("dailyStage3", "Back"))
        self.backMoveButton.setText(_translate("dailyStage3", "<<-"))
        self.forwardMoveButton.setText(_translate("dailyStage3", "->"))

    def reRunPgn(self, dashboard):
        dashboard.puzzleChessBoard.resetUi()
        dashboard.puzzleChessBoard.coverScreen.setHidden(False)

        dashboard.puzzleChessBoard.runPgn(self.moveList)

        self.index = 0

    def nextMove(self, dashboard):
        if self.index < len(self.solution):
            dashboard.puzzleChessBoard.runPgnTurn(dashboard.puzzleChessBoard.moveNumber, self.solution, self.index)

            self.index += 1

    def resetUi(self):
        self.currentUserLabel.setText("Current User:")
        self.currentUserRatingLabel.setText("Rating: 800 -> 820")
        self.dailyPuzzleLabel.setText("Daily Puzzle:")
        self.tournamentLabel.setText("Tournament")
        self.matchupLabel.setText("Niemann Vs Carlsen")
        self.puzzleRatingLabel.setText("Rating: ")
        self.outcomeLabel.setText("Outcome:")
        self.userOutcomeLabel.setText("Win / Loss")
        self.solutionLabel.setText("Solution:")
        self.pgnSolutionLabel.setText("e4 e5")
        self.backButton.setText("Back")
        self.backMoveButton.setText("<<-")
        self.forwardMoveButton.setText("->")

        self.moveList = ""
        self.solution = ""
        self.index = 0
        


 