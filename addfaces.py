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

    faces = facedetect.detectMultiScale(gray, 1.1, 6, minSize=(100, 100))

    for (x, y, w, h) in faces:

        crop = frame[y:y+h, x:x+w]
        resized = cv2.resize(crop, (50, 50)).flatten()

        if count < 100:
            faces_data.append(resized)
            labels.append(name)
            count += 1

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, str(count), (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Capture", frame)

    if cv2.waitKey(1) & 0xFF == ord('q') or count == 100:
        break

video.release()
cv2.destroyAllWindows()

# ---------------- SAVE ----------------
faces_data = np.array(faces_data)
labels = labels[:len(faces_data)]

if 'faces_data.pkl' in os.listdir('data'):
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

print("Face registered successfully")
# import cv2
# import pickle
# import numpy as np
# import os
# video=cv2.VideoCapture(0)
# facedetect=cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

# faces_data=[]

# i=0

# name=input("Enter Your Name: ")
# while True:
#     ret, frame = video.read()
#     if not ret:
#         print("Camera error")
#         continue

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     faces = facedetect.detectMultiScale(
#         gray, 1.1, 6, minSize=(100, 100)
#     )

#     print("Faces detected:", len(faces))

#     for (x, y, w, h) in faces:
#         crop_img = frame[y:y+h, x:x+w]
#         resized_img = cv2.resize(crop_img, (50, 50))

#         if len(faces_data) < 100 and i % 5 == 0:
#             faces_data.append(resized_img)

#         i += 1

#         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
#         cv2.putText(frame, str(len(faces_data)),
#                     (50, 50),
#                     cv2.FONT_HERSHEY_SIMPLEX,
#                     1, (0, 255, 0), 2)

#     cv2.imshow("Frame", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q') or len(faces_data) == 100:
#         break
# video.release()
# cv2.destroyAllWindows()

# faces_data=np.asarray(faces_data)
# faces_data=faces_data.reshape(100, -1)


# if 'names.pkl' not in os.listdir('data/'):
#     names=[name]*100
#     with open('data/names.pkl', 'wb') as f:
#         pickle.dump(names, f)
# else:
#     with open('data/names.pkl', 'rb') as f:
#         names=pickle.load(f)
#     names=names+[name]*50
#     with open('data/names.pkl', 'wb') as f:
#         pickle.dump(names, f)

# if 'faces_data.pkl' not in os.listdir('data/'):
#     with open('data/faces_data.pkl', 'wb') as f:
#         pickle.dump(faces_data, f)
# else:
#     with open('data/faces_data.pkl', 'rb') as f:
#         faces=pickle.load(f)
#     faces=np.append(faces, faces_data, axis=0)
#     with open('data/faces_data.pkl', 'wb') as f:
#         pickle.dump(faces, f)