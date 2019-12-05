import cv2
import imutils
import numpy as np
import pytesseract
import sys
from PIL import Image


# OCR
config = '-l eng --oem 1 --psm 3'
def ocr (croppedImage):
    text = pytesseract.image_to_string(croppedImage, config=config)

    validChars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    cleanText = []

    for char in text:
        if char in validChars:
            cleanText.append(char)

    plate = ''.join(cleanText)

    print(plate)

    cv2.imshow('croppedImage',croppedImage)
