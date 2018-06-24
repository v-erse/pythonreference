import numpy as np
from scipy.misc import imread, imresize
import matplotlib.pyplot as plt

img = imread('../Scipy/seinfeld.jpg')
# tint
img_tinted = img * [1, 0.5, 0.5]
# resize
halfsize = tuple(round(x/2) for x in img.shape)
img_tinted = imresize(img_tinted, halfsize)

# plot first
plt.subplot(2, 1, 1)
plt.imshow(img)

# plot second
plt.subplot(2, 1, 2)
# imshow needs values to be of the uint8 type, so we must cast img_tinted to
# this before we pass it in, using np
plt.imshow(np.uint8(img_tinted))
plt.show()
