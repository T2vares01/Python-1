import cv2
import mediapipe as mp
import pyautogui as py

webcam = cv2.VideoCapture(0)
hand = mp.solutions.hands
Hand = hand.Hands(max_num_hands=2)
mpDrw = mp.solutions.drawing_utils

if webcam.isOpened():
    validacao, frame = webcam.read()
    while validacao:
        validacao, frame = webcam.read()
        cv2.imshow("Video da Webcam", frame)
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = Hand.process(img)
        hanspoint = result.multi_hand_landmarks
        key = cv2.waitKey(5)
        h, w, _ = img.shape
        pontos = []
        key = cv2.waitKey(5)
        if hanspoint:
            for points in hanspoint:
                #print(points)
                mpDrw.draw_landmarks(frame,points,hand.HAND_CONNECTIONS)
                for id, cord in enumerate(points.landmark):
                    cx, cy = int(cord.x * w), int(cord.y * h)
                    print("x:",cx,"y:",cy)
        if key == 27: # ESC
            break
    cv2.imwrite("FotoLira.png", frame)

webcam.release()
cv2.destroyAllWindows()
