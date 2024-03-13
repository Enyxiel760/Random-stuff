import numpy as np
from PIL import Image, ImageShow

width = 8000
height = 6000

#define the complex plane to a granularity as specified in the variables above
x = np.linspace(-2, 1, num=width).reshape(1, width)
y = np.linspace(-1, 1, num=height).reshape(height, 1)
c = np.tile(x, (height, 1)) + 1j * np.tile(y, (1, width))

#force smaller complex type to reduce ram usage of such huge arrays
c = c.astype('complex64')

#create empty array to represent each point in space
z = np.zeros((height, width), dtype=complex)

#create full array of 1's to represent each 'pixel'.
image = np.full((height, width), True, dtype=bool)

#iterate 100 times to be sure a value either escapes the bounds or doesnt
for i in range(100):
    z[image] = z[image] * z[image] + c[image]
    #if value becomes more than 2, we know it escapes the bounds and isnt part of the set so Set that 'pixel' to false. 
    #since we use image as the index, the false value prevents us performing calculations on values we know escape.
    image[np.abs(z) > 2] = False

#turn our array into an image where 1's will represent points in the mandlebrot set
mandelbrot = Image.fromarray(image)

ImageShow.show(mandelbrot)
