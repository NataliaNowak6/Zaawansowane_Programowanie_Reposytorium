from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

def detect(image_path, task_id):
    img = cv2.imread(image_path)
    results = model(img)

    count = 0
    for r in results:
        for box in r.boxes:
            if int(box.cls[0]) == 0:
                count += 1
                x1,y1,x2,y2 = map(int, box.xyxy[0])
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)

    output = f"results/{task_id}.jpg"
    cv2.imwrite(output, img)

    return count, output