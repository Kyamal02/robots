import cv2
import numpy as np

point = -1, -1

def convert(bgr):
    b, g, r = bgr
    print('RGB = ', [r, g, b])
    print('HSV = ', cv2.cvtColor(np.uint8([[bgr]]), cv2.COLOR_BGR2HSV)[0][0])
    print('LAB = ', cv2.cvtColor(np.uint8([[bgr]]), cv2.COLOR_BGR2LAB)[0][0])
    print('YCrCb = ', cv2.cvtColor(np.uint8([[bgr]]), cv2.COLOR_BGR2YCrCb)[0][0])

def mouse_callback(event, x, y, flags, params):
    global point
    if event == cv2.EVENT_LBUTTONDOWN:
       point = x, y

while True:
    # read the color spectrum image
    img = cv2.imread('circle.png')
    # get the color at the point
    color = img[point[1], point[0]]
    # draw a circle at the point
    if point != (-1, -1):
        start_point = point[0] - 4, point[1] - 4
        end_point = point[0] + 4, point[1] + 4
        cv2.rectangle(img, start_point, end_point, (0,0,0), 2)
    # show the image
    cv2.imshow('Color picker', img)
    # set the mouse callback
    cv2.setMouseCallback('Color picker', mouse_callback)
    k = cv2.waitKey(1)
    if k & 0xFF == 27:
        break
        # Wait for 'p' entered
    if k == ord('f'):
        convert(color)
        break
cv2.destroyAllWindows()