from playerDB.jsonFunctions import *
from widgets.utilityWidgets.functions.playFunctions import ratingChange
import requests
from datetime import datetime

def getDailyPuzzle():
    response = requests.get("https://lichess.org/api/puzzle/daily")
    # response holds the url of the api
    # know where request is directed

    statCode = response.status_code
    # statcode holds the code response of the HTTP response
    # held in variable for if statement

    if statCode == 200:
        # if successful, json portion of request is stored

        result = response.json()
        moveList = result['game']['pgn']
        solution = result['puzzle']['solution']
        tournament = result['game']['perf']['name']
        matchup = result['game']['players'][0]['name'] + " Vs " + result['game']['players'][1]['name']
        puzzleRating = result['puzzle']['rating']

        # solution = ['Qh3', 'Rh8', 'Qxf1', 'Qxf1', 'Rxf1']

        return statCode, moveList, solution, tournament, matchup, puzzleRating

    else: 
        # if unsuccessful, code is printed to show error
        return statCode, [], [], "", "", 0

def goToDaily(dashboard):
    queryStatus, moveList, solution, tournament, matchup, puzzleRating = getDailyPuzzle()

    if queryStatus == 200:
        userId = dashboard.baseWindow.userId

        record = getData("puzzles", userId = userId, puzzleId = moveList)

        newSolution = getSolution(dashboard, moveList, solution)

        if len(record) == 0 or record[0]["finished"] == False:
            if len(record) == 0:
                newRecord = {
                    "userId": userId,
                    "puzzleId": moveList,
                    "finished": False,
                    "outcome": "unfinished",
                    "solution": newSolution,
                    "tournament": tournament,
                    "matchup": matchup,
                    "puzzleRating": puzzleRating
                }

                insert("puzzles", newRecord)

            goToDailyStage2(dashboard, moveList, newSolution, tournament, matchup, puzzleRating)

        else:
            goToDailyStage3(dashboard, moveList, newSolution, record[0]["outcome"], tournament, matchup, puzzleRating)

    else:
        print("query fail")


def goToDailyStage2(dashboard, moveList, solution, tournament, matchup, puzzleRating):
    dashboard.dailyStage2Widget.resetUi()

    dashboard.puzzleChessBoard.resetUi()
    dashboard.puzzleChessBoard.runPgn(moveList)
    dashboard.puzzleChessBoard.coverScreen.setHidden(True)

    userId = dashboard.baseWindow.userId

    userRecord = getData("users", id = userId)
    userRecord = userRecord[0]

    dashboard.dailyStage2Widget.currentUserLabel.setText(f'{userRecord["username"]}:')
    dashboard.dailyStage2Widget.currentUserPuzzleRatingLabel.setText(f'Puzzle Rating: {str(userRecord["puzzleRating"])}')
    dashboard.dailyStage2Widget.currentUserPuzzleRating = userRecord["puzzleRating"]

    dashboard.dailyStage2Widget.tournamentLabel.setText(tournament)
    dashboard.dailyStage2Widget.matchupLabel.setText(matchup)
    dashboard.dailyStage2Widget.puzzleRatingLabel.setText(f"Rating: {str(puzzleRating)}")

    dashboard.dailyStage2Widget.puzzleRating = puzzleRating

    dashboard.dailyStage2Widget.ratingDelta = [ratingChange(userRecord["puzzleRating"], puzzleRating, 1, 100), ratingChange(userRecord["puzzleRating"], puzzleRating, 0, 100)]
    dashboard.dailyStage2Widget.deltaLabel.setText(f"Success {'+' if dashboard.dailyStage2Widget.ratingDelta[0] >= 0 else ''}{dashboard.dailyStage2Widget.ratingDelta[0]} / Loss {'+' if dashboard.dailyStage2Widget.ratingDelta[1] >= 0 else ''}{dashboard.dailyStage2Widget.ratingDelta[1]}")

    dashboard.dailyStage2Widget.solution = solution
    dashboard.dailyStage2Widget.moveList = moveList
    dashboard.dailyStage2Widget.currentMove = 0

    dashboard.dailyStage2Widget.moves = int((len(solution) + 1) / 2)
    dashboard.dailyStage2Widget.movesLabel.setText(f'Moves to Make: {str(dashboard.dailyStage2Widget.moves)}')

    dashboard.puzzleStackedWidget.setCurrentIndex(1)


def goToDailyStage3(dashboard, moveList, solution, outcome, tournament, matchup, puzzleRating):
    dashboard.dailyStage3Widget.resetUi()

    dashboard.puzzleChessBoard.resetUi()
    dashboard.puzzleChessBoard.coverScreen.setHidden(False)

    dashboard.dailyStage3Widget.moveList = moveList
    dashboard.dailyStage3Widget.solution = solution

    dashboard.puzzleChessBoard.runPgn(moveList)

    userRecord = getData("users", id = dashboard.baseWindow.userId)
    userRecord = userRecord[0]

    dashboard.dailyStage3Widget.currentUserLabel.setText(dashboard.dailyStage2Widget.currentUserLabel.text())

    try:
        dashboard.dailyStage3Widget.currentUserRatingLabel.setText(f"Rating: {dashboard.dailyStage2Widget.currentUserPuzzleRating} -> {userRecord['puzzleRating']}")

    except AttributeError as e:
        dashboard.dailyStage3Widget.currentUserRatingLabel.setText(f"Rating: {userRecord['puzzleRating']}")


    dashboard.dailyStage3Widget.tournamentLabel.setText(tournament)
    dashboard.dailyStage3Widget.matchupLabel.setText(matchup)
    dashboard.dailyStage3Widget.puzzleRatingLabel.setText(f'Rating: {puzzleRating}')

    if outcome == "Completed!":
        dashboard.dailyStage3Widget.userOutcomeLabel.setStyleSheet("color: rgb(50, 175, 61)")

    else:
        dashboard.dailyStage3Widget.userOutcomeLabel.setStyleSheet("color: rgb(175, 61, 50)")

    dashboard.dailyStage3Widget.userOutcomeLabel.setText(outcome)

    dashboard.dailyStage3Widget.pgnSolutionLabel.setText(' '.join(solution))

    dashboard.puzzleStackedWidget.setCurrentIndex(2)



def newMove(dashboard, pgn):
    if dashboard.puzzleStackedWidget.currentIndex() in (1, 2):
        activeWidget = dashboard.dailyStage2Widget
        puzzleId = dashboard.dailyStage2Widget.moveList

    else:
        activeWidget = dashboard.filterStage2Widget
        puzzleId = dashboard.filterStage2Widget.puzzleDict["fen"]

    # checks if move is a user move
    if activeWidget.currentMove / 2 == int(activeWidget.currentMove / 2):
        # gets the last move from the pgn set
        moveSet = pgn.split()

        if moveSet[-1] in ("1-0", "0-1", "1/2-1/2"):
            move = moveSet[-2]

        else:
            move = moveSet[-1]

        print(f"MOVE IS {move}")

        print(f"SOLUTION IS {activeWidget.solution}")

        if move == activeWidget.solution[activeWidget.currentMove]:
            # gets the colour of the next move
            if dashboard.puzzleChessBoard.moveNumber / 2 == int(dashboard.puzzleChessBoard.moveNumber / 2):
                colour = "white"
            
            else:
                colour = "black"

            # adds one to the current move
            activeWidget.currentMove += 1

            # if the current move is smaller than the length of the solution, a robot move must be made
            if activeWidget.currentMove < len(activeWidget.solution):
                # makes robot move
                dashboard.puzzleChessBoard.runPgnTurn(colour, activeWidget.solution[activeWidget.currentMove])

                activeWidget.currentMove += 1

            # adds a success to the puzzle record then goes to stage 3
            else:
                record = getData("puzzles", userId = dashboard.baseWindow.userId, puzzleId = puzzleId)
                record = record[0]

                record["finished"] = True
                record["outcome"] = "Completed!"

                update("puzzles", record, record["id"])

                userRecord = getData("users", id = dashboard.baseWindow.userId)
                userRecord = userRecord[0]

                newPuzzleRating = userRecord["puzzleRating"] + activeWidget.ratingDelta[0]

                userRecord["puzzleRating"] = newPuzzleRating

                update("users", userRecord, userRecord["id"])

                userId = userRecord["id"]
                timeInfo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                puzzleProgressRecord = {
                    "userId": userId,
                    "datetime": timeInfo,
                    "puzzleRating": newPuzzleRating
                }

                _ = insert("puzzleProgress", puzzleProgressRecord)

                if dashboard.puzzleStackedWidget.currentIndex() in (1, 2):
                    goToDailyStage3(dashboard, dashboard.dailyStage2Widget.moveList, dashboard.dailyStage2Widget.solution, 
                                "Completed!", dashboard.dailyStage2Widget.tournamentLabel.text(), 
                                dashboard.dailyStage2Widget.matchupLabel.text(), dashboard.dailyStage2Widget.puzzleRating)
                    
                else:
                    dashboard.filterStage3Widget.populate(dashboard, "Completed!", dashboard.filterStage2Widget.index)

                    dashboard.puzzleWidget.filterPuzzles[dashboard.filterStage2Widget.index]["outcome"] = "Completed!"

        # adds a fail to puzzle record then goes to stage 3
        else:
            record = getData("puzzles", userId = dashboard.baseWindow.userId, puzzleId = puzzleId)
            record = record[0]

            record["finished"] = True
            record["outcome"] = "Failed"

            update("puzzles", record, record["id"])

            userRecord = getData("users", id = dashboard.baseWindow.userId)
            userRecord = userRecord[0]

            newPuzzleRating = userRecord["puzzleRating"] + activeWidget.ratingDelta[1]

            userRecord["puzzleRating"] = newPuzzleRating

            update("users", userRecord, userRecord["id"])

            userId = userRecord["id"]
            timeInfo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            puzzleProgressRecord = {
                "userId": userId,
                "datetime": timeInfo,
                "puzzleRating": newPuzzleRating
            }

            _ = insert("puzzleProgress", puzzleProgressRecord)

            if dashboard.puzzleStackedWidget.currentIndex() in (1, 2):
                goToDailyStage3(dashboard, dashboard.dailyStage2Widget.moveList, dashboard.dailyStage2Widget.solution, 
                                "Failed", dashboard.dailyStage2Widget.tournamentLabel.text(), 
                                dashboard.dailyStage2Widget.matchupLabel.text(), dashboard.dailyStage2Widget.puzzleRating)
                
            else:
                dashboard.filterStage3Widget.populate(dashboard, "Failed", dashboard.filterStage2Widget.index)

                dashboard.puzzleWidget.filterPuzzles[dashboard.filterStage2Widget.index]["outcome"] = "Failed"
            
    # if move is a robot move, only needs to update the currentMove variable
    else:
        activeWidget.currentMove += 1



def goToPuzzleWidget(dashboard):
    dashboard.puzzleChessBoard.resetUi()
    dashboard.puzzleChessBoard.coverScreen.setHidden(False)

    dashboard.puzzleWidget.errorLabel.setHidden(True)
    dashboard.puzzleWidget.filterPuzzles = []

    dashboard.puzzleWidget.populate(dashboard.baseWindow.userId)
    dashboard.puzzleStackedWidget.setCurrentIndex(0)



def getSolution(dashboard, moveList, solution):
    dashboard.puzzleChessBoard.resetUi()

    fullMoveList = moveList.split() + solution
    dashboard.puzzleChessBoard.runPgn(fullMoveList)

    pgn = dashboard.puzzleChessBoard.pgn.split()

    dashboard.puzzleChessBoard.resetUi()

    print("FULL PGN FULL PGN FULL PGN")
    print(pgn)
    pgn = [value for index, value in enumerate(pgn) if index % 3 != 0]

    print("pgn after removing every third")

    reformattedSolution = pgn[len(solution) * -1:]

    return reformattedSolution


def getFenSolution(dashboard, fen, solution):
    dashboard.puzzleChessBoard.resetUi()
    dashboard.puzzleChessBoard.runFen(fen)

    dashboard.puzzleChessBoard.runPgn(solution)

    pgn = dashboard.puzzleChessBoard.pgn.split()

    dashboard.puzzleChessBoard.resetUi()

    print("FULL PGN FULL PGN FULL PGN")
    print(pgn)
    pgn = [item for item in pgn if not (item[:-1].isdigit() and item.endswith("."))]

    print("pgn after removing every third")

    reformattedSolution = pgn[len(solution) * -1:]

    print(reformattedSolution)

    return reformattedSolution


def goToFilterStage2(dashboard, stage1):
    puzzles = stage1.getParameters(dashboard)

    if puzzles != 400:
        stage1.filterPuzzles = puzzles

        for i in puzzles:
            puzzleRecord = {
                "finished": False,
                "outcome": "unfinished",
                "puzzleId": i["fen"],
                "puzzleRating": i["rating"],
                "solution": i["solution"],
                "userId": dashboard.baseWindow.userId
            }

            insert("puzzles", puzzleRecord)

        for i in range(1, len(puzzles) + 1):
            getattr(dashboard.filterStage2Widget, f"puzzle{i}Button").setHidden(False)
            getattr(dashboard.filterStage2Widget, f"puzzle{i}Button").setText(str(stage1.filterPuzzles[i - 1]["rating"]))

            getattr(dashboard.filterStage3Widget, f"puzzle{i}Button").setHidden(False)
            getattr(dashboard.filterStage3Widget, f"puzzle{i}Button").setText(str(stage1.filterPuzzles[i - 1]["rating"]))

        dashboard.filterStage2Widget.puzzle1Button.active = True
        dashboard.filterStage3Widget.puzzle1Button.active = True

        dashboard.filterStage2Widget.populate(dashboard, 0)

        dashboard.puzzleStackedWidget.setCurrentIndex(3)


def switchPuzzles(dashboard, index):
    if getattr(dashboard.filterStage2Widget, f"puzzle{index + 1}Button").active == False:
        puzzle = dashboard.puzzleWidget.filterPuzzles[index]

        dashboard.filterStage2Widget.puzzle1Button.active = False
        dashboard.filterStage2Widget.puzzle2Button.active = False
        dashboard.filterStage2Widget.puzzle3Button.active = False
        dashboard.filterStage2Widget.puzzle4Button.active = False
        dashboard.filterStage2Widget.puzzle5Button.active = False

        dashboard.filterStage3Widget.puzzle1Button.active = False
        dashboard.filterStage3Widget.puzzle2Button.active = False
        dashboard.filterStage3Widget.puzzle3Button.active = False
        dashboard.filterStage3Widget.puzzle4Button.active = False
        dashboard.filterStage3Widget.puzzle5Button.active = False

        getattr(dashboard.filterStage2Widget, f"puzzle{index + 1}Button").active = True
        getattr(dashboard.filterStage3Widget, f"puzzle{index + 1}Button").active = True

        if puzzle["outcome"] == "unfinished":
            dashboard.filterStage2Widget.populate(dashboard, index)
            dashboard.puzzleStackedWidget.setCurrentIndex(3)

        else:
            dashboard.filterStage3Widget.populate(dashboard, puzzle["outcome"], index)
            dashboard.puzzleStackedWidget.setCurrentIndex(4)


