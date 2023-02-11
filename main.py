import cv2
import numpy as np

reddit = cv2.VideoCapture("reddit/concert.mp4")
relax = cv2.VideoCapture("relax/1.mp4")


while True:
    # Capture frame-by-frame
    ret, frame = reddit.read()
    ret2, frame2 = relax.read()
    frame = cv2.resize(frame,(960,540))
    frame2 = cv2.resize(frame2,(960,540))
    contrast = 1.0
    brightness = 0
    final_video = cv2.vconcat((frame, frame2))
    # frame = np.clip(contrast * frame + brightness, 0, 255)
    # cv2.imshow('frame', frame)
    # cv2.imshow('frame',frame2)
    cv2.imshow("result", final_video)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
