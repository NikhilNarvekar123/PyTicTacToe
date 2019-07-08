''' 
Interactive tic-tac-toe for two players, with readable code for learners
POTENTIAL BUGS: If input is not a number, game will crash :-(
    
--Created By Young Bytes--

'''

# Input Variables
p1 = ""
p2 = ""
winner = -1
victoryMsg = "WINNER WINNER CHICKEN DINNER! Congrats Player "
tieMsg = "Oops--Tie Game :-("


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

def modifyMem(inp, player):
  
  verifiedIn = 0


  while not inputCheck(inp):
    inp = input("Invalid response! Try again.")
  verifiedIn = int(inp)
  
  for i in range(len(elem)):
    if elem[i] == str(verifiedIn):
      if(player == 1):
        elem[i] = "X"
      else:
        elem[i] = "O"
    

# Check board every round
def gameCheck1():
  
  num = 0
  pos= []

  for i in range(len(elem)):
    if(elem[i] == "X"):
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
def gameCheck2():
  
  num = 0
  pos= []

  for i in range(len(elem)):
    if(elem[i] == "O"):
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

# TODO: Function to check whether input is valid each turn
# Current filters out wrong format input, but still cannot stop players from filling filled up spaces
def inputCheck(x):
  try:
    x = int(x)
    if x >= 1 and x <= 9:
      if elem[x-1] != "X" or elem[x-1] != "O":
        return True  
    return False
  except:
    return False




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
      if(gameCheck1()):
        winner = 1
        break
    
    else:
      p2 = input("Enter number of square to fill in: ")
      modifyMem(p2,2)
      printBoard()
      if(gameCheck2()):
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
  
