import cv2
import numpy as np
import os

# https://www.geeksforgeeks.org/python-opencv-cv2-imread-method/

# Define the dimensions of checkerboard
CHECKERBOARD = (7, 7)

# stop the iteration when specified
# accuracy, epsilon, is reached or
# specified number of iterations are completed.
criteria = (cv2.TERM_CRITERIA_EPS +
            cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Vector for 3D points
threedpoints = []

# Vector for 2D points
twodpoints = []

#  3D points real world coordinates
objectp3d = np.zeros((1, CHECKERBOARD[0]
                      * CHECKERBOARD[1],
                      3), np.float32)
objectp3d[0, :, :2] = np.mgrid[0:CHECKERBOARD[0],
                      0:CHECKERBOARD[1]].T.reshape(-1, 2)
prev_img_shape = None

images = [
    'pict/board1.jpg', 'pict/board2.jpg', 'pict/board3.jpg'
]

for filename in images:
    image = cv2.imread(filename)
    grayColor = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ret, corners = cv2.findChessboardCorners(grayColor, CHECKERBOARD,
                                             cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_FAST_CHECK + cv2.CALIB_CB_NORMALIZE_IMAGE)

    # If desired number of corners can be detected then,
    # refine the pixel coordinates and display
    # them on the images of checker board
    if ret == True:
        threedpoints.append(objectp3d)

        # refining pixel coordinates
        # for given 2d points.
        corners2 = cv2.cornerSubPix(grayColor, corners, (11, 11), (-1, -1), criteria)
        twodpoints.append(corners2)

        # Draw and display the corners
        image = cv2.drawChessboardCorners(image, CHECKERBOARD, corners2, ret)
    cv2.imshow('Image', image)
    cv2.waitKey(0)
cv2.destroyAllWindows()

# Perform camera calibration
h, w = image.shape[:2]
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(threedpoints, twodpoints, grayColor.shape[::-1], None, None)

# Displaying required output
print("Camera matrix : ")
print(mtx)

print("distortion coefficient : ")
print(dist)

print("Rotation Vectors :")
print(rvecs)

print("Translation Vectors :")
print(tvecs)