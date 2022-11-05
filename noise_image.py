import numpy as np
from PIL import Image
from simplexnoise.noise import SimplexNoise, normalize
import random

size = 250
noise_scale = 700.0 # Turns up the contrast 
seed = 2345
random.seed(a = seed)


sn = SimplexNoise(num_octaves=7, persistence=0.1, noise_scale=noise_scale)
data = []

print("1")

for i in range(size):
    data.append([])
    for j in range(size):
        noise = normalize(sn.noise(i, j))
        data[i].append(noise * 255.0)

print("2")

# Cast to numpy array so we can save 
data = np.array(data).astype(np.uint8)
img = Image.fromarray(data, mode='L')
img.save('./noise_example5.png')
print("done")