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
  playerOne = Player()
  playerTwo = Player()
  # placeholder
  board = []
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
    print("You currently own {} assets.".format(currentPlayer.getAssets().length()))
    roll = random.randint(1,6)
    position = currentPlayer.getPosition + roll
    if position > 39:
      position -= 40
    currentPlayer.setPos(position)
    # currentSpace = board[position]
    #if currentPlayer.owns(board[position]):
      #if opponent.owns(board[position]):
    print("You have landed on {}.".format("placeholder"))
    print("To view your assets, press 'v' and enter. To pass, press 'p' and enter.")
    
    
def testboard():
  
  testTuple = namedtuple("position", "type", "value")

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

  # Although multiple squares serve no purpose/a unique one, it is easier
  # to just define a "type" for each type of square to allow clear and
  # coherent code in the main game loop. 

  
  # TODO: Figure out where to store rent bonus (according to coloured cards)
  # and should money owed be under value as well?

  # Bottom Right Corner
  square0 = testTuple(0,0,0)

  # Bottom Row
  square1 = testTuple(1,1,60)
  square2 = testTuple(2,2,0)
  square3 = testTuple(3,1,60)
  square4 = testTuple(4,3,0)
  square5 = testTuple(5,4,0)
  square6 = testTuple(6,1,100)
  square7 = testTuple(7,5,0)
  square8 = testTuple(8,1,100)
  square9 = testTuple(9,1,120)

  # Bottom Left Corner
  square10 = testTuple(10,6,0)

  # Left Column
  square11 = testTuple(11,1,140)
  square12 = testTuple(12,7,0)
  square13 = testTuple(13,1,140)
  square14 = testTuple(14,1,160)
  square15 = testTuple(15,4,0)
  square16 = testTuple(16,1,180)
  square17 = testTuple(17,2,0)
  square18 = testTuple(18,1,180)
  square19 = testTuple(19,1,200)
  
  # Top Left Corner
  square20 = testTuple(20,8,0)

  # Top Row
  square21 = testTuple(21,1,220)
  square22 = testTuple(22,5,0)
  square23 = testTuple(23,1,220)
  square24 = testTuple(24,1,240)
  square25 = testTuple(25,4,0)
  square26 = testTuple(26,1,260)
  square27 = testTuple(27,1,260)
  square28 = testTuple(28,7,0)
  square29 = testTuple(29,1,280)

  # Top Right Corner
  square30 = testTuple(30,9,0)

  # Right Column
  square31 = testTuple(31,1,300)
  square32 = testTuple(32,1,300)
  square33 = testTuple(33,2,0)
  square34 = testTuple(34,1,320)
  square35 = testTuple(35,4,0)
  square36 = testTuple(36,5,0)
  square37 = testTuple(37,1,350)
  square38 = testTuple(38,3,0)
  square39 = testTuple(39,1,400)
  

