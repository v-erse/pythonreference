from scipy.misc import imread, imsave, imresize

img = imread("seinfeld.jpg")
print(img.shape)  # returns (490,980,3)

# We can tint the image by applying a transformation to its matrix, i.e.
# multiplying it by something else.
# We can multiply it by an array of shape (3,), and numpy broadcasting will
# handle it for us.
# We end up multiplying all of the red channel values by 1, leaving them
# unchanged, but we do alter the green and blue channel values
img_tinted = img * [1, 0.5, 0.5]

# We can also use scipy to resize the image:
# divide size by two -> (245.0, 490.0, 1.5)
halfsize = tuple(round(x/2) for x in img.shape)
img_tinted = imresize(img_tinted, halfsize)

# We can then save this image back
imsave('seinfeld_tinted.jpg', img_tinted)
