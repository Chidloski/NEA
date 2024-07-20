import requests

response = requests.get("https://lichess.org/api/puzzle/daily")
# response holds the url of the api
# know where request is directed

statCode = response.status_code
# statcode holds the code response of the HTTP response
# held in variable for if statement

for i in range(97, 105):
    print(chr(i))

if statCode == 200:
    # if successful, json portion of request is stored

    result = response.json()
    moveset = result['game']['pgn']
    moveList = moveset.split()
    print(moveList)

else: 
    # if unsuccessful, code is printed to show error
    print(statCode)