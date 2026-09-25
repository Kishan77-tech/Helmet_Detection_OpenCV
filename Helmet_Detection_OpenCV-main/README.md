# 🪖 Helmet Detection System using YOLOv8

A real-time **Helmet Detection System** built using **YOLOv8, OpenCV, FastAPI, and Streamlit**.

The system detects whether a person is wearing a helmet and displays the detection result with bounding boxes and confidence scores.

## 🚀 Features

* 🪖 Helmet detection using YOLOv8
* 🚫 No-helmet detection
* 📷 Image upload and detection
* 🎯 Bounding boxes around detected objects
* 📊 Helmet and No-Helmet count
* 📈 Confidence score for detections
* ⚡ FastAPI backend
* 🖥️ Streamlit frontend
* 🔗 Frontend and backend integrated in a single project

## 🛠️ Technology Stack

| Technology  | Purpose                        |
| ----------- | ------------------------------ |
| Python      | Core programming language      |
| YOLOv8      | Object detection               |
| Ultralytics | YOLOv8 implementation          |
| OpenCV      | Image processing               |
| FastAPI     | Backend REST API               |
| Streamlit   | Frontend interface             |
| Requests    | Frontend-backend communication |

## 📁 Project Structure

```text
Helmet_Detection_OpenCV/
│
├── backend/
│   └── app.py
│
├── frontend/
│   └── app.py
│
├── helmet.pt
├── helmet.mp4
├── helmet_detection.py
├── yolov8n.pt
├── data.yaml
├── requirements.txt
├── README.md
├── .gitignore
└── runs/
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Kishan77-tech/Helmet_Detection_OpenCV.git
```

### 2. Open the project directory

```bash
cd Helmet_Detection_OpenCV
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

The project contains two components:

```text
Frontend → Streamlit
Backend  → FastAPI
```

### Step 1 — Start Backend

Open a terminal in the project directory and run:

```bash
uvicorn backend.app:app --reload
```

Backend will run at:

```text
http://127.0.0.1:8000
```

### Step 2 — Start Frontend

Open another terminal and run:

```bash
streamlit run frontend/app.py
```

The Streamlit application will open in your browser.

Usually:

```text
http://localhost:8501
```

## 🔄 Application Workflow

```text
User
  │
  ▼
Streamlit Frontend
  │
  │ Upload Image
  ▼
FastAPI Backend
  │
  ▼
YOLOv8 Model
  │
  ▼
Object Detection
  │
  ├── Helmet
  │
  └── No Helmet
  │
  ▼
Detection Result
  │
  ▼
Streamlit Frontend
```

## 🧠 Detection Process

1. User uploads an image through the Streamlit interface.
2. The frontend sends the image to the FastAPI backend.
3. FastAPI receives the uploaded image.
4. The YOLOv8 model processes the image.
5. Detected objects are identified.
6. Bounding boxes and confidence scores are added.
7. Helmet and No-Helmet detections are counted.
8. The processed image is returned to the frontend.
9. The result is displayed to the user.

## 📊 Output

The application displays:

* Original uploaded image
* Detection result
* Helmet count
* No-Helmet count
* Bounding boxes
* Confidence scores

## 🔮 Future Enhancements

* Real-time webcam detection
* Video upload and processing through the web interface
* Automatic violation logging
* Database integration
* Detection history
* Dashboard and analytics
* Email/SMS notification system

## 👨‍💻 Author

**Kishan Gupta**

B.Tech – Computer Science Engineering (AI & ML)

GitHub: https://github.com/Kishan77-tech

## 📌 Project Status

The project currently supports image-based helmet detection through an integrated **Streamlit frontend and FastAPI backend**.
