import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('image.jpeg')

plt.imshow(img)
plt.show()