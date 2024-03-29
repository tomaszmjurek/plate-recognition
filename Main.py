# Main.py

import cv2
import numpy as np
import os

import DetectChars
import DetectPlates
import PossiblePlate
import Ocr
import sys

# module level variables
SCALAR_BLACK = (0.0, 0.0, 0.0)
SCALAR_WHITE = (255.0, 255.0, 255.0)
SCALAR_YELLOW = (0.0, 255.0, 255.0)
SCALAR_GREEN = (0.0, 255.0, 0.0)
SCALAR_RED = (0.0, 0.0, 255.0)

def main():

    blnKNNLoadingSuccessful = DetectChars.loadKNNData()         # KNN training

    if blnKNNLoadingSuccessful == False:
        print("\nerror: KNN loading was not successful\n")
        return

    # 1. Loading image
    imgOriginalScene  = cv2.imread(sys.argv[1])               # choose image to process

    if imgOriginalScene is None:
        print("\nerror: image not read from file \n\n")
        os.system("pause")
        return

    # 2. Detecting possible plates
    listOfPossiblePlates = DetectPlates.detectPlatesInScene(imgOriginalScene)           # detect plates

    cv2.imshow("imgOriginalScene", imgOriginalScene)        # show original

    if len(listOfPossiblePlates) == 0:                          # if no plates were found
        print("\nno license plates were detected\n")
    else:

        # 3. Choosing most possible plate
        # if found possible plates takes the one with max number of chars
        listOfPossiblePlates.sort(key = lambda possiblePlate: len(possiblePlate.strChars), reverse=True)
        licPlate = listOfPossiblePlates[0]

        cv2.imshow("imgPlate", licPlate.imgPlate)           # show and save crop of plate
        cv2.imwrite("ImgPlate.png", licPlate.imgPlate)
	
	# 4. Text recognition
    #	Ocr.ocr(licPlate.imgPlate)	# text detection

        drawRedRectangleAroundPlate(imgOriginalScene, licPlate)             # draw red rectangle around plate
        cv2.imshow("imgPlateDetected", imgOriginalScene)        # show original with rectangle
        cv2.imwrite("imgOriginalScene.png", imgOriginalScene)           # write image out to file

    cv2.waitKey(0)					# hold windows open until user presses a key
    return


def drawRedRectangleAroundPlate(imgOriginalScene, licPlate):

    p2fRectPoints = cv2.boxPoints(licPlate.rrLocationOfPlateInScene)            # get 4 vertices of rotated rect
    cv2.line(imgOriginalScene, tuple(p2fRectPoints[0]), tuple(p2fRectPoints[1]), SCALAR_RED, 2)         # draw 4 red lines
    cv2.line(imgOriginalScene, tuple(p2fRectPoints[1]), tuple(p2fRectPoints[2]), SCALAR_RED, 2)
    cv2.line(imgOriginalScene, tuple(p2fRectPoints[2]), tuple(p2fRectPoints[3]), SCALAR_RED, 2)
    cv2.line(imgOriginalScene, tuple(p2fRectPoints[3]), tuple(p2fRectPoints[0]), SCALAR_RED, 2)


if __name__ == "__main__":
    main()


















