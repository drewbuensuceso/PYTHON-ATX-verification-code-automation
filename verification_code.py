import cv2
import pytesseract
import re

def verification(vc_img):
    img = cv2.imread(vc_img, 0)
    _, th1 = cv2.threshold(img, 30, 255, cv2.THRESH_BINARY)
    th2 = cv2.medianBlur(th1, 5)
    vc_string = pytesseract.image_to_string(th1, lang='lang', config="--oem 1 --psm 6 --tessdata-dir tessdata")

    return(re.sub(r"\s+", "", vc_string, flags=re.UNICODE))