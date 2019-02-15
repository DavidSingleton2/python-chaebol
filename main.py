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
  
  testTuple = namedtuple("pos", "type", "value")

  # Field types: 
  #     0 - Default Go Square, Jail, Goto Jail, Squares that aren't common
  #     1 - Asset
  #     2 - Utility
  #     3 - Chance
  #     4 - Community Chest
  

  square0 = testTuple(0,0,0)
  square1 = testTuple(1,0,0)
  square2 = testTuple(2,0,0)
  square3 = testTuple(3,0,0)
  square4 = testTuple(4,0,0)
  square5 = testTuple(5,0,0)
  square6 = testTuple(6,0,0)
  square7 = testTuple(7,0,0)
  square8 = testTuple(8,0,0)
  square9 = testTuple(9,0,0)
  square10 = testTuple(10,0,0)
  square11 = testTuple(11,0,0)
  square12 = testTuple(12,0,0)
  square13 = testTuple(13,0,0)
  square14 = testTuple(14,0,0)
  square15 = testTuple(15,0,0)
  square16 = testTuple(16,0,0)
  square17 = testTuple(17,0,0)
  square18 = testTuple(18,0,0)
  square19 = testTuple(19,0,0)
  square20 = testTuple(20,0,0)
  square21 = testTuple(21,0,0)
  square22 = testTuple(22,0,0)
  square23 = testTuple(23,0,0)
  square24 = testTuple(24,0,0)
  square25 = testTuple(25,0,0)
  square26 = testTuple(26,0,0)
  square27 = testTuple(27,0,0)
  square28 = testTuple(28,0,0)
  square29 = testTuple(29,0,0)
  square30 = testTuple(30,0,0)
  square31 = testTuple(31,0,0)
  square32 = testTuple(32,0,0)
  square33 = testTuple(33,0,0)
  square34 = testTuple(34,0,0)
  square35 = testTuple(35,0,0)
  square36 = testTuple(36,0,0)
  square37 = testTuple(37,0,0)
  square38 = testTuple(38,0,0)
  square39 = testTuple(39,0,0)
  

