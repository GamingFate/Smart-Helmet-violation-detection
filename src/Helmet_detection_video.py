import cv2
import math
import cvzone
from ultralytics import YOLO
import torch
print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0))


# ✅ Use GPU (CUDA) if available
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f"Running on: {device.upper()}")

# ✅ Load YOLO model (use small model or your trained one)
# For highest FPS, train or convert your weights on YOLOv8n
model = YOLO("Weights/best.pt").to(device)

# ✅ Open video
video_path = "Media/bike_2.mp4"
cap = cv2.VideoCapture(video_path)

# ✅ Target 60 FPS playback settings
cap.set(cv2.CAP_PROP_FPS, 25)


# ✅ Class names
classNames = ['With Helmet', 'Without Helmet']

while True:
    success, img = cap.read()
    if not success:
        break

    
    # ✅ Run YOLO detection on GPU
    results = model(img, stream=True, imgsz=480, device=device, verbose=False)

    # ✅ Draw detections
    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            w, h = x2 - x1, y2 - y1
            conf = round(float(box.conf[0]), 2)
            cls = int(box.cls[0])

            # Fast lightweight drawing
            cvzone.cornerRect(img, (x1, y1, w, h), l=5, rt=1)
            cvzone.putTextRect(img, f'{classNames[cls]} {conf}',
                               (max(0, x1), max(35, y1)),
                               scale=1, thickness=1)

    # ✅ Display the output
    cv2.imshow("Helmet Detection (GPU 60FPS Mode)", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
