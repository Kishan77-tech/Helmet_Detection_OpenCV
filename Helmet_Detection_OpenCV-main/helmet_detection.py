from ultralytics import YOLO
import cv2

# Load trained YOLOv8 model
model = YOLO("helmet.pt")  # Make sure this file is in the same folder

# Ask user for source
source = input("Enter 0 for webcam or video file path: ")

# Open video or webcam
cap = cv2.VideoCapture(1 if source.strip() == "1" else source)

# Create display window
cv2.namedWindow("Helmet Detection", cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLOv8 detection
    results = model(frame, conf=0.6, 
                    iou=0.5)


    # Draw bounding boxes
    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cls = int(box.cls[0])
            label = model.names[cls]

            # Green if helmet, Red if no helmet
            color = (0, 255, 0) if "helmet" in label.lower() else (0, 0, 255)

            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

    # Show the frame
    cv2.imshow("Helmet Detection", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
