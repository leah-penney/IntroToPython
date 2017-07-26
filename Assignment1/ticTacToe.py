#This is my Tic Tac Toe game that I made. 
#by Leah Penney
square1 = "_"
square2 = "_"
square3 = "_"
square4 = "_"
square5 = "_"
square6 = "_"
square7 = "_"
square8 = "_"
square9 = "_"

# Read square numbers left to right
# 1|2|3
# 4|5|6
# 7|8|9


def showCurrentBoard(): 
    print("%s|%s|%s\n%s|%s|%s\n%s|%s|%s"%(square1, square2, square3, 
                                          square4, square5, square6, 
                                          square7, square8, square9))


def isThreeInARow(sA, sB, sC):
    allAreX = sA == "x" and sB == "x" and sC == "x" 
    allAreO = sA == "o" and sB == "o" and sC == "o" 
    return allAreX or allAreO

def boardIsFull(): 
    return not(square1 == "_" or square2 == "_" or square3 == "_" or 
               square4 == "_" or square5 == "_" or square6 == "_" or 
               square7 == "_" or square8 == "_" or square9 == "_")
        
num_turns = 1
whoPlays = "o"

isGameOver = False 

while (num_turns <= 9 and not isGameOver):
#   do stuff with current values  
    print (num_turns)
    print("it is currently the %s's turn"%(whoPlays))
    
    print("Here is your Tic Tac Toe Board:")
    print("1|2|3")
    print("4|5|6")
    print("7|8|9")

    squareChoice = input("Which square do you want? ")

    if (squareChoice == "1"): 
        square1 = whoPlays
    if (squareChoice == "2"): 
        square2 = whoPlays
    if (squareChoice == "3"): 
        square3 = whoPlays
    if (squareChoice == "4"): 
        square4 = whoPlays
    if (squareChoice == "5"): 
        square5 = whoPlays
    if (squareChoice == "6"): 
        square6 = whoPlays
    if (squareChoice == "7"): 
        square7 = whoPlays
    if (squareChoice == "8"): 
        square8 = whoPlays
    if (squareChoice == "9"): 
        square9 = whoPlays

    showCurrentBoard()

    didSomeoneWin = (
        isThreeInARow(square1, square4, square7) or
        isThreeInARow(square2, square5, square8) or
        isThreeInARow(square3, square6, square9) or
        isThreeInARow(square1, square2, square3) or
        isThreeInARow(square4, square5, square6) or
        isThreeInARow(square7, square8, square9) or
        isThreeInARow(square1, square5, square9) or
        isThreeInARow(square3, square5, square7))

    if (didSomeoneWin): 
        print("%s won!"%(whoPlays))

#   update values for next turn    
    num_turns = num_turns + 1
   
    if (whoPlays == "o"):
        whoPlays = "x"
    elif (whoPlays == "x"):
        whoPlays = "o"

    isGameOver = boardIsFull() or didSomeoneWin

print("Gameover")