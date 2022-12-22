import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('pict/board_with_coin.jpg')
canny = cv2.Canny(img, 100, 200)

kernel = np.ones((3,3), 'uint8')
dilate = cv2.dilate(canny, kernel=kernel, iterations=1)
erosion = cv2.erode(dilate, kernel=kernel, iterations=1)
plt.subplot(221), plt.imshow(img, cmap = 'gray')
plt.subplot(222), plt.imshow(canny, cmap = 'gray')
plt.subplot(223), plt.imshow(dilate, cmap = 'gray')
plt.subplot(224), plt.imshow(erosion, cmap = 'gray')
plt.show()