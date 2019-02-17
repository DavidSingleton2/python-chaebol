import random
from Player import Player
from collections import namedtuple


## REFER TO assetinfo()
asset = namedtuple("asset", "owner pos colour buildings rents")


# Main Thread of Execution. Begins Chaebol.
def main():
  print("The game has started! Welcome to Chaebol.")
  print("This game requires 2-8 players. Grab some buddies and get started")
  gameloop()

# Loop which runs through players turns.
def gameloop():
  # Turns variable stores current turn
  turns = 0
  board = initboard()
  assets = assetinfo()
  gameEnd = False

  playerInput = int(input("How many players are there? (Enter a number): "))
  while (int(playerInput) > 8) and (int(playerInput) < 2):
    print("Incorrect entry. Please try again.")
    playerInput = input("How many players are there? (Enter a number): ")
  players = [Player() for i in range(int(playerInput)) ]
  playerId = 1
  for player in players:
    player.setId(playerId)
    playerId += 1
  
  # Loop where game logic occurs
  while not(gameEnd):




    #TODO TEMP TESTING
    #currentPlayer = players[turns % len(players)]
    currentPlayer = players[1]





    print("It is Player {}'s turn".format(currentPlayer.getId()))
    print("You have ${} in the bank.".format(currentPlayer.getBalance()))
    print("You currently own {} assets.".format(len(currentPlayer.getAssets())))
    firstRoll = random.randint(1,6)
    secondRoll = random.randint(1,6)
    moves = firstRoll+secondRoll
    if firstRoll == secondRoll:
      print("Doubles! Move " + str(moves) + " spaces and gain another turn.")
      turns -= 1
    position = currentPlayer.getPos() + moves
    if position > 39:
      position -= 40
    
    currentPlayer.setPos(position)
    position = 37

    print("You have landed on {}.".format(board[position].name))
    # assetView = input("To view your assets, press 'v' and enter. To pass, press 'p' and enter.")

    # if assetView is "v":
    #   print("You currently own...")
    
    if board[position].type == 1:
      
      # IMPORTANT ###########
      property = locateasset(assets,position)

      if ownasset(currentPlayer.getId(),assets,position):
          print("You own this asset already")
          

          #WORKING
          if property.buildings < 5:
            upgradeyn = input("Would you like to upgrade this lot to a house/hotel y/n")

            if upgradeyn == 'y':
              currentPlayer.setBalance(currentPlayer.getBalance() - getupgradecost(property.colour))
              print("Your new balance is",currentPlayer.getBalance())

          else:
            print('Building maxed out')
          

      elif property.owner != 0: # Pay rent
        

        #TODO
        #TODO
        #TODO
        #TODO
        # FIX INDEXING OF players[] TO ALIGN WITH ID. ARRAY INDEXED FROM 0 WHILE PLAYER IDS START AT 1. ALSO FINISH THIS RENT ELIF.

        # Landlord
        players[property.owner-1].setBalance(players[property.owner-1].getBalance() + property.rents[property.buildings])

        #Tenant
        currentPlayer.setBalance(currentPlayer.getBalance() - property.rents[property.buildings])

        print("Your new balance is",currentPlayer.getBalance())
        print("Landlord new balance is",players[property.owner-1].getBalance())


      else:
        print("No one owns this asset.")
        print("It is avaliable for ${cost}. You currently have ${balance} in your account.".format(
          cost=board[position].value, balance=currentPlayer.getBalance()
        ))
        purchaseInput = input("Would you like to purchase it? (y/n): ")
        while purchaseInput != 'y' and purchaseInput != 'n':
          print("Invalid input. Please try again")
          purchaseInput = input("No one owns this asset. Would you like to purchase it? (y/n): ")
        if purchaseInput == 'y':
          if currentPlayer.getBalance() > board[position].value:
            print("temp")


    turns +=1
    gameEnd = True # REMOVE LATER
      

def ownasset(id,assets,playerPos):
  boole = False
  for i in range(len(assets)):
    if assets[i].owner == id:
      boole = True
  
  return boole

def locateasset(assets,position):
  for property in assets:
    if property.pos == position:
      return property
      break

def getupgradecost(colcode):
  upgradeCosts = {
    0:50,   # Brown
    1:50,   # L. Blue
    2:100,  # Pink
    3:100,  # Orange
    4:150,  # Red
    5:150,  # Yellow
    6:200,  # Green
    7:200   # Blue
  }
  return upgradeCosts.get(colcode)

  


#TODO RENT
def assetinfo ():
  # Owner is ID of player who owns the lotm 0 by default. Colours are numbered 0-7 brown to blue
  # buildings list how many buildings (houses 1-4, hotel 5) there are. 
  # The rents are how much rent cost
  array = [
    asset(1,  1,  0,  0,  [ 2,  10,  30,  90,   160,  250  ]),
    asset(0,  3,  0,  0,  [ 4,  20,  60,  180,  320,  450  ]),
    asset(0,  6,  1,  0,  [ 6,  30,  90,  270,  400,  550  ]),
    asset(0,  8,  1,  0,  [ 6,  30,  90,  270,  400,  550  ]),
    asset(0,  9,  1,  0,  [ 8,  40,  100, 300,  450,  600  ]),
    asset(0,  11, 2,  0,  [ 10, 50,  150, 450,  625,  750  ]),
    asset(0,  13, 2,  0,  [ 10, 50,  150, 450,  625,  750  ]),
    asset(0,  14, 2,  0,  [ 12, 60,  180, 500,  700,  900  ]),
    asset(0,  16, 3,  0,  [ 14, 70,  200, 550,  750,  950  ]),
    asset(0,  18, 3,  0,  [ 14, 70,  200, 550,  750,  950  ]),
    asset(0,  19, 3,  0,  [ 16, 80,  220, 600,  800,  1000 ]),
    asset(0,  21, 4,  0,  [ 18, 90,  250, 700,  875,  1050 ]),
    asset(0,  23, 4,  0,  [ 18, 90,  250, 700,  875,  1050 ]),
    asset(0,  24, 4,  0,  [ 20, 100, 300, 750,  925,  1100 ]),
    asset(0,  26, 5,  0,  [ 22, 110, 330, 800,  975,  1150 ]),
    asset(0,  27, 5,  0,  [ 22, 110, 330, 800,  975,  1150 ]),
    asset(0,  29, 5,  0,  [ 24, 120, 360, 850,  1025, 1200 ]),
    asset(0,  31, 6,  0,  [ 26, 130, 390, 900,  1100, 1275 ]),
    asset(0,  32, 6,  0,  [ 26, 130, 390, 900,  1100, 1275 ]),
    asset(0,  34, 6,  0,  [ 28, 150, 450, 1000, 1200, 1400 ]),
    asset(1,  37, 7,  0,  [ 35, 175, 500, 1100, 1300, 1500 ]),
    asset(0,  39, 7,  0,  [ 50, 200, 600, 1400, 1700, 2000 ])
  ]

  return array


def initboard():
  
  testTuple = namedtuple("testTuple", "name type value")

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
  testTuple("test0",0,0),

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
  testTuple("test10",6,0),

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