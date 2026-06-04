import cv2, time, json

cap = cv2.VideoCapture("../data/CAM 1 - zone.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    event = {"timestamp": time.time(), "event": "footfall", "count": 1}
    print(json.dumps(event))
    time.sleep(0.5)

cap.release()
