import cv2
import pickle
import numpy as np
import os
import csv
from datetime import datetime
from sklearn.neighbors import KNeighborsClassifier

# ---------------- DATE ----------------
date = datetime.now().strftime("%d-%m-%Y")

# ---------------- PATH ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
attendance_folder = os.path.join(BASE_DIR, "Attendance")

if not os.path.exists(attendance_folder):
    os.makedirs(attendance_folder)

file_path = os.path.join(attendance_folder, f"Attendance_{date}.csv")

# ---------------- CAMERA ----------------
video = cv2.VideoCapture(0)

# ---------------- FACE DETECTOR ----------------
facedetect = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# ---------------- LOAD DATA ----------------
with open('data/names.pkl', 'rb') as f:
    LABELS = pickle.load(f)

with open('data/faces_data.pkl', 'rb') as f:
    FACES = pickle.load(f)

FACES = np.array(FACES)
LABELS = np.array(LABELS)

print("Faces:", FACES.shape)
print("Labels:", LABELS.shape)

# ---------------- TRAIN MODEL ----------------
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(FACES, LABELS)

# ---------------- STORE MARKED NAMES ----------------
marked_today = set()

# Load already marked names from today's file (important)
if os.path.exists(file_path):
    import pandas as pd
    df = pd.read_csv(file_path)

    if "NAME" in df.columns:
        for n in df["NAME"]:
            marked_today.add(n + date)

# ---------------- MAIN LOOP ----------------
while True:
    ret, frame = video.read()
    if not ret:
        continue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = facedetect.detectMultiScale(gray, 1.1, 6, minSize=(100, 100))

    for (x, y, w, h) in faces:

        crop = frame[y:y+h, x:x+w]
        resized = cv2.resize(crop, (50, 50)).flatten().reshape(1, -1)

        output = knn.predict(resized)
        name = str(output[0])

        timestamp = datetime.now().strftime("%H:%M:%S")

        # ---------------- DRAW BOX ----------------
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, name, (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                    (255, 255, 255), 2)

        # ---------------- UNIQUE PER DAY LOGIC ----------------
        key = name + date

        if key not in marked_today:

            marked_today.add(key)

            file_exists = os.path.isfile(file_path)

            with open(file_path, "a", newline="") as f:
                writer = csv.writer(f)
                if not file_exists:
                    writer.writerow(["NAME", "TIME"])
                writer.writerow([name, timestamp])

            print("Marked once:", name)

        break  # IMPORTANT: only one face per frame

    # ---------------- SHOW ----------------
    cv2.imshow("Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()