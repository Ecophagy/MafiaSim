from enum import Enum
import random

Starting_Mafia = 10
Starting_Town = 90
NumberOfGames = 10000
NumberOfTownWins = 0
Mafia_lynched = 0
Town_lynched = 0

class GameState(Enum):
    ONGOING = 1
    MAFIA_WIN = 2
    TOWN_WIN = 3
    ERROR = 4


def evaluateGameState(numOfMafia, numOfTown):
    if numOfMafia >= numOfTown:
        return GameState.MAFIA_WIN
    elif numOfMafia == 0:
        return GameState.TOWN_WIN
    elif numOfTown > numOfMafia:
        return GameState.ONGOING
    else:
        print("ERROR")
        return GameState.ERROR

for x in range(0, NumberOfGames):

    # Reset Game state
    Game_State = GameState.ONGOING
    NumberOfMafia = Starting_Mafia
    NumberOfTown = Starting_Town

    while Game_State == GameState.ONGOING:
        # Day Phase
        rand = random.random()
        mafiaLynchOdds = NumberOfMafia/(NumberOfTown+NumberOfMafia)
        if rand >= mafiaLynchOdds:
            # Town got lynched
            NumberOfTown -= 1
            Town_lynched += 1
        else:
            # Scum got lynched
            NumberOfMafia -= 1
            Mafia_lynched += 1

        # Is the game over?
        Game_State = evaluateGameState(NumberOfMafia, NumberOfTown)
        if Game_State != GameState.ONGOING:
            break

        # Night Phase. Town gets killed
        NumberOfTown -= 1

        # Is the game over?
        Game_State = evaluateGameState(NumberOfMafia, NumberOfTown)

    if Game_State == GameState.TOWN_WIN:
        NumberOfTownWins += 1

print ("Town Win Rate: " + str( NumberOfTownWins/NumberOfGames * 100))
print ("Mafia lynch rate: " + str (Mafia_lynched/(Mafia_lynched+Town_lynched)))
