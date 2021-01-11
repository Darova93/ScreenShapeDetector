import cv2
import numpy as np
import pyautogui
import imutils

from Tools.ShapeDetector import ShapeDetector

SCREEN_SIZE = (1920, 1080)

fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi", fourcc, 20.0, pyautogui.size())
shapeDetector = ShapeDetector()

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # find contours
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts:
        # compute the center of the contour, then detect the name of the
        # shape using only the contour
        M = cv2.moments(c)
        cX = int((M["m10"] / M["m00"])) if M["m00"] != 0 else 0
        cY = int((M["m01"] / M["m00"])) if M["m00"] != 0 else 0
        shape = shapeDetector.detect(c)
        # multiply the contour (x, y)-coordinates by the resize ratio,
        # then draw the contours and the name of the shape on the image
        c = c.astype("float")
        c = c.astype("int")
        cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
        cv2.putText(frame, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    # write the frame
    out.write(frame)
    # show the frame
    cv2.imshow("screenshot", frame)
    # if the user clicks q, it exits
    if cv2.waitKey(1) == ord("q"):
        break

# make sure everything is closed when exited
cv2.destroyAllWindows()
out.release()