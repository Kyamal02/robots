import cv2
import numpy as np
from random import random


def add_salt_pepper_noise(img, probability):
    output = np.zeros(img.shape, np.uint8)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            rnd = random()
            # divide the salt and pepper noise into white and black colors
            prob = probability / 2.0
            inverse_prob = 1 - prob
            #    | -- | real image | -- |
            # white noise        black noise
            output[i, j] = 255 if rnd < prob else 0 if rnd > inverse_prob else img[i, j]
    return output


### BLURRING ###
def median_blur(img, kernel_size):
    return cv2.medianBlur(img, kernel_size)


def gaussian_blur(img, kernel_size):
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), sigmaX=0, sigmaY=0)


def bilateral_filter(img, kernel_size, sigma_color, sigma_space):
    return cv2.bilateralFilter(img, kernel_size, sigma_color, sigma_space)


if __name__ == '__main__':
    # show salted image
    img = cv2.imread('pict.jpg')
    noised = add_salt_pepper_noise(img, 0.5)
    cv2.imshow('Original | Noised', np.hstack((img, noised)))
    cv2.imshow('Median | Gaussian | Bilateral',
               np.concatenate((
                   median_blur(noised, 5),
                   gaussian_blur(noised, 5),
                   bilateral_filter(noised, 9, 75, 75)
               ), axis=1))
    cv2.waitKey(0)
    cv2.destroyAllWindows()