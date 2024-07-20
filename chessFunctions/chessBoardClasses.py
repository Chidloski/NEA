from PyQt5.QtCore import pyqtSignal, QTimer, Qt
from PyQt5.QtWidgets import QLabel, QApplication
from PyQt5.QtGui import QPixmap

# <---- creating sub-classes for the tiles ---->


# square acts as a parent class for both lightsquare and darksquare
# square handles all mouse press functionallity and setup
# -> light and darksquare only used to allow stylesheets to be applied separately
class square(QLabel):

    # adds click functionality to QLabel
    clicked = pyqtSignal(str)

    # initialises the QLabel parent
    def __init__(self, *args, **kwargs):
        QLabel.__init__(self, *args, **kwargs)

    # sets up each tile differently
    def setupLabel(self, font, objName, starter):
        self.setFont(font)
        self.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.setIndent(2)
        self.setObjectName(objName)
        self.occupied = starter

        # variable will hold a move counter for the move at which en passant becomes possible
        # only possible the move after
        self.enPassantActive = -2


    # re-declares the mouse press event functions as QLabel does not have them built-in
    # variable clickState is used to show to current state of click (single, or double)

    def mousePressEvent(self, event):
        # after each mouse press event, clickstate changes to clicked
        self.clickState = "Clicked"

    def mouseReleaseEvent(self, event):
            self.clicked.emit(self.clickState)


class lightSquare(square):
    # child class of square

    type = "light"


class darkSquare(square):
    # child class of square

    type = "dark"


# <---- now defining class for all pieces ---->

class piece(QLabel):
    # creates a sub-class for all pieces
    # assigns the right image, and moveset

    # adds click functionality to the label
    clicked = pyqtSignal(str)

    # initialises the QLabel
    def __init__(self, *args, **kwargs):
        QLabel.__init__(self, *args, **kwargs)

    # adds all necessary values to the object
    def setupLabel(self, colour, objName, piece, position):

        self.setText("")
        self.setPixmap(QPixmap("Resources/ChessIcons/" + colour + piece + ".png"))
        self.setScaledContents(True)
        self.setObjectName(objName)
        self.setHidden(False)

        self.colour = colour
        self.moveset = piece
        self.name = objName
        self.pos = position

        # keeps a tab of if a pawn has moved to check whether it can move two squares forward
        if piece in ("Pawn", "Rook", "King"):
            self.hasMoved = False

    # re-declares the mouse press event functions as QLabel does not have them built-in
    # variable clickState is used to show to current state of click (single, or double)

    def mousePressEvent(self, event):
        # after each mouse press event, clickstate changes to clicked
        self.clickState = "Clicked"

    def mouseReleaseEvent(self, event):
            self.clicked.emit(self.clickState)


    
        



