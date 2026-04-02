import cv2
import time
import numpy as np
import os
import handtrackingmodule as htm

wCam = 1280
hCam = 720

brushThickness = 15
eraserThickness = 50

detector = htm.handDetector(detectionCon=0.85)

folderPath = "Header - virtual painter"
myList = os.listdir(folderPath)
print(myList)
overlayList = []

for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)
print(len(overlayList))
header = overlayList[0]
drawcColor = 0

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

imgCanvas =np.zeros((720, 1280, 3), np.uint8)

while True:
    #1.Import Image 
    success, img = cap.read()

    #2.Find Hand Landmarks
    img = cv2.flip(img, 1)
    img = detector.findHands(img)   
    lmList = detector.findPosition(img)
    if len(lmList) != 0:
        #print(lmList)   
        
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
    
    #3.Check which fingers are up
        fingers = detector.fingersUp()
        #print(fingers)

    #4.If Selection Mode - Two fingers are up - Selection of the tool
        if fingers[1] and fingers[2]:
            xp, yp = 0, 0
            print("Selection Mode")
            
            if y1 < 125:
                if 150 < x1 < 300:
                    header = overlayList[1]
                    drawcColor = (203, 192, 255)
                elif 350 < x1 < 500:
                    header = overlayList[2]
                    drawcColor = (0, 255, 255)
                elif 550 < x1 < 700:
                    header = overlayList[3]
                    drawcColor = (255, 0, 0)
                elif 700 < x1 < 850:
                    header = overlayList[4]
                    drawcColor = (0, 255, 0)
                elif 900 < x1 < 1050:
                    header = overlayList[5]
                    drawcColor = (0, 165, 255)
                elif 1050 < x1 < 1280:
                    header = overlayList[6]
                    drawcColor = (0, 0, 0)
            cv2.rectangle(img,(x1 , y1 - 25), (x2, y2 + 25), drawcColor, cv2.FILLED)


    #5.If Drawing Mode - Index finger is up - Drawing
        if fingers[1] and fingers[2] == False:
            cv2.circle(img,(x1 , y1), 15, drawcColor, cv2.FILLED)
            print("Drawing Mode")
            if xp == 0 and yp == 0:
                xp, yp = x1, y1
            if drawcColor == (0, 0, 0):
                cv2.line(img, (xp, yp), (x1, y1), drawcColor, eraserThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawcColor, eraserThickness)
            else:
                cv2.line(img, (xp, yp), (x1, y1), drawcColor, brushThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawcColor, brushThickness)

            xp, yp = x1, y1 

    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)    
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, imgCanvas)




    #Setting the header image
    img[0:125, 0:1280] = header

    #flipped = cv2.flip(img, 1)
    cv2.imshow ("Image",img)
    cv2.imshow("Canvas", imgCanvas)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break