from PIL import Image
import pygame
from constants import *
#import opensimplex

class WorldMap():

    def __init__(self):
        self.img = Image.open("assets/map.png")
        self.pixels = self.img.load()
        
        self.columns = self.getMapSize()[0]
        self.rows = self.getMapSize()[1]

        self.tilemap = pygame.Surface((self.columns * tileWidth, self.rows * tileHeight))

    def getMapSize(self):
        return self.img.size

    def getPixel(self, x, y):
        if not self.isInBounds(x, y):
            return (0, 0, 0)
        return self.pixels[x, y]

    def setPixel(self, x, y, r, g, b):
        self.pixels.set_pixel(x, y, (r, g, b))

    def isInBounds(self, x, y):
        return 0 <= x < self.columns and 0 <= y < self.rows

    def isOutOfBounds(self, pos):
        x, y = pos
        return not self.isInBounds(x, y)
    
    def generateTilemap(self):
        for x in range(self.columns):
            for y in range(self.rows):
                currentPixel = self.getPixel(x,y)
                if currentPixel == grassColor:
                    self.tilemap.blit(assets['GrassTexture'], (x * tileWidth, y * tileHeight))
                if currentPixel == waterColor:
                    self.tilemap.blit(assets['WaterTexture'], (x * tileWidth, y * tileHeight))
                if currentPixel == mountianColor:
                    self.tilemap.blit(assets['MountianTexture'], (x * tileWidth, y * tileHeight))