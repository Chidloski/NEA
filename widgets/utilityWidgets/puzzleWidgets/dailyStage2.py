from PyQt5 import QtCore, QtGui, QtWidgets
from widgets.utilityWidgets.functions.puzzleFunctions import goToPuzzleWidget


class Ui_dailyStage2(QtWidgets.QWidget):

    def setupUi(self, dashboard):
        self.setObjectName("dailyStage2")
        self.resize(230, 560)

        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(18)

        self.currentUserLabel = QtWidgets.QLabel(self)
        self.currentUserLabel.setGeometry(QtCore.QRect(10, 10, 201, 16))
        self.currentUserLabel.setFont(font)
        self.currentUserLabel.setObjectName("currentUserLabel")

        font.setPointSize(13)

        self.currentUserPuzzleRatingLabel = QtWidgets.QLabel(self)
        self.currentUserPuzzleRatingLabel.setGeometry(QtCore.QRect(20, 30, 191, 16))
        self.currentUserPuzzleRatingLabel.setFont(font)
        self.currentUserPuzzleRatingLabel.setObjectName("currentUserPuzzleRatingLabel")

        font.setPointSize(18)

        self.dailyPuzzleLabel = QtWidgets.QLabel(self)
        self.dailyPuzzleLabel.setGeometry(QtCore.QRect(10, 90, 201, 16))
        self.dailyPuzzleLabel.setFont(font)
        self.dailyPuzzleLabel.setObjectName("dailyPuzzleLabel")

        font.setPointSize(13)

        self.matchupLabel = QtWidgets.QLabel(self)
        self.matchupLabel.setGeometry(QtCore.QRect(20, 140, 191, 16))
        self.matchupLabel.setFont(font)
        self.matchupLabel.setObjectName("matchupLabel")

        self.puzzleRatingLabel = QtWidgets.QLabel(self)
        self.puzzleRatingLabel.setGeometry(QtCore.QRect(20, 160, 191, 16))
        self.puzzleRatingLabel.setFont(font)
        self.puzzleRatingLabel.setObjectName("puzzleRatingLabel")

        self.outcomeDeltaLabel = QtWidgets.QLabel(self)
        self.outcomeDeltaLabel.setGeometry(QtCore.QRect(20, 210, 191, 16))
        self.outcomeDeltaLabel.setFont(font)
        self.outcomeDeltaLabel.setObjectName("outcomeDeltaLabel")

        font.setPointSize(11)

        self.deltaLabel = QtWidgets.QLabel(self)
        self.deltaLabel.setGeometry(QtCore.QRect(30, 230, 191, 16))
        self.deltaLabel.setFont(font)
        self.deltaLabel.setObjectName("deltaLabel")
        
        font.setPointSize(13)

        self.tournamentLabel = QtWidgets.QLabel(self)
        self.tournamentLabel.setGeometry(QtCore.QRect(20, 120, 191, 16))
        self.tournamentLabel.setFont(font)
        self.tournamentLabel.setObjectName("tournamentLabel")

        self.movesLabel = QtWidgets.QLabel(self)
        self.movesLabel.setGeometry(QtCore.QRect(20, 180, 191, 16))
        self.movesLabel.setFont(font)
        self.movesLabel.setObjectName("movesLabel")

        font.setPointSize(16)
        font.setBold(True)

        self.quitButton = QtWidgets.QPushButton(self)
        self.quitButton.setGeometry(QtCore.QRect(10, 510, 201, 41))
        self.quitButton.setFont(font)
        self.quitButton.setObjectName("quitButton")

        self.quitButton.clicked.connect(lambda: goToPuzzleWidget(dashboard))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.currentUserLabel.setText(_translate("dailyStage2", "Current User:"))
        self.currentUserPuzzleRatingLabel.setText(_translate("dailyStage2", "Puzzle Rating: "))
        self.dailyPuzzleLabel.setText(_translate("dailyStage2", "Daily Puzzle:"))
        self.matchupLabel.setText(_translate("dailyStage2", "Niemann Vs Carlsen"))
        self.puzzleRatingLabel.setText(_translate("dailyStage2", "Rating:"))
        self.outcomeDeltaLabel.setText(_translate("dailyStage2", "Possible Outcomes:"))
        self.deltaLabel.setText(_translate("dailyStage2", "Success +100 / Loss -200"))
        self.tournamentLabel.setText(_translate("dailyStage2", "Tournament"))
        self.movesLabel.setText(_translate("dailyStage2", "Moves to Make:"))
        self.quitButton.setText(_translate("dailyStage2", "Quit"))

    def resetUi(self):
        self.currentUserLabel.setText("Current User:")
        self.currentUserPuzzleRatingLabel.setText("Puzzle Rating: ")
        self.dailyPuzzleLabel.setText("Daily Puzzle:")
        self.matchupLabel.setText("Niemann Vs Carlsen")
        self.puzzleRatingLabel.setText("Rating:")
        self.outcomeDeltaLabel.setText("Possible Outcomes:")
        self.deltaLabel.setText("Success +100 / Loss -200")
        self.tournamentLabel.setText("Tournament")
        self.movesLabel.setText("Moves to Make:")
        self.quitButton.setText("Quit")

        self.puzzleRating = 0
        self.solution = ""
        self.moveList = ""
        self.currentMove = 0
        self.moves = 0
        self.ratingDelta = []
        self.currentUserPuzzleRating = 0

