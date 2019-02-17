class Player:
  def __init__(self):
    self._balance = 1500
    self._position = 0
    self._assets = [0,1,2,3] # Array of position of assets palyer will own TEST VALUEs
    self._id = 999 # Default ID set to 999
  
  def buyAsset(self, asset):
    self._balance -= asset.price
    self._assets.append(asset.name)

  def getBalance(self):
    return self._balance

  def setBalance(self, balance):
    self._balance = balance

  def getPos(self):
    return self._position
  
  def setPos(self, pos):
    self._position = pos

  def owns(self, asset):
    return asset.name in self._assets

  def getAssets(self):
    return self._assets

  def setId(self, num):
    self._id = num
  
  def getId(self):
    return self._id