import cv2
import pickle
import numpy as np
import os

video = cv2.VideoCapture(0)

facedetect = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

if not os.path.exists("data"):
    os.makedirs("data")

faces_data = []
labels = []

name = input("Enter Your Name: ")

count = 0

while True:
    ret, frame = video.read()
    if not ret:
        continue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = facedetect.detectMultiScale(gray, 1.1, 5, minSize=(100, 100))

    print("Faces detected:", len(faces))

    for (x, y, w, h) in faces:
        crop = frame[y:y+h, x:x+w]
        resized = cv2.resize(crop, (50, 50))

        # safer capture rule
        if count < 100:
            faces_data.append(resized)
            labels.append(name)
            count += 1

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, str(count), (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Register Face", frame)

    if cv2.waitKey(1) & 0xFF == ord('q') or count == 100:
        break

video.release()
cv2.destroyAllWindows()

# ---------------- SAVE ----------------
faces_data = np.array(faces_data).reshape(len(faces_data), -1)

if 'faces_data.pkl' in os.listdir('data/'):
    with open('data/faces_data.pkl', 'rb') as f:
        old_faces = pickle.load(f)

    with open('data/names.pkl', 'rb') as f:
        old_labels = pickle.load(f)

    faces_data = np.vstack((old_faces, faces_data))
    labels = old_labels + labels

with open('data/faces_data.pkl', 'wb') as f:
    pickle.dump(faces_data, f)

with open('data/names.pkl', 'wb') as f:
    pickle.dump(labels, f)

print("Face registered successfully!")