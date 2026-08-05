import pygame

windowHeight = 500
windowWidth = 800

tileWidth = 64
tileHeight = 64

cameraSpeed = 500

grassColor = (0, 255, 0)
waterColor = (0, 0, 255)
mountianColor = (127, 127,127)

assets = {
	"GrassTexture" : pygame.image.load("assets/grass.png"),
	"WaterTexture" : pygame.image.load("assets/water.png"),
	"MountianTexture" : pygame.image.load("assets/mountian.png"),
	"guy" : pygame.image.load("assets/guy.png"),
	"evilGuy" : pygame.image.load("assets/badGuy.png")
}

def convertTextures():
	global assets
	for i, (k, v) in enumerate(assets.items()):
		v = v.convert()

def addTuples(a, b):
	return tuple(x + y for x, y in zip(a, b))