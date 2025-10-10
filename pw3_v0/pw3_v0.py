import cv2

WINDOW_NAME = 'Mosaic Effect'
IMAGE_PATH = 'kpi.jpg'

img = cv2.imread(IMAGE_PATH)

def apply_mosaic_effect(trackbar_value):
    scale = max(trackbar_value, 1) / 100.0
    h, w = img.shape[:2]
    small = cv2.resize(img, (0, 0), fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)
    mosaic = cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)
    cv2.imshow(WINDOW_NAME, mosaic)

cv2.namedWindow(WINDOW_NAME)
cv2.createTrackbar('Scale', WINDOW_NAME, 1, 100, apply_mosaic_effect)

cv2.waitKey()