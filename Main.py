import pygame
import sys
from constants import *

from World import World
from Renderer import Renderer
from Camera import Camera
from Input import Input

pygame.init()

running = True

renderer = Renderer()
camera = Camera()
world = World()
input = Input()

clock = pygame.time.Clock()

TicksPerSecond = 10
FixedDeltaTime = 1 / TicksPerSecond
accumulator = 0

while running:
	pygame.display.set_caption(f"sovernty silver 144p  tick:{world.ticks}  entityCount:{len(world.entities)}  fps:{clock.get_fps()}")

	deltaTime = clock.tick() / 1000
	
	input.updateInputs(world)
	input.MoveCamera(camera, cameraSpeed, deltaTime)

	accumulator += deltaTime

	while accumulator >= FixedDeltaTime:
		if not input.keys[pygame.K_LALT]: world.Update()
		accumulator -= FixedDeltaTime

	renderer.RenderFrame(world, camera)
	
	if input.QuitProgram:
		running = False


pygame.quit()
sys.exit()
