import os

l = [[" ", " ", " "],
     [" ", " ", " "],
     [" ", " ", " "]]

global isWinner, counter
isWinner = False
counter = 0

def printer():
     print("  | 1 | 2 | 3 |")
     print("1 |", l[0][0], "|", l[0][1], "|", l[0][2], "|")
     print("2 |", l[1][0], "|", l[1][1], "|", l[1][2], "|")
     print("3 |", l[2][0], "|", l[2][1], "|", l[2][2], "|")

def receiverX(row, col):
     l[row - 1][col - 1] = "X"
def receiverO(row, col):
     l[row - 1][col - 1] = "O"

def rowChecker():
     global isWinner
     for i in range(3):
          if l[i][0] == l[i][1] == l[i][2] == "X":
               isWinner = True
               return "X"
          elif l[i][0] == l[i][1] == l[i][2] == "O":
               isWinner = True
               return "O"
def colChecker():
     global isWinner
     for i in range(3):
          if l[0][i] == l[1][i] == l[2][i] == "X":
               isWinner = True
               return "X"
          elif l[0][i] == l[1][i] == l[2][i] == "O":
               isWinner = True
               return "O"
def diagChecker():
     global isWinner
     if (l[0][0] == l[1][1] == l[2][2] == "X") or (l[0][2] == l[1][1] == l[2][0] == "X"):
          isWinner = True
          return "X"
     elif (l[0][0] == l[1][1] == l[2][2] == "O") or (l[0][2] == l[1][1] == l[2][0] == "O"):
          isWinner = True
          return "O"

def winner():
     global isWinner
     if rowChecker() == "X" or colChecker() == "X" or diagChecker() == "X":
          print("Winner Is Player X")
          return True
     elif rowChecker() == "O" or colChecker() == "O" or diagChecker() == "O":
          print("Winner Is Player O")
          return True
     elif counter == 9:
          print("Draw")
          isWinner = True
          return True

def playerX():
     global playerXrow, playerXcol
     playerXrow = int(input("(X) Enter Row: "))
     while playerXrow < 1 or playerXrow > 3:
          print("Please Enter Valid Value")
          playerXrow = int(input("Enter Row: "))
     playerXcol = int(input("(X) Enter Col: "))
     while playerXcol < 1 or playerXcol > 3:
          print("Please Enter Valid Value")
          playerXcol = int(input("(X) Enter Col: "))
     while l[playerXrow - 1][playerXcol - 1] != " ":
          print("Place is already taken")
          playerXrow = int(input("(X) Enter Row: "))
          while playerXrow < 1 or playerXrow > 3:
               print("Please Enter Valid Value")
               playerXrow = int(input("(X) Enter Row: "))
          playerXcol = int(input("(X) Enter Col: "))
          while playerXcol < 1 or playerXcol > 3:
               print("Please Enter Valid Value")
               playerXcol = int(input("(X) Enter Col: "))
     receiverX(playerXrow, playerXcol)

def playerO():
     global playerOrow, playerOcol
     playerOrow = int(input("(O) Enter Row: "))
     while playerOrow < 1 or playerOrow > 3:
          print("Please Enter Valid Value")
          playerOrow = int(input("Enter Row: "))
     playerOcol = int(input("(O) Enter Col: "))
     while playerOcol < 1 or playerOcol > 3:
          print("Please Enter Valid Value")
          playerOcol = int(input("(O) Enter Col: "))
     while l[playerOrow - 1][playerOcol - 1] != " ":
          print("Place is already taken")
          playerOrow = int(input("(O) Enter Row: "))
          while playerOrow < 1 or playerOrow > 3:
               print("Please Enter Valid Value")
               playerOrow = int(input("(O) Enter Row: "))
          playerOcol = int(input("(O) Enter Col: "))
          while playerOcol < 1 or playerOcol > 3:
               print("Please Enter Valid Value")
               playerOcol = int(input("(O) Enter Col: "))
     receiverO(playerOrow, playerOcol)

def main():
     global counter
     os.system('cls')
     printer()
     while isWinner == False:
          playerX()
          counter += 1
          os.system('cls')
          printer()
          if winner():
               break
          playerO()
          counter += 1
          os.system('cls')
          printer()
          if winner():
               break
main()