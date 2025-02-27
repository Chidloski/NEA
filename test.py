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

            print(players)

            players.reverse()

            for index, i in enumerate(players):
                if i != "":
                    if round > 1:
                        print(f"{i} has index {index}")
                        print(f"{round} thus round - 1 is {round - 1}, and the searched index is {index * 2}")
                        if matchups[round - 1][len(matchups[round - 1]) - index - 1] != ["", ""]:
                            xLineStart = x_spacing * (round - 2) + x_spacing / 4

                            ax.plot([xLineStart, xPosition], [yPosition, yPosition], color='white', linestyle='-', linewidth=1)

                            yJoinLineStart = yPosition - (otherSpacings) / 2
                            yJoinLineEnd = yPosition + (otherSpacings) / 2

                            ax.plot([xLineStart, xLineStart], [yJoinLineStart, yJoinLineEnd], color='white', linestyle='-', linewidth=1)

                    print(len(matchups))
                    print(round < len(matchups))

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

                    print(f"{i} at x:{xPosition}, y:{yPosition}")
                

                y_max = max(y_max, yPosition)

                yPosition += otherSpacings * y_spacing

        print(x_max)
        print(y_max)

        print(len(matchups[1]))
        print(y_spacing * len(matchups[1]))

        # Formatting the plot
        ax.set_xlim(0, x_max)
        ax.set_ylim(0, y_max)
        ax.axis('off')

        self.figure.patch.set_facecolor(background_color)  # Figure background
        ax.set_facecolor(background_color)

        #self.setMinimumSize(int(x_max) * 300, int(y_max) * 10)

        print(len(matchups))

        self.figure.subplots_adjust(left=calculateMargin(len(matchups)), right=0.9, top=0.93, bottom=0.07)  # Avoid excessive padding

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
    A = 0.5318

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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scrollable Tournament Bracket Viewer")
        self.resize(250, 320)

        # Create the scrollable Matplotlib widget
        self.scrollable_matplotlib_widget = ScrollableMatplotlibWidget(self)
        self.scrollable_matplotlib_widget.setGeometry(0, 0, 211, 281)

        # Example data
        tournament_data = {
            #1: [["Player A", "Player B"], ["Player C", "Player D"], ["Player E", "Player F"], ["Player G", "Player H"], ["Player A", "Player B"], ["Player C", "Player D"], ["Player E", "Player F"], ["Player G", "Player H"]],
            1: [["Player A", "Player B"], ["Player C", "Player D"]],# ["Player E", "Player F"]],# ["Player G", "Player H"]],
            2: [["Winner1", "Winner2"]], # ["Winner3", "Player G"]],
            3: [["Finalist1", "Player E"]],
            4: [["Winner"]]
        }

        roundRobin_data = [
            [0, "Player 1", 4, 1, 0, 3, 1],
            [0, "Player 2", 5, 3, 1, 1, 3.5],
            [0, "Player 3", 3, 3, 0, 0, 3],
            [0, "Player 4", 6, 0, 6, 0, 3],
        ]

        tournament_data = padMatches(tournament_data)

        print(tournament_data)

        # Draw the bracket
        self.scrollable_matplotlib_widget.draw_tournament_bracket(tournament_data)
        #self.scrollable_matplotlib_widget.draw_round_robin(roundRobin_data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())