__author__ = 'charles'

import argparse
import cv2



ap = argparse.ArgumentParser()
ap.add_argument("-1","--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

