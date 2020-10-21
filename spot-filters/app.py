import cv2
import numpy as np

def average(img):
    b = img[:, :, 0]
    g = img[:, :, 1]
    r = img[:, :, 2]

    single = (b + g + r) / 3
    copy = img.copy()

    copy[:, :, 0] = single
    copy[:, :, 1] = single
    copy[:, :, 2] = single

    return np.sum(copy, axis=2)

def gray_scale_filter_cv(img1):
    gray_image = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    return gray_image