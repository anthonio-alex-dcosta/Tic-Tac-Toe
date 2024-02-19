def sum(a,b,c):
    return a+b+c


def checkBoard():
    wins =[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in wins:
        if(sum(xState[i[0]],xState[i[1]],xState[i[2]])==3):
            return True
        if(sum(zState[i[0]],zState[i[1]],zState[i[2]])==3):
            return True


def placeCharacter(pos,char,count):
    pos2 = int(pos)-1
    global xState
    global zState
    if char == "X":
        xState[pos2] = 1
    elif char == "O":
        zState[pos2] = 1
    if count >= 4:
        return checkBoard()


def printBoard(xState,zState):
    zero = 'X' if xState[0] else ('O' if zState[0] else 1)
    one = 'X' if xState[1] else ('O' if zState[1] else 2)
    two = 'X' if xState[2] else ('O' if zState[2] else 3)
    three = 'X' if xState[3] else ('O' if zState[3] else 4)
    four = 'X' if xState[4] else ('O' if zState[4] else 5)
    five = 'X' if xState[5] else ('O' if zState[5] else 6)
    six = 'X' if xState[6] else ('O' if zState[6] else 7)
    seven = 'X' if xState[7] else ('O' if zState[7] else 8)
    eight = 'X' if xState[8] else ('O' if zState[8] else 9)
    print(f"-------------")
    print(f"| {zero} | {one} | {two} |")
    print(f"|---|---|---|")
    print(f"| {three} | {four} | {five} |")
    print(f"|---|---|---|")
    print(f"| {six} | {seven} | {eight} |")
    print(f"-------------")


def gameInitialization():
    global player1,player2
    player1 = input("Enter player 1's name:")
    player2 = input("Enter player 2's name:")
    print(f"{player1}, your character is X")
    print(f"{player2}, your character is O")


def runGame():
    counter = 0
    f=False
    p_name=None
    while counter<9:
        win = 0
        printBoard(xState,zState)
        if counter%2==0:
            if (placeCharacter(input(f"{player1}, where do you want to place 'X':"),'X',counter)):
                p_name = player1
                f = True
                break
        else:
            if (placeCharacter(input(f"{player2}, where do you want to place 'O':"),'O',counter)):
                p_name = player2
                f = True
                break
        counter+=1
    printBoard(xState,zState)
    if f == False:
        print("The game ends in a draw.")
    else:
        print(f"{p_name} has won the game!!!!")
      

xState =[0,0,0,0,0,0,0,0,0]
zState =[0,0,0,0,0,0,0,0,0]
board = [[1,2,3],[4,5,6],[7,8,9]]
player1 = player2 = None 
gameInitialization()
runGame()