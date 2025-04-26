from PyQt5 import QtCore, QtGui, QtWidgets
from playerDB.jsonFunctions import *
from widgets.utilityWidgets.functions.puzzleFunctions import getDailyPuzzle, goToDaily, getFenSolution, goToFilterStage2
from widgets.labelClasses import AutoResizingLabel, AutoResizingRadioButton
import requests


class Ui_PuzzleWidget(QtWidgets.QWidget):

    def setupUi(self, dashboard):
        self.setObjectName("puzzleWidget")
        self.resize(230, 560)

        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(18)
        font.setBold(False)

        self.filterPuzzles = []

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

        self.filtersLabel = AutoResizingLabel(18, False, parent = self)
        self.filtersLabel.setGeometry(QtCore.QRect(10, 70, 201, 21))
        self.filtersLabel.setFont(font)
        self.filtersLabel.setObjectName("filtersLabel")

        font.setPointSize(13)

        self.openingRadioButton = AutoResizingRadioButton(13, False, parent = self)
        self.openingRadioButton.setGeometry(QtCore.QRect(20, 110, 99, 20))
        self.openingRadioButton.setFont(font)
        self.openingRadioButton.setObjectName("openingRadioButton")
        self.openingRadioButton.clicked.connect(lambda: self.toggleRadio(self.positionRadioGroup, self.midgameRadioButton, self.endgameRadioButton))
        self.openingRadioButton.theme = "opening" 
        self.openingRadioButton.status = "unclicked"

        self.midgameRadioButton = AutoResizingRadioButton(13, False, parent = self)
        self.midgameRadioButton.setGeometry(QtCore.QRect(20, 130, 99, 20))
        self.midgameRadioButton.setFont(font)
        self.midgameRadioButton.setObjectName("midgameRadioButton")
        self.midgameRadioButton.clicked.connect(lambda: self.toggleRadio(self.positionRadioGroup, self.openingRadioButton, self.endgameRadioButton))
        self.midgameRadioButton.theme = "middlegame"
        self.midgameRadioButton.status = "unclicked"

        self.endgameRadioButton = AutoResizingRadioButton(13, False, parent = self)
        self.endgameRadioButton.setGeometry(QtCore.QRect(20, 150, 99, 20))
        self.endgameRadioButton.setFont(font)
        self.endgameRadioButton.setObjectName("endgameRadioButton")
        self.endgameRadioButton.clicked.connect(lambda: self.toggleRadio(self.positionRadioGroup, self.openingRadioButton, self.midgameRadioButton))
        self.endgameRadioButton.theme = "endgame"
        self.endgameRadioButton.status = "unclicked"

        self.positionRadioGroup = QtWidgets.QButtonGroup(self)
        self.positionRadioGroup.addButton(self.openingRadioButton)
        self.positionRadioGroup.addButton(self.midgameRadioButton)
        self.positionRadioGroup.addButton(self.endgameRadioButton)

        self.forkRadioButton = AutoResizingRadioButton(13, False, parent = self)
        self.forkRadioButton.setGeometry(QtCore.QRect(120, 110, 91, 20))
        self.forkRadioButton.setFont(font)
        self.forkRadioButton.setObjectName("forkRadioButton")
        self.forkRadioButton.clicked.connect(lambda: self.toggleRadio(self.motifRadioGroup, self.pinRadioButton, self.discoveredRadioButton))
        self.forkRadioButton.theme = "fork"
        self.forkRadioButton.status = "unclicked"


        self.pinRadioButton = AutoResizingRadioButton(13, False, parent = self)
        self.pinRadioButton.setGeometry(QtCore.QRect(120, 130, 91, 20))
        self.pinRadioButton.setFont(font)
        self.pinRadioButton.setObjectName("pinRadio")
        self.pinRadioButton.clicked.connect(lambda: self.toggleRadio(self.motifRadioGroup, self.forkRadioButton, self.discoveredRadioButton))
        self.pinRadioButton.theme = "skewer"
        self.pinRadioButton.status = "unclicked"

        self.discoveredRadioButton = AutoResizingRadioButton(13, False, parent = self)
        self.discoveredRadioButton.setGeometry(QtCore.QRect(120, 150, 91, 20))
        self.discoveredRadioButton.setFont(font)
        self.discoveredRadioButton.setObjectName("discoveredRadio")
        self.discoveredRadioButton.clicked.connect(lambda: self.toggleRadio(self.motifRadioGroup, self.pinRadioButton, self.forkRadioButton))
        self.discoveredRadioButton.theme = "discoveredAttack"
        self.discoveredRadioButton.status = "unclicked"

        self.motifRadioGroup = QtWidgets.QButtonGroup(self)
        self.motifRadioGroup.addButton(self.forkRadioButton)
        self.motifRadioGroup.addButton(self.pinRadioButton)
        self.motifRadioGroup.addButton(self.discoveredRadioButton)

        self.positionLabel = AutoResizingLabel(13, False, parent = self)
        self.positionLabel.setGeometry(QtCore.QRect(20, 90, 71, 21))
        self.positionLabel.setFont(font)
        self.positionLabel.setObjectName("positionLabel")

        self.motifLabel = AutoResizingLabel(13, False, parent = self)
        self.motifLabel.setGeometry(QtCore.QRect(120, 90, 71, 21))
        self.motifLabel.setFont(font)
        self.motifLabel.setObjectName("motifLabel")

        self.taskLabel = AutoResizingLabel(13, False, parent = self)
        self.taskLabel.setGeometry(QtCore.QRect(20, 180, 71, 21))
        self.taskLabel.setFont(font)
        self.taskLabel.setObjectName("taskLabel")

        self.winRadioButton = AutoResizingRadioButton(13, False, parent = self)
        self.winRadioButton.setGeometry(QtCore.QRect(20, 200, 99, 20))
        self.winRadioButton.setFont(font)
        self.winRadioButton.setObjectName("winRadioButton")
        self.winRadioButton.clicked.connect(lambda: self.toggleRadio(self.playstyleRadioGroup, self.defendRadioButton))
        self.winRadioButton.theme = "mate"
        self.winRadioButton.status = "unclicked"

        self.defendRadioButton = AutoResizingRadioButton(13, False, parent = self)
        self.defendRadioButton.setGeometry(QtCore.QRect(20, 220, 99, 20))
        self.defendRadioButton.setFont(font)
        self.defendRadioButton.setObjectName("defendRadioButton")
        self.defendRadioButton.clicked.connect(lambda: self.toggleRadio(self.playstyleRadioGroup, self.winRadioButton))
        self.defendRadioButton.theme = "defensiveMove"
        self.defendRadioButton.status = "unclicked"

        self.playstyleRadioGroup = QtWidgets.QButtonGroup(self)
        self.playstyleRadioGroup.addButton(self.winRadioButton)
        self.playstyleRadioGroup.addButton(self.defendRadioButton)

        self.specialLabel = AutoResizingLabel(13, False, parent = self)
        self.specialLabel.setGeometry(QtCore.QRect(120, 180, 71, 21))
        self.specialLabel.setFont(font)
        self.specialLabel.setObjectName("specialLabel")

        self.sacrificeRadioButton = AutoResizingRadioButton(13, False, parent = self)
        self.sacrificeRadioButton.setGeometry(QtCore.QRect(120, 200, 99, 20))
        self.sacrificeRadioButton.setFont(font)
        self.sacrificeRadioButton.setObjectName("sacrificeRadioButton")
        self.sacrificeRadioButton.clicked.connect(lambda: self.toggleRadio(self.specialRadioGroup, self.zugzwangRadioButton))
        self.sacrificeRadioButton.theme = "sacrifice"
        self.sacrificeRadioButton.status = "unclicked"

        self.zugzwangRadioButton = AutoResizingRadioButton(13, False, parent = self)
        self.zugzwangRadioButton.setGeometry(QtCore.QRect(120, 220, 99, 20))
        self.zugzwangRadioButton.setFont(font)
        self.zugzwangRadioButton.setObjectName("zugzwangRadioButton")
        self.zugzwangRadioButton.clicked.connect(lambda: self.toggleRadio(self.specialRadioGroup, self.sacrificeRadioButton))
        self.zugzwangRadioButton.theme = "zugzwang"
        self.zugzwangRadioButton.status = "unclicked"

        self.specialRadioGroup = QtWidgets.QButtonGroup(self)
        self.specialRadioGroup.addButton(self.sacrificeRadioButton)
        self.specialRadioGroup.addButton(self.zugzwangRadioButton)

        self.ratingSlider = QtWidgets.QSlider(self)
        self.ratingSlider.setGeometry(QtCore.QRect(20, 265, 181, 25))
        self.ratingSlider.setFont(font)
        self.ratingSlider.setMinimum(400)
        self.ratingSlider.setMaximum(2800)
        self.ratingSlider.setSliderPosition(800)
        self.ratingSlider.setOrientation(QtCore.Qt.Horizontal)
        self.ratingSlider.setInvertedAppearance(False)
        self.ratingSlider.setTickInterval(0)
        self.ratingSlider.setObjectName("ratingSlider")
        self.ratingSlider.valueChanged.connect(self.updateRatingLabel)

        self.ratingLabel = AutoResizingLabel(13, False, parent = self)
        self.ratingLabel.setGeometry(QtCore.QRect(70, 245, 91, 21))
        self.ratingLabel.setFont(font)
        self.ratingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ratingLabel.setObjectName("ratingLabel")

        self.numOfPuzzleSlider = QtWidgets.QSlider(self)
        self.numOfPuzzleSlider.setGeometry(QtCore.QRect(20, 315, 181, 25))
        self.numOfPuzzleSlider.setFont(font)
        self.numOfPuzzleSlider.setMinimum(1)
        self.numOfPuzzleSlider.setMaximum(5)
        self.numOfPuzzleSlider.setProperty("value", 3)
        self.numOfPuzzleSlider.setSliderPosition(3)
        self.numOfPuzzleSlider.setOrientation(QtCore.Qt.Horizontal)
        self.numOfPuzzleSlider.setInvertedAppearance(False)
        self.numOfPuzzleSlider.setTickInterval(0)
        self.numOfPuzzleSlider.setObjectName("numOfPuzzlesSlider")
        self.numOfPuzzleSlider.valueChanged.connect(self.updateNumOfPuzzlesLabel)

        self.numOfPuzzlesLabel = AutoResizingLabel(13, False, parent = self)
        self.numOfPuzzlesLabel.setGeometry(QtCore.QRect(40, 295, 151, 21))
        self.numOfPuzzlesLabel.setFont(font)
        self.numOfPuzzlesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.numOfPuzzlesLabel.setObjectName("numOfPuzzlesLabel")

        self.errorLabel = AutoResizingLabel(13, False, parent = self)
        self.errorLabel.setGeometry(QtCore.QRect(10, 330, 201, 31))
        self.errorLabel.setFont(font)
        self.errorLabel.setStyleSheet("color: rgb(175, 61, 50)")
        self.errorLabel.setText("")
        self.errorLabel.setWordWrap(True)
        self.errorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.errorLabel.setObjectName("errorLabel")
        self.errorLabel.setHidden(True)

        font.setPointSize(18)
        font.setBold(True)

        self.getPuzzlesButton = QtWidgets.QPushButton(self)
        self.getPuzzlesButton.setGeometry(QtCore.QRect(20, 370, 181, 41))
        self.getPuzzlesButton.setFont(font)
        self.getPuzzlesButton.setObjectName("getPuzzlesButton")
        self.getPuzzlesButton.clicked.connect(lambda: goToFilterStage2(dashboard, self))

        font.setBold(False)

        self.dailyPuzzleLabel = AutoResizingLabel(18, False, parent = self)
        self.dailyPuzzleLabel.setGeometry(QtCore.QRect(10, 430, 201, 21))
        self.dailyPuzzleLabel.setFont(font)
        self.dailyPuzzleLabel.setObjectName("dailyPuzzleLabel")

        font.setPointSize(13)

        self.matchupLabel = AutoResizingLabel(13, False, parent = self)
        self.matchupLabel.setGeometry(QtCore.QRect(20, 450, 191, 21))
        self.matchupLabel.setFont(font)
        self.matchupLabel.setObjectName("matchupLabel")

        self.dailyRatingLabel = AutoResizingLabel(13, False, parent = self)
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


    def updateRatingLabel(self, value):
        self.ratingLabel.setText(f"Rating: {value}")

    
    def updateNumOfPuzzlesLabel(self, value):
        self.numOfPuzzlesLabel.setText(f"Number of Puzzles: {value}")


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.currentUserLabel.setText(_translate("puzzleWidget", "Current User:"))
        self.currentUserPuzzleRatingLabel.setText(_translate("puzzleWidget", "Puzzle Rating:"))
        self.filtersLabel.setText(_translate("puzzleWidget", "Filters:"))
        self.openingRadioButton.setText(_translate("puzzleWidget", "opening"))
        self.midgameRadioButton.setText(_translate("puzzleWidget", "midgame"))
        self.endgameRadioButton.setText(_translate("puzzleWidget", "endgame"))
        self.forkRadioButton.setText(_translate("puzzleWidget", "fork"))
        self.pinRadioButton.setText(_translate("puzzleWidget", "pin"))
        self.positionLabel.setText(_translate("puzzleWidget", "Position:"))
        self.motifLabel.setText(_translate("puzzleWidget", "Motif:"))
        self.discoveredRadioButton.setText(_translate("puzzleWidget", "discovered"))
        self.taskLabel.setText(_translate("puzzleWidget", "Task:"))
        self.winRadioButton.setText(_translate("puzzleWidget", "win"))
        self.defendRadioButton.setText(_translate("puzzleWidget", "defend"))
        self.specialLabel.setText(_translate("puzzleWidget", "Special:"))
        self.sacrificeRadioButton.setText(_translate("puzzleWidget", "sacrifice"))
        self.zugzwangRadioButton.setText(_translate("puzzleWidget", "zugzwang"))
        self.ratingLabel.setText(_translate("puzzleWidget", "Rating: 800"))
        self.numOfPuzzlesLabel.setText(_translate("puzzleWidget", "Number of Puzzles: 3"))
        self.getPuzzlesButton.setText(_translate("puzzleWidget", "Get Puzzles"))
        self.dailyPuzzleLabel.setText(_translate("puzzleWidget", "Daily Puzzle:"))
        self.matchupLabel.setText(_translate("puzzleWidget", "Niemman Vs Carlsen"))
        self.dailyRatingLabel.setText(_translate("puzzleWidget", "Rating:"))
        self.dailyPuzzleButton.setText(_translate("puzzleWidget", "Daily Puzzle"))


    def resetUi(self, userId):
        self.motifRadioGroup.setExclusive(False)
        self.specialRadioGroup.setExclusive(False)
        self.positionRadioGroup.setExclusive(False)
        self.playstyleRadioGroup.setExclusive(False)

        self.pinRadioButton.setChecked(False)
        self.forkRadioButton.setChecked(False)
        self.discoveredRadioButton.setChecked(False)
        self.openingRadioButton.setChecked(False)
        self.midgameRadioButton.setChecked(False)
        self.endgameRadioButton.setChecked(False)
        self.winRadioButton.setChecked(False)
        self.defendRadioButton.setChecked(False)
        self.sacrificeRadioButton.setChecked(False)
        self.zugzwangRadioButton.setChecked(False)

        self.motifRadioGroup.setExclusive(True)
        self.specialRadioGroup.setExclusive(True)
        self.positionRadioGroup.setExclusive(True)
        self.playstyleRadioGroup.setExclusive(True)

        self.numOfPuzzlesLabel.setText("Number of Puzzles: 3")
        self.numOfPuzzleSlider.setValue(3)

        self.populate(userId)


    # get daily puzzle and set rating slider to the correct rating
    def populate(self, userId):
        user = getData("users", id = userId)
        queryStatus, *_, matchup,  puzzleRating = getDailyPuzzle()

        self.currentUserLabel.setText(user[0]["username"] + ":")
        self.currentUserPuzzleRatingLabel.setText(f"Puzzle Rating : {user[0]['puzzleRating']}")

        self.ratingSlider.setValue(int(user[0]['puzzleRating']))
        self.ratingLabel.setText(f"Rating: {user[0]['puzzleRating']}")

        if queryStatus == 200:
            self.matchupLabel.setText(matchup)
            self.dailyRatingLabel.setText(f"Rating: {puzzleRating}")

        else:
            self.dailyRatingLabel.setText("Couldn't fetch puzzle")


    # set up behaviour for toggles
    def toggleRadio(self, radioGroup, *args):
        sender = self.sender()

        for btn in args:
            if btn != sender and btn.status == "clicked":
                btn.status = "unclicked"

        if sender.status == "clicked":
            radioGroup.setExclusive(False)
            sender.setChecked(False)
            radioGroup.setExclusive(True)

            sender.status = "unclicked"

        else:
           sender.status = "clicked"


    # fetch filter puzzles
    def getParameters(self, dashboard):
        groups = [self.motifRadioGroup, self.specialRadioGroup, self.positionRadioGroup, self.playstyleRadioGroup]
        themes = []

        # get filters if any button is selected
        for i in groups:
            if i.checkedButton():
                themes.append(i.checkedButton().theme)

        rating = self.ratingSlider.value()
        numberOfPuzzles = self.numOfPuzzleSlider.value()

        parameters = {
            "rating": str(rating),
            "themesType": "ALL",
            "count": str(numberOfPuzzles)
        }

        # themes list must be in json format
        if themes:
            parameters["themes"] = json.dumps(themes)

        heads = {
            "x-rapidapi-key": "fe146e7cbamshaa42abfb08774abp142fdajsnfd4934fbdbfd",
            "x-rapidapi-host": "chess-puzzles.p.rapidapi.com"
        }

        print(heads)

        url = "https://chess-puzzles.p.rapidapi.com/"

        response = requests.get(url, headers=heads, params=parameters)
        statCode = response.status_code

        # if the puzzles are fetched
        if statCode == 200:
            result = response.json()
            fetchedPuzzles = result["puzzles"]

            puzzles = []

            for i in fetchedPuzzles:
                solution = getFenSolution(dashboard, i["fen"], i["moves"])
                robotMove = solution.pop(0)

                record = {
                    "fen": i["fen"],
                    "rating": i["rating"],
                    "robotMove": robotMove,
                    "solution": solution,
                    "outcome": "unfinished"
                }

                puzzles.append(record)

            print(fetchedPuzzles)
            print(puzzles)

            return puzzles

        # show error
        else: 
            self.errorLabel.setText("No Matching Puzzles found")
            self.errorLabel.setHidden(False)

            print(statCode)

            return 400