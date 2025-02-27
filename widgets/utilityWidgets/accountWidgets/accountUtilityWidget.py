from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QScrollArea,
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import rcParams
from matplotlib.patches import Rectangle
from playerDB.jsonFunctions import *
from PyQt5.QtGui import QPalette
from datetime import datetime



class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.canvas)

        self.setFixedSize(200, 280)

    def plot_lines(self, x1, y1, x2, y2, xlabel="X Axis", ylabel="Y Axis", title="Two Line Graphs"):
        rcParams['font.family'] = 'Fira Code'

        background_color = get_default_qt_background_color(self)

        x1 = [datetime.strptime(ts, "%Y-%m-%d %H:%M:%S") for ts in x1]
        x2 = [datetime.strptime(ts, "%Y-%m-%d %H:%M:%S") for ts in x2]

        """Plots two line graphs with labels and automatic scaling."""
        self.ax.clear()  # Clear previous plots
        self.ax.plot(x1, y1, label="Match Rating", color="blue", linestyle="-", marker="o")
        self.ax.plot(x2, y2, label="Puzzle Rating", color="red", linestyle="--", marker="x")
        
        # Set labels and title
        self.ax.set_ylabel(ylabel, fontsize=8, color="white")
        self.ax.set_title(title, fontsize=10, color="white", fontweight="bold")

        self.ax.tick_params(axis="y", labelsize=6, colors="white")

        #self.ax.legend(fontsize=6, loc="best", frameon=False)

        for spine in self.ax.spines.values():
            spine.set_color("white")

        self.ax.set_facecolor(background_color)

        # Remove x-axis tick labels
        self.ax.set_xticklabels([])

        # Remove x-axis ticks (small lines along the axis)
        self.ax.set_xticks([])

        self.figure.set_facecolor(background_color)

        self.figure.tight_layout(pad=1.5)
        
        self.figure.subplots_adjust(left=0.28, right=0.95, top=0.88, bottom=0.15)

        self.canvas.draw()



def get_default_qt_background_color(widget):
    palette = widget.palette()
    color = palette.color(QPalette.Background)  # Get the default background color
    return color.name()  # Convert to hex color code



class Ui_accountUtility(QtWidgets.QWidget):

    def setupUi(self, dashboard, baseWindow):
        self.setObjectName("accountUtilityPage")
        self.resize(230, 560)

        self.userId = -1

        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(20)
        font.setBold(True)

        self.matchLabel = QtWidgets.QLabel(self)
        self.matchLabel.setGeometry(QtCore.QRect(10, 10, 201, 21))
        self.matchLabel.setFont(font)
        self.matchLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.matchLabel.setObjectName("matchLabel")

        font.setFamily("Fira Code")
        font.setPointSize(14)

        self.match1Label = QtWidgets.QLabel(self)
        self.match1Label.setGeometry(QtCore.QRect(10, 40, 201, 20))
        self.match1Label.setFont(font)
        self.match1Label.setAlignment(QtCore.Qt.AlignCenter)
        self.match1Label.setObjectName("match1Label")

        self.match2Label = QtWidgets.QLabel(self)
        self.match2Label.setGeometry(QtCore.QRect(10, 65, 201, 20))
        self.match2Label.setFont(font)
        self.match2Label.setAlignment(QtCore.Qt.AlignCenter)
        self.match2Label.setObjectName("match2Label")

        self.match3Label = QtWidgets.QLabel(self)
        self.match3Label.setGeometry(QtCore.QRect(10, 90, 201, 20))
        self.match3Label.setFont(font)
        self.match3Label.setAlignment(QtCore.Qt.AlignCenter)
        self.match3Label.setObjectName("match3Label")

        self.match4Label = QtWidgets.QLabel(self)
        self.match4Label.setGeometry(QtCore.QRect(10, 115, 201, 20))
        self.match4Label.setFont(font)
        self.match4Label.setAlignment(QtCore.Qt.AlignCenter)
        self.match4Label.setObjectName("match4Label")

        self.match5Label = QtWidgets.QLabel(self)
        self.match5Label.setGeometry(QtCore.QRect(10, 140, 201, 20))
        self.match5Label.setFont(font)
        self.match5Label.setAlignment(QtCore.Qt.AlignCenter)
        self.match5Label.setObjectName("match5Label")

        font.setPointSize(20)
        font.setBold(True)

        # Create the scrollable Matplotlib widget
        self.matplotlib_widget = MatplotlibWidget(self)
        self.matplotlib_widget.setGeometry(10, 200, 210, 320)
        self.matplotlib_widget.setObjectName("matplotlibWidget")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)



    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.matchLabel.setText(_translate("accountUtilityPage", "Match Stats:"))
        self.match1Label.setText(_translate("accountUtilityPage", "vs Player, Won!"))
        self.match2Label.setText(_translate("accountUtilityPage", "vs Player, Won!"))
        self.match3Label.setText(_translate("accountUtilityPage", "vs Player, Won!"))
        self.match4Label.setText(_translate("accountUtilityPage", "vs Player, Won!"))
        self.match5Label.setText(_translate("accountUtilityPage", "vs Player, Won!"))



    def resetUi(self):
        self.userId = -1

        self.match1Label.setHidden(True)
        self.match2Label.setHidden(True)
        self.match3Label.setHidden(True)
        self.match4Label.setHidden(True)
        self.match5Label.setHidden(True)



    def fetchStatistics(self, userId):
        matchRatingQuery = {"userId": userId}
        matchRatingRecords = getData("matchProgress", **matchRatingQuery)

        puzzleQuery = {"userId": userId}
        puzzleRatingRecords = getData("puzzleProgress", **puzzleQuery)

        whiteMatchQuery = {"whitePlayer": userId}
        blackMatchQuery = {"blackPlayer": userId}

        whiteMatches = getData("matches", **whiteMatchQuery)
        blackMatches = getData("matches", **blackMatchQuery)

        matches = whiteMatches + blackMatches
        matches = self.cleanse(matches)
        matches = self.insertionSort(matches)
        matches = matches[-5:]

        return matches, matchRatingRecords, puzzleRatingRecords

    
    def cleanse(self, list):
        newList = []

        for i in list:
            if i["winner"] != "Unfinished match":
                newList.append(i)

        return newList


    def insertionSort(self, list):
        for i in range(1, len(list)):
            placed = False
            value = list[i]

            y = i - 1

            while placed == False:
                if y == -1:
                    list[0] = value
                    placed = True

                elif value["id"] > list[y]["id"]:
                    list[y + 1] = value
                    placed = True

                else:
                    list[y + 1] = list[y]
                    y -= 1

        return list
    


    def populate(self, userId):
        matches, matchRatingRecords, puzzleRatingRecords = self.fetchStatistics(userId)

        for index, i in enumerate(matches):
            if i["winner"] == "draw":
                outcome = "Draw"

            elif i["winner"] == userId:
                outcome = "Won!"

            else:
                outcome = "Lost :("

            if i["whitePlayer"] == userId:
                opponentId = i["blackPlayer"]

            else:
                opponentId = i["whitePlayer"]

            print(i)

            if opponentId == "guest":
                versus = "vs Guest, "

            else:
                query = {"id": opponentId}
                opponent = getData("users", **query)
                opponent = opponent[0]
                opponentUsername = opponent["username"]

                versus = f"vs {opponentUsername}, "

            getattr(self, f"match{index + 1}Label").setText(versus + outcome)
            getattr(self, f"match{index + 1}Label").setHidden(False)

        puzzleX = []
        puzzleY = []

        for i in puzzleRatingRecords:
            puzzleX.append(i["datetime"])
            puzzleY.append(i["puzzleRating"])

        matchX = []
        matchY = []

        for i in matchRatingRecords:
            matchX.append(i["datetime"])
            matchY.append(i["matchRating"])

        self.matplotlib_widget.plot_lines(matchX, matchY, puzzleX, puzzleY, "Date / Time", "Rating", "Rating Stats.")



