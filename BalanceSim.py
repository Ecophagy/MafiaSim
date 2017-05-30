from enum import Enum
import random

NumberOfGames = 1000

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

def playGame(Starting_Mafia, Starting_Town):
    Mafia_lynched = 0
    Town_lynched = 0

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
        return GameState.TOWN_WIN

def playXGames(Starting_Mafia, Starting_Town, Number_Of_Games):
    town_wins = 0
    for x in range (0, Number_Of_Games):
        if playGame(Starting_Mafia, Starting_Town) == GameState.TOWN_WIN:
            town_wins+=1
    return (town_wins / Number_Of_Games)

#Find how many town is required to balance a certain size mafia
for Number_Of_Mafia in range (1, 10):
    town_players = 2
    Town_Win_Percentage = 0.0
    #run games until we get a balanced game with a nearly 50% town win rate
    while 0.49 >  Town_Win_Percentage  < 0.51:
        town_players+=1
        Town_Win_Percentage = playXGames(Number_Of_Mafia, town_players, NumberOfGames) #Play enough games to get a reliable win rate
    print(str(Number_Of_Mafia) + ":" + str(town_players))
    Town_Win_Percentage = 0.0 #reset


