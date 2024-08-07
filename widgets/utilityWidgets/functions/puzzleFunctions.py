from playerDB.jsonFunctions import *
from widgets.utilityWidgets.functions.playFunctions import ratingChange
import requests

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
    # checks if move is a user move
    if dashboard.dailyStage2Widget.currentMove / 2 == int(dashboard.dailyStage2Widget.currentMove / 2):
        # gets the last move from the pgn set
        moveSet = pgn.split()

        if moveSet[-1] in ("1-0", "0-1", "1/2-1/2"):
            move = moveSet[-2]

        else:
            move = moveSet[-1]

        print(f"MOVE IS {move}")

        if move == dashboard.dailyStage2Widget.solution[dashboard.dailyStage2Widget.currentMove]:
            # gets the colour of the next move
            if dashboard.puzzleChessBoard.moveNumber / 2 == int(dashboard.puzzleChessBoard.moveNumber / 2):
                colour = "white"
            
            else:
                colour = "black"

            # adds one to the current move
            dashboard.dailyStage2Widget.currentMove += 1

            # if the current move is smaller than the length of the solution, a robot move must be made
            if dashboard.dailyStage2Widget.currentMove < len(dashboard.dailyStage2Widget.solution):
                # makes robot move
                dashboard.puzzleChessBoard.runPgnTurn(colour, dashboard.dailyStage2Widget.solution[dashboard.dailyStage2Widget.currentMove])

                dashboard.dailyStage2Widget.currentMove += 1

            # adds a success to the puzzle record then goes to stage 3
            else:
                record = getData("puzzles", userId = dashboard.baseWindow.userId, puzzleId = dashboard.dailyStage2Widget.moveList)
                record = record[0]

                record["finished"] = True
                record["outcome"] = "Completed!"

                update("puzzles", record, record["id"])

                userRecord = getData("users", id = dashboard.baseWindow.userId)
                userRecord = userRecord[0]
                userRecord["puzzleRating"] = userRecord["puzzleRating"] + dashboard.dailyStage2Widget.ratingDelta[0]

                update("users", userRecord, userRecord["id"])

                goToDailyStage3(dashboard, dashboard.dailyStage2Widget.moveList, dashboard.dailyStage2Widget.solution, 
                            "Completed!", dashboard.dailyStage2Widget.tournamentLabel.text(), 
                            dashboard.dailyStage2Widget.matchupLabel.text(), dashboard.dailyStage2Widget.puzzleRating)

        # adds a fail to puzzle record then goes to stage 3
        else:
            record = getData("puzzles", userId = dashboard.baseWindow.userId, puzzleId = dashboard.dailyStage2Widget.moveList)
            record = record[0]

            record["finished"] = True
            record["outcome"] = "Failed"

            update("puzzles", record, record["id"])

            userRecord = getData("users", id = dashboard.baseWindow.userId)
            userRecord = userRecord[0]
            userRecord["puzzleRating"] = userRecord["puzzleRating"] + dashboard.dailyStage2Widget.ratingDelta[1]

            update("users", userRecord, userRecord["id"])
            
            goToDailyStage3(dashboard, dashboard.dailyStage2Widget.moveList, dashboard.dailyStage2Widget.solution, 
                            "Failed", dashboard.dailyStage2Widget.tournamentLabel.text(), 
                            dashboard.dailyStage2Widget.matchupLabel.text(), dashboard.dailyStage2Widget.puzzleRating)
            
    # if move is a robot move, only needs to update the currentMove variable
    else:
        dashboard.dailyStage2Widget.currentMove += 1


def goToPuzzleWidget(dashboard):
    dashboard.puzzleChessBoard.resetUi()

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