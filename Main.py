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

renderer = Renderer()
camera = Camera()
world = World()
inputs = Input(world, camera)

clock = pygame.time.Clock()

TicksPerSecond = 10
FixedDeltaTime = 1 / TicksPerSecond
accumulator = 0

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
