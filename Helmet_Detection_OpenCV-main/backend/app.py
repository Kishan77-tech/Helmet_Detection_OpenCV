from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from ultralytics import YOLO
import cv2
import os
import uuid

app = FastAPI(title="Helmet Detection API")

# Path of trained helmet detection model
MODEL_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "helmet.pt"
)

model = YOLO(MODEL_PATH)

# Folders for uploaded and processed images
UPLOAD_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "uploads"
)

OUTPUT_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "outputs"
)

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)


@app.get("/")
def home():
    return {
        "message": "Helmet Detection API is running"
    }


@app.post("/detect")
async def detect(file: UploadFile = File(...)):

    file_id = str(uuid.uuid4())

    filename = file.filename

    input_path = os.path.join(
        UPLOAD_DIR,
        file_id + "_" + filename
    )

    output_path = os.path.join(
        OUTPUT_DIR,
        file_id + "_" + filename
    )

    # Save uploaded file
    contents = await file.read()

    with open(input_path, "wb") as f:
        f.write(contents)

    # Read image
    image = cv2.imread(input_path)

    if image is None:
        return {
            "error": "Invalid image file"
        }

    # YOLO detection
    results = model(image)

    helmet_count = 0
    no_helmet_count = 0

    for result in results:

        for box in result.boxes:

            x1, y1, x2, y2 = map(
                int,
                box.xyxy[0]
            )

            cls = int(box.cls[0])

            label = model.names[cls]

            confidence = float(box.conf[0])

            # Helmet = Green
            if "helmet" in label.lower():
                color = (0, 255, 0)
                helmet_count += 1

            # No Helmet = Red
            else:
                color = (0, 0, 255)
                no_helmet_count += 1

            # Draw bounding box
            cv2.rectangle(
                image,
                (x1, y1),
                (x2, y2),
                color,
                2
            )

            # Display label + confidence
            cv2.putText(
                image,
                f"{label} {confidence:.2f}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                color,
                2
            )

    # Save processed image
    cv2.imwrite(
        output_path,
        image
    )

    return {
        "message": "Detection completed",
        "helmet_count": helmet_count,
        "no_helmet_count": no_helmet_count,
        "result_file": os.path.basename(output_path)
    }


@app.get("/result/{filename}")
def get_result(filename: str):

    path = os.path.join(
        OUTPUT_DIR,
        filename
    )

    return FileResponse(path)