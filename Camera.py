
class Camera():

	def __init__(self):
		self.positionX = 0
		self.positionY = 0
	
	def moveCamera(self, dp):
		self.positionX += dp[0]
		self.positionY += dp[1]
	
	def getPosition(self):
		return (self.positionX, self.positionY)
	
	def setPosition(self, position):
		self.positionX = position[0]
		self.positionY = position[1]