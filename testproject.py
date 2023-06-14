import cv2
import time
import posemodule as pm
cap = cv2.VideoCapture(0)
pTime = 0
detector = pm.poseDetector()
while(True):
    success, img = cap.read()
    img = detector.findPose(img)
    lmList = detector.findPosition(img,draw=False)
    if len(lmList)!=0:
        print(lmList)
        cv2.circle(img,(lmList))
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN,3, (255, 0, 0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(True)
