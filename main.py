import random
import Player
from collections import namedtuple

# Main Thread of Execution. Begins Chaebol.
def main():
  print("The game has started! Welcome to Chaebol.")
  print("This game requires 2 players. Grab a buddy and get started")
  gameloop()

# Loop which runs through players turns.
def gameloop():
  # Turns variable, track whos turn it is, player 1 even, player 2 odd
  firstPlayer = True
  # Initialises two player classes
  playerOne = Player.Player()
  playerTwo = Player.Player()
  # placeholder
  board = initboard()
  gameEnd = False

  # Loop where game logic occurs
  while not(gameEnd):
    if firstPlayer:
      currentPlayer = playerOne
      opponent = playerTwo
      print("It is player one's turn.")
    else:
      currentPlayer = playerTwo
      opponent = playerOne
      print("It is player two's turn.")
    print("You have ${} in the bank.".format(currentPlayer.getBalance()))
    print("You currently own {} assets.".format(len(currentPlayer.getAssets())))
    roll = random.randint(1,6)
    position = currentPlayer.getPos() + roll
    if position > 39:
      position -= 40
    currentPlayer.setPos(position)

    # currentSpace = board[position]
    #if currentPlayer.owns(board[position]):
      #if opponent.owns(board[position]):
    # print("You have landed on {}.".format(board[position].name)))
    assetView = input("To view your assets, press 'v' and enter. To pass, press 'p' and enter.")

    if assetView is "v":
      print("You currently own...")
      # Add assets and their rent, etc.


    


    gameEnd = True # REMOVE LATER
    

#TODO RENT

def initboard():
  
  testTuple = namedtuple("testTuple", "name type value colour")

  # Board is referencing Standard US after Sept. 2008
  # https://monopoly.fandom.com/wiki/Monopoly_Board

  # Types in order of appearance
  # 0 Go
  # 1 Asset
  # 2 Community Chest
  # 3 Tax
  # 4 Railroad
  # 5 Chance
  # 6 Jail
  # 7 Utility
  # 8 Free Parking
  # 9 Go To Jail

  # TODO: Figure out where to store rent bonus (according to coloured cards)
  # and should money owed be under value as well?

  board = [
  # Bottom Right Corner
  testTuple("test0",0),

  # Bottom Row
  testTuple("test1",1,60),
  testTuple("test2",2,0),
  testTuple("test3",1,60),
  testTuple("test4",3,0),
  testTuple("test5",4,0),
  testTuple("test6",1,100),
  testTuple("test7",5,0),
  testTuple("test8",1,100),
  testTuple("test9",1,120),

  # Bottom Left Corner
  testTuple(10,"test10",6,0),

  # Left Column
  testTuple("test11",1,140),
  testTuple("test12",7,0),
  testTuple("test13",1,140),
  testTuple("test14",1,160),
  testTuple("test15",4,0),
  testTuple("test16",1,180),
  testTuple("test17",2,0),
  testTuple("test18",1,180),
  testTuple("test19",1,200),
  
  # Top Left Corner
  testTuple("test20",8,0),

  # Top Row
  testTuple("test21",1,220),
  testTuple("test22",5,0),
  testTuple("test23",1,220),
  testTuple("test24",1,240),
  testTuple("test25",4,0),
  testTuple("test26",1,260),
  testTuple("test27",1,260),
  testTuple("test28",7,0),
  testTuple("test29",1,280),

  # Top Right Corner
  testTuple("test30",9,0),

  # Right Column
  testTuple("test31",1,300),
  testTuple("test32",1,300),
  testTuple("test33",2,0),
  testTuple("test34",1,320),
  testTuple("test35",4,0),
  testTuple("test36",5,0),
  testTuple("test37",1,350),
  testTuple("test38",3,0),
  testTuple("test39",1,400)
  ]
  return board

main()