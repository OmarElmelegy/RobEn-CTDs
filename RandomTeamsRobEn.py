import random

def main():
    TeamNums = int(input("Enter number of players in each team: "))
    while True:
        TotalNumPlayers = int(input("Enter total Num of players: "))
        if(TotalNumPlayers%TeamNums == 0):
            break
        else:
            print("Enter a number divisable by number of players in each team..")
            continue
    TotalNames = []
    n = TotalNumPlayers // TeamNums
    PlayersInput(TotalNumPlayers,TotalNames)
    RandomizeTeams(TotalNames,n,TeamNums)
    
def RandomizeTeams(TotalNames,n,TeamNums):
    random.shuffle(TotalNames)
    for i in range(n):
        print(f"Team {i} members are: ")
        for _ in range(0,TeamNums):
            print(f"[{TotalNames.pop(-1)}]",end=" ")
        print("\n")

def PlayersInput(TotalNumPlayers,TotalNames):
    for _ in range(TotalNumPlayers):
        name = input()
        if(name[2] == '-'):
            if(name[3] == ' '):
                TotalNames.append(name[4:])
            else:
                TotalNames.append(name[3:])
        else:
            TotalNames.append(name[2:])
main()