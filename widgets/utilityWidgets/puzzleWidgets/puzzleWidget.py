from PyQt5 import QtCore, QtGui, QtWidgets
from playerDB.jsonFunctions import *
from widgets.utilityWidgets.functions.puzzleFunctions import getDailyPuzzle, goToDaily


class Ui_PuzzleWidget(QtWidgets.QWidget):

    def setupUi(self, dashboard):
        self.setObjectName("puzzleWidget")
        self.resize(230, 560)

        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(18)
        font.setBold(False)

        self.currentUserLabel = QtWidgets.QLabel(self)
        self.currentUserLabel.setGeometry(QtCore.QRect(10, 10, 201, 21))
        self.currentUserLabel.setFont(font)
        self.currentUserLabel.setObjectName("currentUserLabel")

        font.setPointSize(13)

        self.currentUserPuzzleRatingLabel = QtWidgets.QLabel(self)
        self.currentUserPuzzleRatingLabel.setGeometry(QtCore.QRect(20, 30, 191, 21))
        self.currentUserPuzzleRatingLabel.setFont(font)
        self.currentUserPuzzleRatingLabel.setObjectName("currentUserPuzzleRatingLabel")

        font.setPointSize(18)

        self.filtersLabel = QtWidgets.QLabel(self)
        self.filtersLabel.setGeometry(QtCore.QRect(10, 70, 201, 21))
        self.filtersLabel.setFont(font)
        self.filtersLabel.setObjectName("filtersLabel")

        font.setPointSize(13)

        self.openingRadioButton = QtWidgets.QRadioButton(self)
        self.openingRadioButton.setGeometry(QtCore.QRect(20, 110, 99, 20))
        self.openingRadioButton.setFont(font)
        self.openingRadioButton.setObjectName("openingRadioButton")

        self.midgameRadioButton = QtWidgets.QRadioButton(self)
        self.midgameRadioButton.setGeometry(QtCore.QRect(20, 130, 99, 20))
        self.midgameRadioButton.setFont(font)
        self.midgameRadioButton.setObjectName("midgameRadioButton")

        self.endgameRadioButton = QtWidgets.QRadioButton(self)
        self.endgameRadioButton.setGeometry(QtCore.QRect(20, 150, 99, 20))
        self.endgameRadioButton.setFont(font)
        self.endgameRadioButton.setObjectName("endgameRadioButton")

        self.forkRadioButton = QtWidgets.QRadioButton(self)
        self.forkRadioButton.setGeometry(QtCore.QRect(120, 110, 91, 20))
        self.forkRadioButton.setFont(font)
        self.forkRadioButton.setObjectName("forkRadioButton")

        self.pinRadio = QtWidgets.QRadioButton(self)
        self.pinRadio.setGeometry(QtCore.QRect(120, 130, 91, 20))
        self.pinRadio.setFont(font)
        self.pinRadio.setObjectName("pinRadio")

        self.positionLabel = QtWidgets.QLabel(self)
        self.positionLabel.setGeometry(QtCore.QRect(20, 90, 71, 21))
        self.positionLabel.setFont(font)
        self.positionLabel.setObjectName("positionLabel")

        self.motifLabel = QtWidgets.QLabel(self)
        self.motifLabel.setGeometry(QtCore.QRect(120, 90, 71, 21))
        self.motifLabel.setFont(font)
        self.motifLabel.setObjectName("motifLabel")

        self.tradeLabel = QtWidgets.QRadioButton(self)
        self.tradeLabel.setGeometry(QtCore.QRect(120, 150, 91, 20))
        self.tradeLabel.setFont(font)
        self.tradeLabel.setObjectName("tradeLabel")

        self.taskLabel = QtWidgets.QLabel(self)
        self.taskLabel.setGeometry(QtCore.QRect(20, 180, 71, 21))
        self.taskLabel.setFont(font)
        self.taskLabel.setObjectName("taskLabel")

        self.winRadioButton = QtWidgets.QRadioButton(self)
        self.winRadioButton.setGeometry(QtCore.QRect(20, 200, 99, 20))
        self.winRadioButton.setFont(font)
        self.winRadioButton.setObjectName("winRadioButton")

        self.drawRadioButton = QtWidgets.QRadioButton(self)
        self.drawRadioButton.setGeometry(QtCore.QRect(20, 220, 99, 20))
        self.drawRadioButton.setFont(font)
        self.drawRadioButton.setObjectName("drawRadioButton")

        self.defendRadioButton = QtWidgets.QRadioButton(self)
        self.defendRadioButton.setGeometry(QtCore.QRect(20, 240, 99, 20))
        self.defendRadioButton.setFont(font)
        self.defendRadioButton.setObjectName("defendRadioButton")

        self.colourLabel = QtWidgets.QLabel(self)
        self.colourLabel.setGeometry(QtCore.QRect(120, 180, 71, 21))
        self.colourLabel.setFont(font)
        self.colourLabel.setObjectName("colourLabel")

        self.whiteRadioButton = QtWidgets.QRadioButton(self)
        self.whiteRadioButton.setGeometry(QtCore.QRect(120, 200, 99, 20))
        self.whiteRadioButton.setFont(font)
        self.whiteRadioButton.setObjectName("whiteRadioButton")

        self.blackRadioButton = QtWidgets.QRadioButton(self)
        self.blackRadioButton.setGeometry(QtCore.QRect(120, 220, 99, 20))
        self.blackRadioButton.setFont(font)
        self.blackRadioButton.setObjectName("blackRadioButton")

        self.ratingSlider = QtWidgets.QSlider(self)
        self.ratingSlider.setGeometry(QtCore.QRect(20, 290, 181, 25))
        self.ratingSlider.setFont(font)
        self.ratingSlider.setMinimum(400)
        self.ratingSlider.setMaximum(2800)
        self.ratingSlider.setSliderPosition(800)
        self.ratingSlider.setOrientation(QtCore.Qt.Horizontal)
        self.ratingSlider.setInvertedAppearance(False)
        self.ratingSlider.setTickInterval(0)
        self.ratingSlider.setObjectName("ratingSlider")

        self.ratingLabel = QtWidgets.QLabel(self)
        self.ratingLabel.setGeometry(QtCore.QRect(70, 270, 91, 21))
        self.ratingLabel.setFont(font)
        self.ratingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ratingLabel.setObjectName("ratingLabel")

        self.numOfPuzzleSlider = QtWidgets.QSlider(self)
        self.numOfPuzzleSlider.setGeometry(QtCore.QRect(20, 340, 181, 25))
        self.numOfPuzzleSlider.setFont(font)
        self.numOfPuzzleSlider.setMinimum(1)
        self.numOfPuzzleSlider.setMaximum(5)
        self.numOfPuzzleSlider.setProperty("value", 3)
        self.numOfPuzzleSlider.setSliderPosition(3)
        self.numOfPuzzleSlider.setOrientation(QtCore.Qt.Horizontal)
        self.numOfPuzzleSlider.setInvertedAppearance(False)
        self.numOfPuzzleSlider.setTickInterval(0)
        self.numOfPuzzleSlider.setObjectName("horizontalSlider_2")

        self.numOfPuzzlesLabel = QtWidgets.QLabel(self)
        self.numOfPuzzlesLabel.setGeometry(QtCore.QRect(40, 320, 151, 21))
        self.numOfPuzzlesLabel.setFont(font)
        self.numOfPuzzlesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.numOfPuzzlesLabel.setObjectName("numOfPuzzlesLabel")

        font.setPointSize(18)
        font.setBold(True)

        self.getPuzzlesButton = QtWidgets.QPushButton(self)
        self.getPuzzlesButton.setGeometry(QtCore.QRect(20, 370, 181, 41))
        self.getPuzzlesButton.setFont(font)
        self.getPuzzlesButton.setObjectName("getPuzzlesButton")

        font.setBold(False)

        self.dailyPuzzleLabel = QtWidgets.QLabel(self)
        self.dailyPuzzleLabel.setGeometry(QtCore.QRect(10, 430, 201, 21))
        self.dailyPuzzleLabel.setFont(font)
        self.dailyPuzzleLabel.setObjectName("dailyPuzzleLabel")

        font.setPointSize(13)

        self.matchupLabel = QtWidgets.QLabel(self)
        self.matchupLabel.setGeometry(QtCore.QRect(20, 450, 191, 21))
        self.matchupLabel.setFont(font)
        self.matchupLabel.setObjectName("matchupLabel")

        self.dailyRatingLabel = QtWidgets.QLabel(self)
        self.dailyRatingLabel.setGeometry(QtCore.QRect(20, 470, 191, 21))
        self.dailyRatingLabel.setFont(font)
        self.dailyRatingLabel.setObjectName("dailyRatingLabel")

        font.setPointSize(18)
        font.setBold(True)

        self.dailyPuzzleButton = QtWidgets.QPushButton(self)
        self.dailyPuzzleButton.setGeometry(QtCore.QRect(20, 500, 181, 41))
        self.dailyPuzzleButton.setFont(font)
        self.dailyPuzzleButton.setObjectName("dailyPuzzleButton")
        self.dailyPuzzleButton.clicked.connect(lambda: goToDaily(dashboard))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.currentUserLabel.setText(_translate("puzzleWidget", "Current User:"))
        self.currentUserPuzzleRatingLabel.setText(_translate("puzzleWidget", "Puzzle Rating:"))
        self.filtersLabel.setText(_translate("puzzleWidget", "Filters:"))
        self.openingRadioButton.setText(_translate("puzzleWidget", "opening"))
        self.midgameRadioButton.setText(_translate("puzzleWidget", "midgame"))
        self.endgameRadioButton.setText(_translate("puzzleWidget", "endgame"))
        self.forkRadioButton.setText(_translate("puzzleWidget", "fork"))
        self.pinRadio.setText(_translate("puzzleWidget", "pin"))
        self.positionLabel.setText(_translate("puzzleWidget", "Position:"))
        self.motifLabel.setText(_translate("puzzleWidget", "Motif:"))
        self.tradeLabel.setText(_translate("puzzleWidget", "trade"))
        self.taskLabel.setText(_translate("puzzleWidget", "Task:"))
        self.winRadioButton.setText(_translate("puzzleWidget", "win"))
        self.drawRadioButton.setText(_translate("puzzleWidget", "draw"))
        self.defendRadioButton.setText(_translate("puzzleWidget", "defend"))
        self.colourLabel.setText(_translate("puzzleWidget", "Colour:"))
        self.whiteRadioButton.setText(_translate("puzzleWidget", "white"))
        self.blackRadioButton.setText(_translate("puzzleWidget", "black"))
        self.ratingLabel.setText(_translate("puzzleWidget", "Rating:"))
        self.numOfPuzzlesLabel.setText(_translate("puzzleWidget", "Number of Puzzles:"))
        self.getPuzzlesButton.setText(_translate("puzzleWidget", "Get Puzzles"))
        self.dailyPuzzleLabel.setText(_translate("puzzleWidget", "Daily Puzzle:"))
        self.matchupLabel.setText(_translate("puzzleWidget", "Niemman Vs Carlsen"))
        self.dailyRatingLabel.setText(_translate("puzzleWidget", "Rating:"))
        self.dailyPuzzleButton.setText(_translate("puzzleWidget", "Daily Puzzle"))

    def populate(self, userId):
        user = getData("users", id = userId)
        queryStatus, *_, matchup,  puzzleRating = getDailyPuzzle()

        self.currentUserLabel.setText(user[0]["username"] + ":")
        self.currentUserPuzzleRatingLabel.setText(f"Puzzle Rating : {user[0]['puzzleRating']}")

        if queryStatus == 200:
            self.matchupLabel.setText(matchup)
            self.dailyRatingLabel.setText(f"Rating: {puzzleRating}")

        else:
            self.dailyRatingLabel.setText("Couldn't fetch puzzle")
