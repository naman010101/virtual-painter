import cv2
import mediapipe as mp
import time
import os

class handDetector:
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        # 1. SETUP: Load the model file 
        self.MODEL_PATH = 'hand_landmarker.task' 
        options = mp.tasks.vision.HandLandmarkerOptions( 
            base_options=mp.tasks.BaseOptions(model_asset_path=self.MODEL_PATH), 
            running_mode=mp.tasks.vision.RunningMode.IMAGE 
        ) 
      
        self.landmarker = mp.tasks.vision.HandLandmarker.create_from_options(options)

      # Define hand connections outside the loop
        self.HAND_CONNECTIONS = [
            (0,1),(1,2),(2,3),(3,4),
            (0,5),(5,6),(6,7),(7,8),
            (5,9),(9,10),(10,11),(11,12),
            (9,13),(13,14),(14,15),(15,16),
            (13,17),(17,18),(18,19),(19,20),
            (0,17)
        ]

        self.tipIds = [4, 8, 12, 16, 20]

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 

        # Create MediaPipe Image 
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=imgRGB) 

        # Detect hand landmarks 
        self.hand_landmarker_result = self.landmarker.detect(mp_image) 
        
        return img
    
    def findPosition(self, img, handNo=0, draw=True):
        self.lmList = []
        
        if self.hand_landmarker_result.hand_landmarks:
         if handNo < len(self.hand_landmarker_result.hand_landmarks):
            hand_landmarks = self.hand_landmarker_result.hand_landmarks[handNo]
            points = []  
            h, w, c = img.shape
         
            for id, lm in enumerate(hand_landmarks): 
                cx, cy = int(lm.x * w), int(lm.y * h)
                #print(id, cx, cy) 
                points.append((cx, cy)) 
                
                self.lmList.append([id, cx, cy])
                if draw:
                # Highlight the tip of the index finger 
                  cv2.circle(img, (cx,cy),7,(255,0,255),cv2.FILLED) 
                
                  for connection in self.HAND_CONNECTIONS: 
                    start_idx, end_idx = connection 
                    if start_idx < len(points) and end_idx < len(points):
                        cv2.line(img, points[start_idx], points[end_idx], (255, 0, 0), 2)
        return self.lmList
    
    def fingersUp(self):
        fingers = []
        if len(self.lmList) != 0:
        
        #For Thumb
            if self.lmList[17][1] > self.lmList[4][1]:

                if self.lmList[self.tipIds[0]][1] < self.lmList[self.tipIds[0]-1][1]:
                   fingers.append(1)
                else:
                   fingers.append(0)
            else:
                if self.lmList[self.tipIds[0]][1] > self.lmList[self.tipIds[0]-1][1]:
                   fingers.append(1)
                else:
                   fingers.append(0)

        #For Fingers
            for id in range(1, 5):
                if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id]-2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
        return fingers
def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        success, img = cap.read()
        if not success:
            break

        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        if len(lmList) != 0:
            print(lmList[4])

        cTime = time.time()
        if pTime > 0:
            fps = 1 / (cTime - pTime)
        else:
            fps = 0
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)

        cv2.imshow("Hand Tracking", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()


