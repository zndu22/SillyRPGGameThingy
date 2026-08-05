import math
from opensimplex import OpenSimplex
from PIL import Image
import random

# 1. Initialization and Constants
WIDTH, HEIGHT = 100, 100
SCALE = 0.05  # Controls the zoom level of the noise features
OCTAVES = 7  # Number of noise layers combined for detail
LACUNARITY = 2.0  # Frequency multiplier per octave
PERSISTENCE = 0.5  # Amplitude multiplier per octave

# Create image buffer and initialize OpenSimplex
img = Image.new("RGB", (WIDTH, HEIGHT))
heightmap = Image.new("RGB", (WIDTH, HEIGHT))
pixels = img.load()
heightmapPixels = heightmap.load()

gen = OpenSimplex(seed=random.randint(0, 1000))

# Center points for distance calculations
cx, cy = WIDTH / 2, HEIGHT / 2
max_dist = math.sqrt(cx**2 + cy**2)

# 2. Main Generation Loop
for y in range(HEIGHT):
    for x in range(WIDTH):

        # A. Calculate Fractal OpenSimplex Noise (FBm)
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

        # Normalize noise strictly to a [0.0, 1.0] range
        noise_val = (noise_val / max_possible_noise + 1.0) / 2.0
        

        # B. Apply Radial Falloff Mask (forces edges to ocean)
        dx = x - cx
        dy = y - cy
        dist = math.sqrt(dx**2 + dy**2) / max_dist

        # Island equation: pushes center up, drops edges down
        elevation = (noise_val + (1.0 - dist * 1.2)) / 2.0
        elevation = max(0.0, min(1.0, elevation))  # Clamp between 0 and 1
        
        height = int(elevation*255)
        heightmapPixels[x, y] = (height, height, height)

        # C. Map Elevation to Biome Colors
        if elevation < 0.46:
            color = (0, 0, 255)  # Shallow Water
        elif elevation < 0.65:
            color = (0, 255, 0)  # Grassland
        else:
            color = (127, 127, 127)  # Snow Peaks

        pixels[x, y] = color
        print(f"position: {x}, {y}, is generated")

# 3. Save Output Image
img.show()
img.save("map.png")
heightmap.save("heightmap.png")
print("Continent map generated successfully as 'continent.png'!")
