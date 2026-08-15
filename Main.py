import pygame
import sys
from constants import *

from World import World
from Renderer import Renderer
from Camera import Camera
from Input import Input
from CharacterStats import CharacterStats

pygame.init()

running = True

camera = Camera()
world = World()
inputs = Input(world, camera)
renderer = Renderer(inputs)

clock = pygame.time.Clock()

TicksPerSecond = 10
FixedDeltaTime = 1 / TicksPerSecond
accumulator = 0

world.addEntity(assets["house"], (1, 1))
# There will be at least one other type of entity.
# buildings, which will be enterable by heroes and provide services, such as stores, guilds, or taverns.
# And props, which will be decoration around the world. Either passable, like a bridge, or not, like a wall or rock.

# Being in the same tile as a building counts as being 'in' that building. I'll have it just draw the building in that case.

# I'll add UI eventually, probably pygame_gui, that will show each entity in the tile you're hovering over, and all their information.

while running:
	pygame.display.set_caption(f"sovernty silver 144p  tick:{world.ticks}  entityCount:{len(world.entities)}  fps:{clock.get_fps()}")

	deltaTime = clock.tick() / 1000
	
	inputs.updateInputs()
	inputs.MoveCamera(cameraSpeed, deltaTime)

	accumulator += deltaTime

	while accumulator >= FixedDeltaTime:
		if not inputs.keys[pygame.K_LALT]: world.Update()
		accumulator -= FixedDeltaTime

	renderer.RenderFrame(world, camera)
	
	if inputs.QuitProgram:
		running = False


pygame.quit()
sys.exit()
