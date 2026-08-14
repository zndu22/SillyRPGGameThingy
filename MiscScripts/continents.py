import math
from opensimplex import OpenSimplex
from PIL import Image
import random

# 1. Initialization and Constants	
WIDTH, HEIGHT = 200, 200
SCALE = 0.05
OCTAVES = 7 
LACUNARITY = 2.0 # Frequency multiplier per octave
PERSISTENCE = 0.5 # Amplitude multiplier per octave

img = Image.new("RGB", (WIDTH, HEIGHT))
heightmap = Image.new("RGB", (WIDTH, HEIGHT))
pixels = img.load()
heightmapPixels = heightmap.load()

SEED = random.randint(0, 1000)
gen = OpenSimplex(seed=SEED)
print(f"Seed is: {SEED}")

# Center points for distance calculations
cx, cy = WIDTH / 2, HEIGHT / 2
maxDist = math.sqrt(cx**2 + cy**2)

# for every tile on the map:
for y in range(HEIGHT):
	for x in range(WIDTH):

		# first, Get the Base noise value for the tile.
		noise_val = 0
		amplitude = 1.0
		frequency = SCALE
		max_possible_noise = 0

		for _ in range(OCTAVES):
			# OpenSimplex 2D outputs between -1.0 and 1.0
			raw_noise = gen.noise2(x * frequency, y * frequency)
			noise_val += raw_noise * amplitude
			max_possible_noise += amplitude
			amplitude *= PERSISTENCE
			frequency *= LACUNARITY

		# Clamp noise value between 0 and 1
		noise_val = (noise_val / max_possible_noise + 1.0) / 2.0
		

		# Then, for the continent effect, apply the radial falloff map.
		dx = x - cx
		dy = y - cy
		dist = math.sqrt(dx**2 + dy**2) / maxDist

		elevation = (noise_val + (1.0 - dist * 1.2)) / 2.0
		elevation = max(0.0, min(1.0, elevation))  # Clamp between 0 and 1 again
		
		height = int(elevation*255)
		heightmapPixels[x, y] = (height, height, height)

		elevation = int(elevation * 255) # quantize elevation to 0-255 scale, 'cause I want to
		
		# And finally, color each tile appropriately
		if elevation < 110:
			color = (0, 0, 255)  # Water
		elif elevation < 180:
			color = (0, 255, 0)  # Grass
		else:
			color = (127, 127, 127)  # Mountians

		pixels[x, y] = color
		print(f"position: {x}, {y}, is generated")

# 3. Save Output Image
img.show()
img.save("map.png")
heightmap.save("heightmap.png")
print("Continent map generated successfully as 'continent.png'!")
