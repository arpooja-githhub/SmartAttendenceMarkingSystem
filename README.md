# 📌 Smart Attendance Marking System using Face Recognition

## 📖 Overview

The Smart Attendance Marking System using Face Recognition is an automated attendance management solution that uses Computer Vision and Machine Learning techniques to detect and recognize faces in real time. The system captures facial data using a webcam, identifies registered users, and automatically marks attendance without manual intervention.

This project eliminates traditional attendance methods such as manual registers, ID cards, or biometric touch systems, making attendance tracking faster, more secure, and efficient.

---

# 🚀 Features

- ✅ Real-time face detection using OpenCV
- ✅ Face recognition using K-Nearest Neighbors (KNN)
- ✅ Automatic attendance marking
- ✅ Duplicate attendance prevention
- ✅ Attendance stored in CSV format
- ✅ Streamlit dashboard for attendance monitoring
- ✅ Simple and user-friendly interface
- ✅ Webcam-based live recognition

---

# 🛠️ Technologies Used

## 🔹 Frontend
- Streamlit

## 🔹 Backend
- Python
- OpenCV
- NumPy
- Scikit-learn
- Pandas
- Pickle

---

# 📂 Project Structure

```bash
SmartAttendanceSystem/
│
├── data/
│   ├── faces_data.pkl
│   ├── names.pkl
│
├── Attendance/
│   ├── Attendance_dd-mm-yyyy.csv
│
├── app.py
├── capture.py
├── streamlit_app.py
├── README.md
```

---

# ⚙️ System Requirements

## 🖥️ Hardware Requirements
- Processor: Intel i3 or above
- RAM: 4GB minimum
- Webcam
- Storage: 500MB free space

## 💻 Software Requirements
- Python 3.8+
- OpenCV
- Streamlit
- Scikit-learn
- Pandas
- NumPy



---

# 🧠 Working Principle

1. Face images are captured using webcam
2. OpenCV detects faces using Haar Cascade classifier
3. Face images are resized and converted into vectors
4. KNN algorithm compares live face with stored dataset
5. If matched, attendance is marked automatically
6. Attendance data is stored in CSV format

---

# Flow Chat

<img width="420" height="924" alt="image" src="https://github.com/user-attachments/assets/b3986ac1-0d72-457f-b4c5-26a01f4523c0" />


---
# FINAL DASHBOARD OUTPUT
<img width="3022" height="1560" alt="image" src="https://github.com/user-attachments/assets/7ea09596-9f50-492d-9c15-2568331d3935" />


# 🌐 Future Enhancements

- Firebase/MySQL database integration
- Deep learning-based face recognition
- Mobile application support
- Cloud deployment
- Attendance analytics dashboard
- Check-in / Check-out functionality

---

# 🎯 Applications

- Schools and Colleges
- Offices and Companies
- Training Institutes
- Organizations and Events

---

# 👨‍💻 Author

Developed by: **Pooja A R**

---

# 📜 License

This project is developed for educational and learning purposes.
