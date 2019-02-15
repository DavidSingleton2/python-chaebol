class Player:
  def __init__(self):
    self._balance = 1500
    self._position = 0
    self._assets = []
  
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