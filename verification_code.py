import cv2
import pytesseract

def verification(vc_img):
    img = cv2.imread(vc_img, 0)
    _, th1 = cv2.threshold(img, 40, 255, cv2.THRESH_BINARY)
    vc_string = pytesseract.image_to_string(th1,lang='eng', config="--psm 6 --tessdata-dir tessdata"
                                                                       "--oem 3 -c tessedit_char_whitelist=0123456789"))
    return(vc_string)