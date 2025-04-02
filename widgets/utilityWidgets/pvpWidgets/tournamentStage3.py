from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QScrollArea,
)
from PyQt5.QtGui import QPalette
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import rcParams
from matplotlib.patches import Rectangle
import math
from playerDB.jsonFunctions import *
from widgets.utilityWidgets.functions.tournamentFunctions import goToStage1FromTournaments, goToTournamentStage4, finaliseTournament
from widgets.labelClasses import AutoResizingLabel


class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.canvas)

    def draw_tournament_bracket(self, matchups):
        rcParams['font.family'] = 'Fira Code'

        background_color = get_default_qt_background_color(self)
        
        self.figure.clear()  # Clear the figure
        ax = self.figure.add_subplot(111)

        y_spacing = 2
        x_spacing = 1

        y_max = 0
        x_max = 0

        for round, matches in matchups.items():
            xPosition = x_spacing * (round - 1)
            yPosition = 0

            x_max = xPosition

            firstSpacing = (2**(round - 1) - 1)
            otherSpacings = 2**(round)

            players = []

            for match in matches:
                for player in match:
                    players.append(player)

            yPosition += firstSpacing * y_spacing

            #print(players)

            players.reverse()

            print(f"round: {round}, with players: {players}")

            for index, i in enumerate(players):
                if i != "":
                    if round > 1:
                        #print(f"{i} has index {index}")
                        #print(f"{round} thus round - 1 is {round - 1}, and the searched index is {index * 2}")
                        if matchups[round - 1][len(matchups[round - 1]) - index - 1] != ["", ""]:
                            xLineStart = x_spacing * (round - 2) + x_spacing / 4

                            ax.plot([xLineStart, xPosition], [yPosition, yPosition], color='white', linestyle='-', linewidth=1)

                            yJoinLineStart = yPosition - (otherSpacings) / 2
                            yJoinLineEnd = yPosition + (otherSpacings) / 2

                            ax.plot([xLineStart, xLineStart], [yJoinLineStart, yJoinLineEnd], color='white', linestyle='-', linewidth=1)

                    #print(len(matchups))
                    #print(round < len(matchups))

                    if round < len(matchups):
                        xLineStart = x_spacing * (round - 2) + x_spacing

                        ax.plot([xLineStart, xLineStart + x_spacing / 4], [yPosition, yPosition], color='white', linestyle='-', linewidth=1)
    
                    text = ax.text(xPosition, yPosition, i, ha='right', va='center', fontsize=10, color='white') #, bbox=dict(facecolor=background_color, edgecolor='none'))

                    renderer = self.canvas.get_renderer()
                    bbox = text.get_window_extent(renderer).transformed(ax.transData.inverted())

                    bboxWidth = bbox.x1 - bbox.x0

                    # Draw a rectangle using the bounding box of the text
                    padding = bboxWidth  # Add padding around the text
                    rect = Rectangle(
                        (bbox.x0 - padding * 3.5, bbox.y0 - padding),
                        bbox.width + 3.5 * padding,
                        bbox.height + 3.5 * padding,
                        color=background_color,
                        zorder=text.get_zorder() - 1,  # Draw behind the text
                    )
                    ax.add_patch(rect)

                    #print(f"{i} at x:{xPosition}, y:{yPosition}")
                

                y_max = max(y_max, yPosition)

                yPosition += otherSpacings * y_spacing

        #print(x_max)
        #print(y_max)

        #print(len(matchups[1]))
        #print(y_spacing * len(matchups[1]))

        # Formatting the plot
        ax.set_xlim(0, x_max)
        ax.set_ylim(0, y_max)
        ax.axis('off')

        self.figure.subplots_adjust(left=calculateMargin(len(matchups)), right=0.9, top=0.93, bottom=0.07)  # Avoid excessive padding

        self.figure.patch.set_facecolor(background_color)  # Figure background
        ax.set_facecolor(background_color)

        # Adjust the resolution to make the grid visually compressed
        self.canvas.setFixedSize(int(x_max * 150), int(y_max * 12)) 

        self.canvas.draw()

    def draw_round_robin(self, playerStats):
        # passes in a 2d list, list for each player containing id, username, games played, games won, games drawn, games lost, and points
        rcParams['font.family'] = 'Fira Code'

        background_color = get_default_qt_background_color(self)

        playerStats = insertionSort(playerStats)
        
        self.figure.clear()  # Clear the figure
        ax = self.figure.add_subplot(111)

        y_spacing = 2.5

        yPosition = 0

        index = len(playerStats) - 1

        for i in playerStats:
            ax.text(0, yPosition, f"{index + 1}.", ha='left', va='center', fontsize=10, color='white')
            ax.text(0.15, yPosition, i[1], ha='left', va='center', fontsize=10, color='white')
            ax.text(1, yPosition, i[2], ha='center', va='center', fontsize=10, color='white')
            ax.text(1.25, yPosition, i[3], ha='center', va='center', fontsize=10, color='white')
            ax.text(1.5, yPosition, i[4], ha='center', va='center', fontsize=10, color='white')
            ax.text(1.75, yPosition, i[5], ha='center', va='center', fontsize=10, color='white')
            ax.text(2.05, yPosition, i[6], ha='center', va='center', fontsize=10, color='white')

            index -= 1
            yPosition += y_spacing

        ax.text(0, yPosition, "Player", ha='left', va='center', fontsize=10, fontweight='bold', color='white')
        ax.text(1, yPosition, "GP", ha='center', va='center', fontsize=10, fontweight='bold', color='white')
        ax.text(1.25, yPosition, "W", ha='center', va='center', fontsize=10, fontweight='bold', color='white')
        ax.text(1.5, yPosition, "D", ha='center', va='center', fontsize=10, fontweight='bold', color='white')
        ax.text(1.75, yPosition, "L", ha='center', va='center', fontsize=10, fontweight='bold', color='white')
        ax.text(2.05, yPosition, "Pts", ha='center', va='center', fontsize=10, fontweight='bold', color='white')

        y_max = yPosition
        x_max = 2.05

        # Formatting the plot
        ax.set_xlim(0, x_max)
        ax.set_ylim(0, y_max)
        ax.axis('off')

        self.figure.patch.set_facecolor(background_color)  # Figure background
        ax.set_facecolor(background_color)

        self.figure.subplots_adjust(left=0, right=0.9, top=0.93, bottom=0.07)  # Avoid excessive padding

        # Adjust the resolution to make the grid visually compressed
        self.canvas.setFixedSize(int(x_max * 150), int(y_max * 12)) 

        self.canvas.draw()


# relationship between number of rounds and margin subplot follows an inverse exponential with the following values
# solving for A allows us to find all margins from one equation wherein a is the constant that scales up the scale factor
def calculateMargin(rounds):
    B = 0.7385
    #A = 0.5318
    A = 0.65

    return round(A * (B**rounds), 2)

def get_default_qt_background_color(widget):
    palette = widget.palette()
    color = palette.color(QPalette.Background)  # Get the default background color
    return color.name()  # Convert to hex color code

def padMatches(bracket):
    # takes in a dictionary of matchups and pads all null matches

    print(len(bracket))

    size = 2**(len(bracket) - 2)

    for round, matches in bracket.items():
        
        for i in range(len(matches), size):
            matches.append(["", ""])

        size = size // 2

    return bracket


def insertionSort(list):
    for i in range(1, len(list)):
        placed = False
        value = list[i]

        y = i - 1

        while placed == False:
            if y == -1:
                list[0] = value
                placed = True

            elif value[6] > list[y][6]:
                list[y + 1] = value
                placed = True

            elif value[6] == list[y][6] and value[2] < list[y][2]:
                list[y + 1] = value
                placed = True

            elif value[6] == list[y][6] and value[2] == list[y][2] and value[3] > list[y][3]:
                list[y + 1] = value
                placed = True

            else:
                list[y + 1] = list[y]
                y -= 1

    return list


class ScrollableMatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Create the Matplotlib widget
        self.matplotlib_widget = MatplotlibWidget()

        # Embed it inside a QScrollArea
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidget(self.matplotlib_widget)
        self.scroll_area.setWidgetResizable(True)

        # Set fixed size for the scrollable area
        self.scroll_area.setFixedSize(201, 271)

        # Layout for the scrollable widget
        layout = QVBoxLayout(self)
        layout.addWidget(self.scroll_area)

    def draw_tournament_bracket(self, matchups):
        self.matplotlib_widget.draw_tournament_bracket(matchups)

    def draw_round_robin(self, playerStats):
        self.matplotlib_widget.draw_round_robin(playerStats)


class Ui_TournamentStage3(QtWidgets.QWidget):

    def setupUi(self, dashboard, baseWindow):
        self.setObjectName("tournamentStage3Page")
        self.resize(230, 560)
        self.setAutoFillBackground(False)

        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(24)
        font.setBold(True)

        self.tournamentType = ""
        self.userDetails = []
        self.knockoutDetails = {}
        self.roundRobinDetails = []
        self.roundRobinMatches = []
        self.matchIndex = 0
        self.currentMatch = []
        self.tournamentId = -1

        self.typeLabel = AutoResizingLabel(24, True, parent = self)
        self.typeLabel.setGeometry(QtCore.QRect(10, 10, 201, 31))
        self.typeLabel.setFont(font)
        self.typeLabel.setObjectName("typeLabel")

        # Create the scrollable Matplotlib widget
        self.scrollable_matplotlib_widget = ScrollableMatplotlibWidget(self)
        self.scrollable_matplotlib_widget.setGeometry(0, 30, 211, 281)
        self.scrollable_matplotlib_widget.setObjectName("matplotlibWidget")

        self.nextMatchLabel = AutoResizingLabel(24, True, parent = self)
        self.nextMatchLabel.setGeometry(QtCore.QRect(10, 320, 201, 31))
        self.nextMatchLabel.setFont(font)
        self.nextMatchLabel.setObjectName("nextMatchLabel")

        font.setPointSize(18)

        self.quitButton = QtWidgets.QPushButton(self)
        self.quitButton.setGeometry(QtCore.QRect(10, 511, 201, 41))
        self.quitButton.setFont(font)
        self.quitButton.setObjectName("quitButton")
        self.quitButton.clicked.connect(lambda: goToStage1FromTournaments(dashboard))

        self.nextMatchButton = QtWidgets.QPushButton(self)
        self.nextMatchButton.setGeometry(QtCore.QRect(10, 470, 201, 41))
        self.nextMatchButton.setFont(font)
        self.nextMatchButton.setObjectName("nextMatchButton")
        self.nextMatchButton.clicked.connect(lambda: goToTournamentStage4(dashboard, self.currentMatch, self.userDetails))

        self.player1Label = AutoResizingLabel(18, True, parent = self)
        self.player1Label.setGeometry(QtCore.QRect(10, 350, 141, 31))
        self.player1Label.setFont(font)
        self.player1Label.setObjectName("player1Label")

        self.versusLabel = AutoResizingLabel(18, True, parent = self)
        self.versusLabel.setGeometry(QtCore.QRect(25, 390, 161, 61))
        self.versusLabel.setFont(font)
        self.versusLabel.setAlignment(QtCore.Qt.AlignCenter|QtCore.Qt.AlignTop)
        self.versusLabel.setObjectName("versusLabel")

        self.player2Label = AutoResizingLabel(18, True, parent = self)
        self.player2Label.setGeometry(QtCore.QRect(70, 430, 141, 31))
        self.player2Label.setFont(font)
        self.player2Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.player2Label.setObjectName("player2Label")
        
        font.setPointSize(14)

        self.player1RatingLabel = AutoResizingLabel(14, True, parent = self)
        self.player1RatingLabel.setGeometry(QtCore.QRect(10, 380, 58, 16))
        self.player1RatingLabel.setFont(font)
        self.player1RatingLabel.setObjectName("player1Ratinglabel")
        
        self.player2RatingLabel = AutoResizingLabel(14, True, parent = self)
        self.player2RatingLabel.setGeometry(QtCore.QRect(150, 420, 58, 16))
        self.player2RatingLabel.setFont(font)
        self.player2RatingLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.player2RatingLabel.setObjectName("player2RatingLabel")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    
    def populateNextMatch(self, match, userDetails):

        print(f"Match: {match}")
        print(f"Users: {userDetails}")

        if match != -1:
            player1 = match[0]
            player2 = match[1]

            for i in userDetails:
                if i[1] == player1:
                    player1Rating = i[2]

            for i in userDetails:
                if i[1] == player2:
                    player2Rating = i[2]

            self.player1Label.setText(player1)
            self.player1RatingLabel.setText(str(player1Rating))

            self.player2Label.setText(player2)
            self.player2RatingLabel.setText(str(player2Rating))

        else:
            self.nextMatchButton.setHidden(True)
            self.player1Label.setHidden(True)
            self.player1RatingLabel.setHidden(True)
            self.player2Label.setHidden(True)
            self.player2RatingLabel.setHidden(True)

            self.nextMatchLabel.setText("Winner:")

            if self.tournamentType == "Knockout":
                winner = self.knockoutDetails[len(self.knockoutDetails)][0][0]

            else:
                winner = self.roundRobinDetails[0]

                for i in self.roundRobinDetails:
                    if i[6] > winner[6]:
                        winner = i

                winner = i[1]

            self.versusLabel.setText(winner)

            query = {"username": winner}

            user = getData("users", **query)

            winnerId = "unfinished"

            if len(user) == 0:
                winnerId = "guest"

            elif len(user) == 1:
                winnerId = user[0]["id"]

            finaliseTournament(self.tournamentId, winnerId)

            #FINALISE TOURNAMENT RECORD


    def resetUi(self):
        self.tournamentType = ""
        self.userDetails = []
        self.knockoutDetails = {}
        self.roundRobinDetails = []
        self.roundRobinMatches = []
        self.matchIndex = 0
        self.currentMatch = []
        self.tournamentId = -1

        self.typeLabel.setText("")
        self.player1Label.setText("")
        self.player1RatingLabel.setText("")
        self.player2Label.setText("")
        self.player2RatingLabel.setText("")

        self.nextMatchButton.setHidden(False)
        self.player1Label.setHidden(False)
        self.player1RatingLabel.setHidden(False)
        self.player1Label.setHidden(False)
        self.player1RatingLabel.setHidden(False)

        self.nextMatchButton.setText("Next Match:")
        self.versusLabel.setText("Vs.")


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.typeLabel.setText(_translate("tournamentStage3Page", "Tournament"))
        self.nextMatchLabel.setText(_translate("tournamentStage3Page", "Next Match:"))
        self.quitButton.setText(_translate("tournamentStage3Page", "Quit Tournament"))
        self.nextMatchButton.setText(_translate("tournamentStage3Page", "Next Match"))
        self.player1Label.setText(_translate("tournamentStage3Page", "Player 1"))
        self.versusLabel.setText(_translate("tournamentStage3Page", "Vs."))
        self.player2Label.setText(_translate("tournamentStage3Page", "Player 2"))
        self.player1RatingLabel.setText(_translate("tournamentStage3Page", "800"))
        self.player2RatingLabel.setText(_translate("tournamentStage3Page", "800"))

