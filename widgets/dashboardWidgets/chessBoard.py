from PyQt5 import QtCore, QtGui, QtWidgets
from chessFunctions.chessBoardClasses import *
from chessFunctions.move import *
from chessFunctions.movementFunctions import promotingTo


class Ui_chessBoard(QtWidgets.QWidget):

    # the current move list contains all information necessary for the move function
    # - position 0 contains whether a move is active
    # - position 1 contains the address of the piece to move
    # - position 2 contains the valid tiles to move
    # - position 3 contains the move number
    # - position 4 contains the attacking pieces
    # - position 5 contains pieces that are highlighted from the previous move (e.g last move)
    # - position 6 contains the pgn moveset of the game
    currentMove = [False, -1, [], 0, [], [], ""]

    moveActive = False
    pieceBeingMoved = -1
    validTiles = []
    moveNumber = 0
    attackers = []
    previousMove = []
    pgn = ""

    def moveFunction(self, currentPiece):
            # print(self.currentMove)
            #self.currentMove = move(self, currentPiece, self.currentMove[0], self.currentMove[1], 
            #                        self.currentMove[2], self.currentMove[3], self.currentMove[4], 
            #                        self.currentMove[5], self.currentMove[6])
            
            (self.moveActive, self.pieceBeingMoved, self.validTiles, 
            self.moveNumber, self.attackers, self.previousMove, self.pgn) = move(self, currentPiece, self.moveActive, self.pieceBeingMoved, 
                                                                                self.validTiles, self.moveNumber, self.attackers, 
                                                                                self.previousMove, self.pgn)

    def setupUi(self):
        self.setObjectName("chessBoard")
        self.resize(560, 560)

        # font is declared once as it doesn't change
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(14)
        font.setBold(True)

        # the next 300 lines contain repeated code for each tile 
        # tiles with added words for coords also have alignment declared and font declared
        self.a8 = lightSquare(self)
        self.a8.setGeometry(QtCore.QRect(0, 0, 70, 70))
        self.a8.setupLabel(font, "a8", "blackARook")
        self.a8.clicked.connect(lambda: self.moveFunction(self.a8))

        self.b8 = darkSquare(self)
        self.b8.setGeometry(QtCore.QRect(70, 0, 70, 70))
        self.b8.setupLabel(font, "b8", "blackBKnight")
        self.b8.clicked.connect(lambda: self.moveFunction(self.b8))

        self.c8 = lightSquare(self)
        self.c8.setGeometry(QtCore.QRect(140, 0, 70, 70))
        self.c8.setupLabel(font, "c8", "blackCBishop")
        self.c8.clicked.connect(lambda: self.moveFunction(self.c8))

        self.d8 = darkSquare(self)
        self.d8.setGeometry(QtCore.QRect(210, 0, 70, 70))
        self.d8.setupLabel(font, "d8", "blackQueen")
        self.d8.clicked.connect(lambda: self.moveFunction(self.d8))

        self.e8 = lightSquare(self)
        self.e8.setGeometry(QtCore.QRect(280, 0, 70, 70))
        self.e8.setupLabel(font, "e8", "blackKing")
        self.e8.clicked.connect(lambda: self.moveFunction(self.e8))

        self.f8 = darkSquare(self)
        self.f8.setGeometry(QtCore.QRect(350, 0, 70, 70))
        self.f8.setupLabel(font, "f8", "blackFBishop")
        self.f8.clicked.connect(lambda: self.moveFunction(self.f8))

        self.g8 = lightSquare(self)
        self.g8.setGeometry(QtCore.QRect(420, 0, 70, 70))
        self.g8.setupLabel(font, "g8", "blackGKnight")
        self.g8.clicked.connect(lambda: self.moveFunction(self.g8))

        self.h8 = darkSquare(self)
        self.h8.setGeometry(QtCore.QRect(490, 0, 70, 70))
        self.h8.setupLabel(font, "h8", "blackHRook")
        self.h8.clicked.connect(lambda: self.moveFunction(self.h8))

        self.a7 = darkSquare(self)
        self.a7.setGeometry(QtCore.QRect(0, 70, 70, 70))
        self.a7.setupLabel(font, "a7", "blackAPawn")
        self.a7.clicked.connect(lambda: self.moveFunction(self.a7))

        self.b7 = lightSquare(self)
        self.b7.setGeometry(QtCore.QRect(70, 70, 70, 70))
        self.b7.setupLabel(font, "b7", "blackBPawn")
        self.b7.clicked.connect(lambda: self.moveFunction(self.b7))

        self.c7 = darkSquare(self)
        self.c7.setGeometry(QtCore.QRect(140, 70, 70, 70))
        self.c7.setupLabel(font, "c7", "blackCPawn")
        self.c7.clicked.connect(lambda: self.moveFunction(self.c7))

        self.d7 = lightSquare(self)
        self.d7.setGeometry(QtCore.QRect(210, 70, 70, 70))
        self.d7.setupLabel(font, "d7", "blackDPawn")
        self.d7.clicked.connect(lambda: self.moveFunction(self.d7))

        self.e7 = darkSquare(self)
        self.e7.setGeometry(QtCore.QRect(280, 70, 70, 70))
        self.e7.setupLabel(font, "e7", "blackEPawn")
        self.e7.clicked.connect(lambda: self.moveFunction(self.e7))

        self.f7 = lightSquare(self)
        self.f7.setGeometry(QtCore.QRect(350, 70, 70, 70))
        self.f7.setupLabel(font, "f7", "blackFPawn")
        self.f7.clicked.connect(lambda: self.moveFunction(self.f7))

        self.g7 = darkSquare(self)
        self.g7.setGeometry(QtCore.QRect(420, 70, 70, 70))
        self.g7.setupLabel(font, "g7", "blackGPawn")
        self.g7.clicked.connect(lambda: self.moveFunction(self.g7))

        self.h7 = lightSquare(self)
        self.h7.setGeometry(QtCore.QRect(490, 70, 70, 70))
        self.h7.setupLabel(font, "h7", "blackHPawn")
        self.h7.clicked.connect(lambda: self.moveFunction(self.h7))

        self.a6 = lightSquare(self)
        self.a6.setGeometry(QtCore.QRect(0, 140, 70, 70))
        self.a6.setupLabel(font, "a6", "False")
        self.a6.clicked.connect(lambda: self.moveFunction(self.a6))

        self.b6 = darkSquare(self)
        self.b6.setGeometry(QtCore.QRect(70, 140, 70, 70))
        self.b6.setupLabel(font, "b6", "False")
        self.b6.clicked.connect(lambda: self.moveFunction(self.b6))

        self.c6 = lightSquare(self)
        self.c6.setGeometry(QtCore.QRect(140, 140, 70, 70))
        self.c6.setupLabel(font, "c6", "False")
        self.c6.clicked.connect(lambda: self.moveFunction(self.c6))

        self.d6 = darkSquare(self)
        self.d6.setGeometry(QtCore.QRect(210, 140, 70, 70))
        self.d6.setupLabel(font, "d6", "False")
        self.d6.clicked.connect(lambda: self.moveFunction(self.d6))

        self.e6 = lightSquare(self)
        self.e6.setGeometry(QtCore.QRect(280, 140, 70, 70))
        self.e6.setupLabel(font, "e6", "False")
        self.e6.clicked.connect(lambda: self.moveFunction(self.e6))

        self.f6 = darkSquare(self)
        self.f6.setGeometry(QtCore.QRect(350, 140, 70, 70))
        self.f6.setupLabel(font, "f6", "False")
        self.f6.clicked.connect(lambda: self.moveFunction(self.f6))

        self.g6 = lightSquare(self)
        self.g6.setGeometry(QtCore.QRect(420, 140, 70, 70))
        self.g6.setupLabel(font, "g6", "False")
        self.g6.clicked.connect(lambda: self.moveFunction(self.g6))

        self.h6 = darkSquare(self)
        self.h6.setGeometry(QtCore.QRect(490, 140, 70, 70))
        self.h6.setupLabel(font, "h6", "False")
        self.h6.clicked.connect(lambda: self.moveFunction(self.h6))

        self.a5 = darkSquare(self)
        self.a5.setGeometry(QtCore.QRect(0, 210, 70, 70))
        self.a5.setupLabel(font, "a5", "False")
        self.a5.clicked.connect(lambda: self.moveFunction(self.a5))

        self.b5 = lightSquare(self)
        self.b5.setGeometry(QtCore.QRect(70, 210, 70, 70))
        self.b5.setupLabel(font, "b5", "False")
        self.b5.clicked.connect(lambda: self.moveFunction(self.b5))

        self.c5 = darkSquare(self)
        self.c5.setGeometry(QtCore.QRect(140, 210, 70, 70))
        self.c5.setupLabel(font, "c5", "False")
        self.c5.clicked.connect(lambda: self.moveFunction(self.c5))

        self.d5 = lightSquare(self)
        self.d5.setGeometry(QtCore.QRect(210, 210, 70, 70))
        self.d5.setupLabel(font, "d5", "False")
        self.d5.clicked.connect(lambda: self.moveFunction(self.d5))

        self.e5 = darkSquare(self)
        self.e5.setGeometry(QtCore.QRect(280, 210, 70, 70))
        self.e5.setupLabel(font, "e5", "False")
        self.e5.clicked.connect(lambda: self.moveFunction(self.e5))

        self.f5 = lightSquare(self)
        self.f5.setGeometry(QtCore.QRect(350, 210, 70, 70))
        self.f5.setupLabel(font, "f5", "False")
        self.f5.clicked.connect(lambda: self.moveFunction(self.f5))

        self.g5 = darkSquare(self)
        self.g5.setGeometry(QtCore.QRect(420, 210, 70, 70))
        self.g5.setupLabel(font, "g5", "False")
        self.g5.clicked.connect(lambda: self.moveFunction(self.g5))

        self.h5 = lightSquare(self)
        self.h5.setGeometry(QtCore.QRect(490, 210, 70, 70))
        self.h5.setupLabel(font, "h5", "False")
        self.h5.clicked.connect(lambda: self.moveFunction(self.h5))

        self.a4 = lightSquare(self)
        self.a4.setGeometry(QtCore.QRect(0, 280, 70, 70))
        self.a4.setupLabel(font, "a4", "False")
        self.a4.clicked.connect(lambda: self.moveFunction(self.a4))

        self.b4 = darkSquare(self)
        self.b4.setGeometry(QtCore.QRect(70, 280, 70, 70))
        self.b4.setupLabel(font, "b4", "False")
        self.b4.clicked.connect(lambda: self.moveFunction(self.b4))

        self.c4 = lightSquare(self)
        self.c4.setGeometry(QtCore.QRect(140, 280, 70, 70))
        self.c4.setupLabel(font, "c4", "False")
        self.c4.clicked.connect(lambda: self.moveFunction(self.c4))

        self.d4 = darkSquare(self)
        self.d4.setGeometry(QtCore.QRect(210, 280, 70, 70))
        self.d4.setupLabel(font, "d4", "False")
        self.d4.clicked.connect(lambda: self.moveFunction(self.d4))

        self.e4 = lightSquare(self)
        self.e4.setGeometry(QtCore.QRect(280, 280, 70, 70))
        self.e4.setupLabel(font, "e4", "False")
        self.e4.clicked.connect(lambda: self.moveFunction(self.e4))

        self.f4 = darkSquare(self)
        self.f4.setGeometry(QtCore.QRect(350, 280, 70, 70))
        self.f4.setupLabel(font, "f4", "False")
        self.f4.clicked.connect(lambda: self.moveFunction(self.f4))

        self.g4 = lightSquare(self)
        self.g4.setGeometry(QtCore.QRect(420, 280, 70, 70))
        self.g4.setupLabel(font, "g4", "False")
        self.g4.clicked.connect(lambda: self.moveFunction(self.g4))

        self.h4 = darkSquare(self)
        self.h4.setGeometry(QtCore.QRect(490, 280, 70, 70))
        self.h4.setupLabel(font, "h4", "False")
        self.h4.clicked.connect(lambda: self.moveFunction(self.h4))

        self.a3 = darkSquare(self)
        self.a3.setGeometry(QtCore.QRect(0, 350, 70, 70))
        self.a3.setupLabel(font, "a3", "False")
        self.a3.clicked.connect(lambda: self.moveFunction(self.a3))

        self.b3 = lightSquare(self)
        self.b3.setGeometry(QtCore.QRect(70, 350, 70, 70))
        self.b3.setupLabel(font, "b3", "False")
        self.b3.clicked.connect(lambda: self.moveFunction(self.b3))

        self.c3 = darkSquare(self)
        self.c3.setGeometry(QtCore.QRect(140, 350, 70, 70))
        self.c3.setupLabel(font, "c3", "False")
        self.c3.clicked.connect(lambda: self.moveFunction(self.c3))

        self.d3 = lightSquare(self)
        self.d3.setGeometry(QtCore.QRect(210, 350, 70, 70))
        self.d3.setupLabel(font, "d3", "False")
        self.d3.clicked.connect(lambda: self.moveFunction(self.d3))

        self.e3 = darkSquare(self)
        self.e3.setGeometry(QtCore.QRect(280, 350, 70, 70))
        self.e3.setupLabel(font, "e3", "False")
        self.e3.clicked.connect(lambda: self.moveFunction(self.e3))

        self.f3 = lightSquare(self)
        self.f3.setGeometry(QtCore.QRect(350, 350, 70, 70))
        self.f3.setupLabel(font, "f3", "False")
        self.f3.clicked.connect(lambda: self.moveFunction(self.f3))

        self.g3 = darkSquare(self)
        self.g3.setGeometry(QtCore.QRect(420, 350, 70, 70))
        self.g3.setupLabel(font, "g3", "False")
        self.g3.clicked.connect(lambda: self.moveFunction(self.g3))

        self.h3 = lightSquare(self)
        self.h3.setGeometry(QtCore.QRect(490, 350, 70, 70))
        self.h3.setupLabel(font, "h3", "False")
        self.h3.clicked.connect(lambda: self.moveFunction(self.h3))

        self.a2 = lightSquare(self)
        self.a2.setGeometry(QtCore.QRect(0, 420, 70, 70))
        self.a2.setupLabel(font, "a2", "whiteAPawn")
        self.a2.clicked.connect(lambda: self.moveFunction(self.a2))

        self.b2 = darkSquare(self)
        self.b2.setGeometry(QtCore.QRect(70, 420, 70, 70))
        self.b2.setupLabel(font, "b2", "whiteBPawn")
        self.b2.clicked.connect(lambda: self.moveFunction(self.b2))

        self.c2 = lightSquare(self)
        self.c2.setGeometry(QtCore.QRect(140, 420, 70, 70))
        self.c2.setupLabel(font, "c2", "whiteCPawn")
        self.c2.clicked.connect(lambda: self.moveFunction(self.c2))

        self.d2 = darkSquare(self)
        self.d2.setGeometry(QtCore.QRect(210, 420, 70, 70))
        self.d2.setupLabel(font, "d2", "whiteDPawn")
        self.d2.clicked.connect(lambda: self.moveFunction(self.d2))

        self.e2 = lightSquare(self)
        self.e2.setGeometry(QtCore.QRect(280, 420, 70, 70))
        self.e2.setupLabel(font, "e2", "whiteEPawn")
        self.e2.clicked.connect(lambda: self.moveFunction(self.e2))

        self.f2 = darkSquare(self)
        self.f2.setGeometry(QtCore.QRect(350, 420, 70, 70))
        self.f2.setupLabel(font, "f2", "whiteFPawn")
        self.f2.clicked.connect(lambda: self.moveFunction(self.f2))

        self.g2 = lightSquare(self)
        self.g2.setGeometry(QtCore.QRect(420, 420, 70, 70))
        self.g2.setupLabel(font, "g2", "whiteGPawn")
        self.g2.clicked.connect(lambda: self.moveFunction(self.g2))

        self.h2 = darkSquare(self)
        self.h2.setGeometry(QtCore.QRect(490, 420, 70, 70))
        self.h2.setupLabel(font, "h2", "whiteHPawn")
        self.h2.clicked.connect(lambda: self.moveFunction(self.h2))

        self.a1 = darkSquare(self)
        self.a1.setGeometry(QtCore.QRect(0, 490, 70, 70))
        self.a1.setupLabel(font, "a1", "whiteARook")
        self.a1.clicked.connect(lambda: self.moveFunction(self.a1))

        self.b1 = lightSquare(self)
        self.b1.setGeometry(QtCore.QRect(70, 490, 70, 70))
        self.b1.setupLabel(font, "b1", "whiteBKnight")
        self.b1.clicked.connect(lambda: self.moveFunction(self.b1))

        self.c1 = darkSquare(self)
        self.c1.setGeometry(QtCore.QRect(140, 490, 70, 70))
        self.c1.setupLabel(font, "c1", "whiteCBishop")
        self.c1.clicked.connect(lambda: self.moveFunction(self.c1))

        self.d1 = lightSquare(self)
        self.d1.setGeometry(QtCore.QRect(210, 490, 70, 70))
        self.d1.setupLabel(font, "d1", "whiteQueen")
        self.d1.clicked.connect(lambda: self.moveFunction(self.d1))

        self.e1 = darkSquare(self)
        self.e1.setGeometry(QtCore.QRect(280, 490, 70, 70))
        self.e1.setupLabel(font, "e1", "whiteKing")
        self.e1.clicked.connect(lambda: self.moveFunction(self.e1))

        self.f1 = lightSquare(self)
        self.f1.setGeometry(QtCore.QRect(350, 490, 70, 70))
        self.f1.setupLabel(font, "f1", "whiteFBishop")
        self.f1.clicked.connect(lambda: self.moveFunction(self.f1))

        self.g1 = darkSquare(self)
        self.g1.setGeometry(QtCore.QRect(420, 490, 70, 70))
        self.g1.setupLabel(font, "g1", "whiteGKnight")
        self.g1.clicked.connect(lambda: self.moveFunction(self.g1))

        self.h1 = lightSquare(self)
        self.h1.setGeometry(QtCore.QRect(490, 490, 70, 70))
        self.h1.setupLabel(font, "h1", "whiteHRook")
        self.h1.clicked.connect(lambda: self.moveFunction(self.h1))

        # <---- now declaring all pieces ---->

        # next block of code declares each piece along with
        # starting position, image file path

        self.blackARook = piece(self)
        self.blackARook.setGeometry(QtCore.QRect(5, 5, 60, 60))
        self.blackARook.setupLabel("black", "blackARook", "Rook", "a8")
        self.blackARook.clicked.connect(lambda: self.moveFunction(self.blackARook))

        self.blackBKnight = piece(self)
        self.blackBKnight.setGeometry(QtCore.QRect(75, 5, 60, 60))
        self.blackBKnight.setupLabel("black", "blackBKnight", "Knight", "b8")
        self.blackBKnight.clicked.connect(lambda: self.moveFunction(self.blackBKnight))

        self.blackCBishop = piece(self)
        self.blackCBishop.setGeometry(QtCore.QRect(145, 5, 60, 60))
        self.blackCBishop.setupLabel("black", "blackCBishop", "Bishop", "c8")
        self.blackCBishop.clicked.connect(lambda: self.moveFunction(self.blackCBishop))

        self.blackQueen = piece(self)
        self.blackQueen.setGeometry(QtCore.QRect(215, 5, 60, 60))
        self.blackQueen.setupLabel("black", "blackQueen", "Queen", "d8")
        self.blackQueen.clicked.connect(lambda: self.moveFunction(self.blackQueen))

        self.blackKing = piece(self)
        self.blackKing.setGeometry(QtCore.QRect(285, 5, 60, 60))
        self.blackKing.setupLabel("black", "blackKing", "King", "e8")
        self.blackKing.clicked.connect(lambda: self.moveFunction(self.blackKing))

        self.blackFBishop = piece(self)
        self.blackFBishop.setGeometry(QtCore.QRect(355, 5, 60, 60))
        self.blackFBishop.setupLabel("black", "blackFBishop", "Bishop", "f8")
        self.blackFBishop.clicked.connect(lambda: self.moveFunction(self.blackFBishop))

        self.blackGKnight = piece(self)
        self.blackGKnight.setGeometry(QtCore.QRect(425, 5, 60, 60))
        self.blackGKnight.setupLabel("black", "blackGKnight", "Knight", "g8")
        self.blackGKnight.clicked.connect(lambda: self.moveFunction(self.blackGKnight))

        self.blackHRook = piece(self)
        self.blackHRook.setGeometry(QtCore.QRect(495, 5, 60, 60))
        self.blackHRook.setupLabel("black", "blackHRook", "Rook", "h8")
        self.blackHRook.clicked.connect(lambda: self.moveFunction(self.blackHRook))

        self.blackAPawn = piece(self)
        self.blackAPawn.setGeometry(QtCore.QRect(5, 75, 60, 60))
        self.blackAPawn.setupLabel("black", "blackAPawn", "Pawn", "a7")
        self.blackAPawn.clicked.connect(lambda: self.moveFunction(self.blackAPawn))

        self.blackBPawn = piece(self)
        self.blackBPawn.setGeometry(QtCore.QRect(75, 75, 60, 60))
        self.blackBPawn.setupLabel("black", "blackBPawn", "Pawn", "b7")
        self.blackBPawn.clicked.connect(lambda: self.moveFunction(self.blackBPawn))

        self.blackCPawn = piece(self)
        self.blackCPawn.setGeometry(QtCore.QRect(145, 75, 60, 60))
        self.blackCPawn.setupLabel("black", "blackCPawn", "Pawn", "c7")
        self.blackCPawn.clicked.connect(lambda: self.moveFunction(self.blackCPawn))

        self.blackDPawn = piece(self)
        self.blackDPawn.setGeometry(QtCore.QRect(215, 75, 60, 60))
        self.blackDPawn.setupLabel("black", "blackDPawn", "Pawn", "d7")
        self.blackDPawn.clicked.connect(lambda: self.moveFunction(self.blackDPawn))

        self.blackEPawn = piece(self)
        self.blackEPawn.setGeometry(QtCore.QRect(285, 75, 60, 60))
        self.blackEPawn.setupLabel("black", "blackEPawn", "Pawn", "e7")
        self.blackEPawn.clicked.connect(lambda: self.moveFunction(self.blackEPawn))

        self.blackFPawn = piece(self)
        self.blackFPawn.setGeometry(QtCore.QRect(355, 75, 60, 60))
        self.blackFPawn.setupLabel("black", "blackFPawn", "Pawn", "f7")
        self.blackFPawn.clicked.connect(lambda: self.moveFunction(self.blackFPawn))

        self.blackGPawn = piece(self)
        self.blackGPawn.setGeometry(QtCore.QRect(425, 75, 60, 60))
        self.blackGPawn.setupLabel("black", "blackGPawn", "Pawn", "g7")
        self.blackGPawn.clicked.connect(lambda: self.moveFunction(self.blackGPawn))

        self.blackHPawn = piece(self)
        self.blackHPawn.setGeometry(QtCore.QRect(495, 75, 60, 60))
        self.blackHPawn.setupLabel("black", "blackHPawn", "Pawn", "h7")
        self.blackHPawn.clicked.connect(lambda: self.moveFunction(self.blackHPawn))

        self.whiteARook = piece(self)
        self.whiteARook.setGeometry(QtCore.QRect(5, 495, 60, 60))
        self.whiteARook.setupLabel("white", "whiteARook", "Rook", "a1")
        self.whiteARook.clicked.connect(lambda: self.moveFunction(self.whiteARook))

        self.whiteBKnight = piece(self)
        self.whiteBKnight.setGeometry(QtCore.QRect(75, 495, 60, 60))
        self.whiteBKnight.setupLabel("white", "whiteBKnight", "Knight", "b1")
        self.whiteBKnight.clicked.connect(lambda: self.moveFunction(self.whiteBKnight))

        self.whiteCBishop = piece(self)
        self.whiteCBishop.setGeometry(QtCore.QRect(145, 495, 60, 60))
        self.whiteCBishop.setupLabel("white", "whiteCBishop", "Bishop", "c1")
        self.whiteCBishop.clicked.connect(lambda: self.moveFunction(self.whiteCBishop))

        self.whiteQueen = piece(self)
        self.whiteQueen.setGeometry(QtCore.QRect(215, 495, 60, 60))
        self.whiteQueen.setupLabel("white", "whiteQueen", "Queen", "d1")
        self.whiteQueen.clicked.connect(lambda: self.moveFunction(self.whiteQueen))

        self.whiteKing = piece(self)
        self.whiteKing.setGeometry(QtCore.QRect(285, 495, 60, 60))
        self.whiteKing.setupLabel("white", "whiteKing", "King", "e1")
        self.whiteKing.clicked.connect(lambda: self.moveFunction(self.whiteKing))

        self.whiteFBishop = piece(self)
        self.whiteFBishop.setGeometry(QtCore.QRect(355, 495, 60, 60))
        self.whiteFBishop.setupLabel("white", "whiteFBishop", "Bishop", "f1")
        self.whiteFBishop.clicked.connect(lambda: self.moveFunction(self.whiteFBishop))

        self.whiteGKnight = piece(self)
        self.whiteGKnight.setGeometry(QtCore.QRect(425, 495, 60, 60))
        self.whiteGKnight.setupLabel("white", "whiteGKnight", "Knight", "g1")
        self.whiteGKnight.clicked.connect(lambda: self.moveFunction(self.whiteGKnight))

        self.whiteHRook = piece(self)
        self.whiteHRook.setGeometry(QtCore.QRect(495, 495, 60, 60))
        self.whiteHRook.setupLabel("white", "whiteHRook", "Rook", "h1")
        self.whiteHRook.clicked.connect(lambda: self.moveFunction(self.whiteHRook))

        self.whiteAPawn = piece(self)
        self.whiteAPawn.setGeometry(QtCore.QRect(5, 425, 60, 60))
        self.whiteAPawn.setupLabel("white", "whiteAPawn", "Pawn", "a2")
        self.whiteAPawn.clicked.connect(lambda: self.moveFunction(self.whiteAPawn))

        self.whiteBPawn = piece(self)
        self.whiteBPawn.setGeometry(QtCore.QRect(75, 425, 60, 60))
        self.whiteBPawn.setupLabel("white", "whiteBPawn", "Pawn", "b2")
        self.whiteBPawn.clicked.connect(lambda: self.moveFunction(self.whiteBPawn))

        self.whiteCPawn = piece(self)
        self.whiteCPawn.setGeometry(QtCore.QRect(145, 425, 60, 60))
        self.whiteCPawn.setupLabel("white", "whiteCPawn", "Pawn", "c2")
        self.whiteCPawn.clicked.connect(lambda: self.moveFunction(self.whiteCPawn))

        self.whiteDPawn = piece(self)
        self.whiteDPawn.setGeometry(QtCore.QRect(215, 425, 60, 60))
        self.whiteDPawn.setupLabel("white", "whiteDPawn", "Pawn", "d2")
        self.whiteDPawn.clicked.connect(lambda: self.moveFunction(self.whiteDPawn))

        self.whiteEPawn = piece(self)
        self.whiteEPawn.setGeometry(QtCore.QRect(285, 425, 60, 60))
        self.whiteEPawn.setupLabel("white", "whiteEPawn", "Pawn", "e2")
        self.whiteEPawn.clicked.connect(lambda: self.moveFunction(self.whiteEPawn))

        self.whiteFPawn = piece(self)
        self.whiteFPawn.setGeometry(QtCore.QRect(355, 425, 60, 60))
        self.whiteFPawn.setupLabel("white", "whiteFPawn", "Pawn", "f2")
        self.whiteFPawn.clicked.connect(lambda: self.moveFunction(self.whiteFPawn))

        self.whiteGPawn = piece(self)
        self.whiteGPawn.setGeometry(QtCore.QRect(425, 425, 60, 60))
        self.whiteGPawn.setupLabel("white", "whiteGPawn", "Pawn", "g2")
        self.whiteGPawn.clicked.connect(lambda: self.moveFunction(self.whiteGPawn))

        self.whiteHPawn = piece(self)
        self.whiteHPawn.setGeometry(QtCore.QRect(495, 425, 60, 60))
        self.whiteHPawn.setupLabel("white", "whiteHPawn", "Pawn", "h2")
        self.whiteHPawn.clicked.connect(lambda: self.moveFunction(self.whiteHPawn))

        self.coverScreen = QLabel(self)
        self.coverScreen.setGeometry(QtCore.QRect(0, 0, 560, 560))
        self.coverScreen.setStyleSheet("background: rgba(255, 0, 0, 0);")
        self.coverScreen.setHidden(True)

        font.setPointSize(36)

        self.gameOverLabel = QLabel(self)
        self.gameOverLabel.setGeometry(QtCore.QRect(155, 220, 250, 120))
        self.gameOverLabel.setFont(font)
        self.gameOverLabel.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.gameOverLabel.setStyleSheet("background-color: rgb(50, 50, 50); padding: 1; border-radius: 10px;")
        self.gameOverLabel.setHidden(True)

        font.setPointSize(20)

        self.playAgainButton = QtWidgets.QPushButton(self)
        self.playAgainButton.setGeometry(QtCore.QRect(190, 290, 180, 40))
        self.playAgainButton.setFont(font)
        self.playAgainButton.setObjectName("playAgain")
        self.playAgainButton.setStyleSheet("background-color: rgb(238, 125, 55); border-radius: 5px")
        self.playAgainButton.clicked.connect(lambda: self.resetUi())
        self.playAgainButton.setHidden(True)

        self.promotionLabel = QLabel(self)
        self.promotionLabel.setGeometry(QtCore.QRect(185, 230, 190, 100))
        self.promotionLabel.setFont(font)
        self.promotionLabel.setAlignment(Qt.AlignCenter|Qt.AlignCenter)
        self.promotionLabel.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.promotionLabel.setHidden(True)

        font.setPointSize(16)

        self.knightButton = QtWidgets.QPushButton(self)
        self.knightButton.setGeometry(QtCore.QRect(195, 240, 80, 80))
        self.knightButton.setFont(font)
        self.knightButton.setObjectName("Knight")

        self.queenButton = QtWidgets.QPushButton(self)
        self.queenButton.setGeometry(QtCore.QRect(285, 240, 80, 80))
        self.queenButton.setFont(font)
        self.queenButton.setObjectName("Queen")

        # calls log in function which checks the input of username and password
        # passes in the self of the group window to allow access to the stacked widget
        self.knightButton.clicked.connect(lambda: self.promotionEvent("Knight", "N"))
        self.queenButton.clicked.connect(lambda: self.promotionEvent("Queen", "Q"))

        self.knightButton.setHidden(True)
        self.queenButton.setHidden(True)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def resetUi(self):
        self.currentMove = [False, -1, [], 0, [], [], ""]

        self.moveActive = False
        self.pieceBeingMoved = -1
        self.validTiles = []
        self.moveNumber = 0
        self.attackers = []
        self.previousMove = []
        self.pgn = ""

        # font is declared once as it doesn't change
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(14)
        font.setBold(True)

        self.a8.setupLabel(font, "a8", "blackARook")

        self.b8.setupLabel(font, "b8", "blackBKnight")
        
        self.c8.setupLabel(font, "c8", "blackCBishop")
        
        self.d8.setupLabel(font, "d8", "blackQueen")
        
        self.e8.setupLabel(font, "e8", "blackKing")
        
        self.f8.setupLabel(font, "f8", "blackFBishop")
        
        self.g8.setupLabel(font, "g8", "blackGKnight")
        
        self.h8.setupLabel(font, "h8", "blackHRook")
        
        self.a7.setupLabel(font, "a7", "blackAPawn")
        
        self.b7.setupLabel(font, "b7", "blackBPawn")
        
        self.c7.setupLabel(font, "c7", "blackCPawn")
        
        self.d7.setupLabel(font, "d7", "blackDPawn")
        
        self.e7.setupLabel(font, "e7", "blackEPawn")
        
        self.f7.setupLabel(font, "f7", "blackFPawn")
        
        self.g7.setupLabel(font, "g7", "blackGPawn")
        
        self.h7.setupLabel(font, "h7", "blackHPawn")
        
        self.a6.setupLabel(font, "a6", "False")
        
        self.b6.setupLabel(font, "b6", "False")
        
        self.c6.setupLabel(font, "c6", "False")
        
        self.d6.setupLabel(font, "d6", "False")
        
        self.e6.setupLabel(font, "e6", "False")
        
        self.f6.setupLabel(font, "f6", "False")
        
        self.g6.setupLabel(font, "g6", "False")
        
        self.h6.setupLabel(font, "h6", "False")
        
        self.a5.setupLabel(font, "a5", "False")
        
        self.b5.setupLabel(font, "b5", "False")
        
        self.c5.setupLabel(font, "c5", "False")
        
        self.d5.setupLabel(font, "d5", "False")
        
        self.e5.setupLabel(font, "e5", "False")
        
        self.f5.setupLabel(font, "f5", "False")
        
        self.g5.setupLabel(font, "g5", "False")
        
        self.h5.setupLabel(font, "h5", "False")
        
        self.a4.setupLabel(font, "a4", "False")
        
        self.b4.setupLabel(font, "b4", "False")
        
        self.c4.setupLabel(font, "c4", "False")
        
        self.d4.setupLabel(font, "d4", "False")
        
        self.e4.setupLabel(font, "e4", "False")
        
        self.f4.setupLabel(font, "f4", "False")
        
        self.g4.setupLabel(font, "g4", "False")
        
        self.h4.setupLabel(font, "h4", "False")
        
        self.a3.setupLabel(font, "a3", "False")
        
        self.b3.setupLabel(font, "b3", "False")
        
        self.c3.setupLabel(font, "c3", "False")
        
        self.d3.setupLabel(font, "d3", "False")
        
        self.e3.setupLabel(font, "e3", "False")
        
        self.f3.setupLabel(font, "f3", "False")
        
        self.g3.setupLabel(font, "g3", "False")
        
        self.h3.setupLabel(font, "h3", "False")
        
        self.a2.setupLabel(font, "a2", "whiteAPawn")
        
        self.b2.setupLabel(font, "b2", "whiteBPawn")
        
        self.c2.setupLabel(font, "c2", "whiteCPawn")
        
        self.d2.setupLabel(font, "d2", "whiteDPawn")
        
        self.e2.setupLabel(font, "e2", "whiteEPawn")
        
        self.f2.setupLabel(font, "f2", "whiteFPawn")
        
        self.g2.setupLabel(font, "g2", "whiteGPawn")
        
        self.h2.setupLabel(font, "h2", "whiteHPawn")
        
        self.a1.setupLabel(font, "a1", "whiteARook")
        
        self.b1.setupLabel(font, "b1", "whiteBKnight")
        
        self.c1.setupLabel(font, "c1", "whiteCBishop")
        
        self.d1.setupLabel(font, "d1", "whiteQueen")
        
        self.e1.setupLabel(font, "e1", "whiteKing")
        
        self.f1.setupLabel(font, "f1", "whiteFBishop")
        
        self.g1.setupLabel(font, "g1", "whiteGKnight")
        
        self.h1.setupLabel(font, "h1", "whiteHRook")


        self.blackARook.setupLabel("black", "blackARook", "Rook", "a8")
        self.blackARook.move(5, 5)
        
        self.blackBKnight.setupLabel("black", "blackBKnight", "Knight", "b8")
        self.blackBKnight.move(75, 5)
        
        self.blackCBishop.setupLabel("black", "blackCBishop", "Bishop", "c8")
        self.blackCBishop.move(145, 5)
        
        self.blackQueen.setupLabel("black", "blackQueen", "Queen", "d8")
        self.blackQueen.move(215, 5)
        
        self.blackKing.setupLabel("black", "blackKing", "King", "e8")
        self.blackKing.move(285, 5)
        
        self.blackFBishop.setupLabel("black", "blackFBishop", "Bishop", "f8")
        self.blackFBishop.move(355, 5)
        
        self.blackGKnight.setupLabel("black", "blackGKnight", "Knight", "g8")
        self.blackGKnight.move(425, 5)
        
        self.blackHRook.setupLabel("black", "blackHRook", "Rook", "h8")
        self.blackHRook.move(495, 5)
        
        self.blackAPawn.setupLabel("black", "blackAPawn", "Pawn", "a7")
        self.blackAPawn.move(5, 75)
        
        self.blackBPawn.setupLabel("black", "blackBPawn", "Pawn", "b7")
        self.blackBPawn.move(75, 75)
        
        self.blackCPawn.setupLabel("black", "blackCPawn", "Pawn", "c7")
        self.blackCPawn.move(145, 75)
        
        self.blackDPawn.setupLabel("black", "blackDPawn", "Pawn", "d7")
        self.blackDPawn.move(215, 75)
        
        self.blackEPawn.setupLabel("black", "blackEPawn", "Pawn", "e7")
        self.blackEPawn.move(285, 75)
        
        self.blackFPawn.setupLabel("black", "blackFPawn", "Pawn", "f7")
        self.blackFPawn.move(355, 75)
        
        self.blackGPawn.setupLabel("black", "blackGPawn", "Pawn", "g7")
        self.blackGPawn.move(425, 75)
        
        self.blackHPawn.setupLabel("black", "blackHPawn", "Pawn", "h7")
        self.blackHPawn.move(495, 75)
        
        self.whiteARook.setupLabel("white", "whiteARook", "Rook", "a1")
        self.whiteARook.move(5, 495)
        
        self.whiteBKnight.setupLabel("white", "whiteBKnight", "Knight", "b1")
        self.whiteBKnight.move(75, 495)
        
        self.whiteCBishop.setupLabel("white", "whiteCBishop", "Bishop", "c1")
        self.whiteCBishop.move(145, 495)
        
        self.whiteQueen.setupLabel("white", "whiteQueen", "Queen", "d1")
        self.whiteQueen.move(215, 495)
        
        self.whiteKing.setupLabel("white", "whiteKing", "King", "e1")
        self.whiteKing.move(285, 495)
        
        self.whiteFBishop.setupLabel("white", "whiteFBishop", "Bishop", "f1")
        self.whiteFBishop.move(355, 495)
        
        self.whiteGKnight.setupLabel("white", "whiteGKnight", "Knight", "g1")
        self.whiteGKnight.move(425, 495)
        
        self.whiteHRook.setupLabel("white", "whiteHRook", "Rook", "h1")
        self.whiteHRook.move(495, 495)
        
        self.whiteAPawn.setupLabel("white", "whiteAPawn", "Pawn", "a2")
        self.whiteAPawn.move(5, 425)
        
        self.whiteBPawn.setupLabel("white", "whiteBPawn", "Pawn", "b2")
        self.whiteBPawn.move(75, 425)
        
        self.whiteCPawn.setupLabel("white", "whiteCPawn", "Pawn", "c2")
        self.whiteCPawn.move(145, 425)
        
        self.whiteDPawn.setupLabel("white", "whiteDPawn", "Pawn", "d2")
        self.whiteDPawn.move(215, 425)
        
        self.whiteEPawn.setupLabel("white", "whiteEPawn", "Pawn", "e2")
        self.whiteEPawn.move(285, 425)
        
        self.whiteFPawn.setupLabel("white", "whiteFPawn", "Pawn", "f2")
        self.whiteFPawn.move(355, 425)
        
        self.whiteGPawn.setupLabel("white", "whiteGPawn", "Pawn", "g2")
        self.whiteGPawn.move(425, 425)
        
        self.whiteHPawn.setupLabel("white", "whiteHPawn", "Pawn", "h2")
        self.whiteHPawn.move(495, 425)
        

        self.coverScreen.setHidden(True)
        self.gameOverLabel.setHidden(True)
        self.playAgainButton.setHidden(True)




    def promotionEvent(self, newPiece, alias):
        self.pgn = promotingTo(newPiece, self, alias, self.pgn, self.attackers, self.previousMove, self.moveNumber)




    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.a8.setText(_translate("chessBoard", "8"))
        self.a7.setText(_translate("chessBoard", "7"))
        self.a6.setText(_translate("chessBoard", "6"))
        self.a5.setText(_translate("chessBoard", "5"))
        self.a4.setText(_translate("chessBoard", "4"))
        self.a3.setText(_translate("chessBoard", "3"))
        self.a2.setText(_translate("chessBoard", "2"))
        self.a1.setText(_translate("chessBoard", "a1"))
        self.b1.setText(_translate("chessBoard", "b"))
        self.c1.setText(_translate("chessBoard", "c"))
        self.d1.setText(_translate("chessBoard", "d"))
        self.e1.setText(_translate("chessBoard", "e"))
        self.f1.setText(_translate("chessBoard", "f"))
        self.g1.setText(_translate("chessBoard", "g"))
        self.h1.setText(_translate("chessBoard", "h"))
        self.queenButton.setText(_translate("chessBoard", "Queen"))
        self.knightButton.setText(_translate("chessBoard", "Knight"))
        self.gameOverLabel.setText(_translate("chessBoard", "game over"))
        self.playAgainButton.setText(_translate("chessBoard", "Play Again!"))

