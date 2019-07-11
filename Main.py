''' 
Interactive tic-tac-toe for two players, with readable code for learners
POTENTIAL BUGS: If input is not a number, game will crash :-(
    
--Created By Young Bytes--

'''

import random as ra


# Input Variables
p1 = ""
p2 = ""
winner = -1
victoryMsg = "WINNER WINNER CHICKEN DINNER! Congrats Player "
tieMsg = "Oops--Tie Game :-("
winCombos = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]


# Board objects
border = "____________"
sep =    "------------"
elem = ["1","2","3","4","5","6","7","8","9"]

# Output methods
def printBoard():
  
  count = 0;

  print(border)
  
  for j in range(3):
    
    for i in range(11):
      if((i+1) % 4 == 0):
        print("|",end="")
      elif((i+1) % 4 == 2):
          print(elem[count],end="")
          count += 1
      else:
        print(" ",end="")
    
    if(j!=2):
      print("\n"+sep)
    else:
      print("\n"+border+"\n")  

# Check board every round
def gameCheck1(arr):
  
  num = 0
  pos= []

  for i in range(len(arr)):
    if(arr[i] == "X"):
      num += 1
      pos.append(i+1)
  
  if num >= 3:
    for j in range(len(pos)-2):
      dif = (pos[j+2] - pos[j+1] == pos[j+1] - pos[j])
      wow = pos[j+1] - pos[j]

      if dif and (wow == 3 or wow == 4):
        return True
      elif dif and (wow == 1):
        if not ((3 in pos and 4 in pos) or (4 in pos and 5 in pos)):
          return True
  
  return False
def gameCheck2(arr):
  
  num = 0
  pos= []

  for i in range(len(arr)):
    if(arr[i] == "O"):
      num += 1
      pos.append(i+1)
  
  if num >= 3:
    for j in range(len(pos)-2):
      dif = (pos[j+2] - pos[j+1] == pos[j+1] - pos[j])
      wow = pos[j+1] - pos[j]

      if dif and (wow == 3 or wow == 4):
        return True
      elif dif and (wow == 1):
        if not ((3 in pos and 4 in pos) or (4 in pos and 5 in pos)):
          return True

  
  return False

# Work together to prevent invalid input or filling in squares that are already taken, progress game
def inputCheck(x):
  try:
    x = int(x)
    if x >= 1 and x <= 9:
      if elem[x-1] != "X" or elem[x-1] != "O":
        return True  
    return False
  except:
    return False
def checkLoop(inp):
  while not inputCheck(inp):
    inp = input("Invalid response! Try again.")
  return int(inp)
def modifyMem(inp, player):
  
  verifiedIn = 0
  exit = False

  verifiedIn = checkLoop(inp)
  
  while not exit:
    for i in range(len(elem)):
      if (elem[i] == str(verifiedIn)) and (elem[i] != 'X' or elem != 'O') :
        if(player == 1):
          elem[i] = "X"
        else:
          elem[i] = "O"
        exit = True
    if not exit:
      inp = input("Already filled! Choose another square.")
      verifiedIn = checkLoop(inp)
  










# Overall AI Control
def aiControl2(step):
  data = elem.copy() 
  for i in data:
    if i == 'X' or i == 'O':
      data.remove(i)
  if step == 1:
    num = data[ra.randint(0,len(data))]
    modifyMem(num,2)
  if step == 2:
    None

# Scans the board for AI block move
def aiScan():
  match = None
  num = 0
  pos= []

  for i in range(len(elem)):
    if elem[i] == "X":
      num += 1
      pos.append(i+1)
  
  if num == 2:

    for i in range(len(winCombos)):
      if pos[0] in winCombos[i]:
        if pos[1] in winCombos[i]:
          match = winCombos[i]
  
    return match[2]

# Scans board for AI win move
def buildChain():
  None

  

  

















''' Actual Game '''

print("\nWelcome to TicTacToe, 2-player mode!")

# Game Loop
while True:

  print("\n**GAME STARTED! -- Every turn, enter the letter of space to fill**\n")
  printBoard()

  # Player Turns
  for i in range(10):
    
    if i % 2 == 0:
      p1 = input("Enter number of square to fill in: ")
      modifyMem(p1,1)
      printBoard()
      if(gameCheck1(elem)):
        winner = 1
        break
    
    else:
      p2 = input("Enter number of square to fill in: ")
      modifyMem(p2,2)
      printBoard()
      if(gameCheck2(elem)):
        winner = 2
        break

  # Result Outputter
  if winner == 1:
    print("\n" + victoryMsg + "1!")
  elif winner == 2:
    print("\n" + victoryMsg + "2!")
  else:
    print("\n" + tieMsg)
  
  elem =["1","2","3","4","5","6","7","8","9"]
  input("\nEnter any key to restart!")
  
