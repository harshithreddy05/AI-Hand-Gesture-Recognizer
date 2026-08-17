# 🤖 AI Hand Gesture Recognizer

<p align="center">

### ✋ Real-Time Hand Gesture Recognition Using AI & Computer Vision

An intelligent computer vision application that detects and recognizes hand gestures in real time using a webcam, MediaPipe, OpenCV, and Python.

</p>

---

## 🚀 Overview

**AI Hand Gesture Recognizer** is a real-time computer vision project that uses your device's camera to detect a human hand, track its landmarks, and identify different hand gestures.

The system processes the camera feed continuously and uses **MediaPipe Hand Landmarker** to identify 21 key points on the hand. These landmarks are then analyzed using a gesture recognition algorithm to determine the gesture being performed.

The goal of this project is to demonstrate how **Artificial Intelligence, Computer Vision, and Python** can be combined to create an interactive real-world application.

---

## ✨ Features

- 🎥 Real-time webcam processing
- ✋ Real-time hand detection
- 🟢 21-point hand landmark tracking
- 🤖 AI-powered hand landmark detection using MediaPipe
- 🧠 Gesture classification
- ⚡ Real-time response
- 💻 Runs locally on your computer
- 🔒 No image or video data is uploaded to a server
- 👥 Designed as a collaborative GitHub project

### Currently Recognized Gestures

| Gesture | Recognition |
|---|---|
| ✋ Open Palm | `OPEN PALM` |
| ✊ Fist | `FIST` |
| ✌️ Peace | `PEACE` |
| ☝️ Pointing | `POINTING` |
| 👍 Thumbs Up | `THUMBS UP` |

---

# 📸 Project Preview

> Add screenshots or GIFs of the application here.bb

### Hand Detection

![Hand Detection](screenshots/hand-detection.png)

### Gesture Recognition

![Gesture Recognition](screenshots/gesture-recognition.png)

> **Tip:** Replace these images with screenshots from your own project.

---

# 🧠 How It Works

The application follows a simple computer vision pipeline:

```text
              📷 Webcam
                  │
                  ▼
             🎥 OpenCV
                  │
                  ▼
          🖼️ Video Frame
                  │
                  ▼
       🤖 MediaPipe Hand Landmarker
                  │
                  ▼
        ✋ 21 Hand Landmarks
                  │
                  ▼
       🧠 Gesture Recognition
                  │
                  ▼
          🎯 Gesture Result

 Processing Pipeline

1. Capture
OpenCV captures frames from the device webcam.

2. Pre-processing
Each frame is converted from BGR to RGB format for MediaPipe processing.

3. Hand Detection
MediaPipe detects the hand and identifies 21 hand landmarks.

4. Landmark Processing
The landmark coordinates are converted into screen coordinates.

5. Gesture Recognition
The landmark positions are analyzed to determine the current hand gesture.

6. Real-Time Display
The recognized gesture is displayed directly on the camera feed.

🛠️Tech Stack

| Technology     | Purpose                        |
| -------------- | ------------------------------ |
| 🐍 Python 3.11 | Core programming language      |
| 👁️ OpenCV     | Webcam & image processing      |
| 🤖 MediaPipe   | Hand landmark detection        |
| 🔢 NumPy       | Numerical processing           |
| 🌳 Git         | Version control                |
| 🐙 GitHub      | Collaboration & source control |
| 💻 VS Code     | Development environment        |


📂Project Structure

AI-Hand-Gesture-Recognizer/
│
├── models/
│   └── hand_landmarker.task
│
├── main.py
├── gesture_recognition.py
├── requirements.txt
├── README.md
├── .gitignore
└── venv/
venv/ is excluded from GitHub using .gitignore.

⚙️Installation

1️⃣ Clone the repository

git clone https://github.com/harshithreddy05/AI-Hand-Gesture-Recognizer.git
Move into the project:
cd AI-Hand-Gesture-Recognizer

2️⃣ Install Python

Make sure Python 3.11 is installed.
Check your version:
python3.11 --version
Expected:
Python 3.11.x

3️⃣ Create a virtual environment

macOS / Linux
python3.11 -m venv venv
Activate it:
source venv/bin/activate

Windows
py -3.11 -m venv venv
Activate:
venv\Scripts\activate

4️⃣ Install dependencies

pip install -r requirements.txt

This installs the required libraries:

OpenCV
MediaPipe
NumPy

▶️ Run the Project

After activating the virtual environment:
python main.py

You should see:
✅ AI Hand Detection started!

Press Q to quit.

A webcam window will open.

Place your hand in front of the camera and perform one of the supported gestures.

To stop the application:
Press Q


🔐 Privacy

The project processes the webcam feed locally on the user's computer.

No camera footage is intentionally uploaded to a remote server by this application.

Camera permission may be required by your operating system.



🌐 Cross-Platform Usage

The project is designed to work across different computers.

A different user does not need your Mac or your Wi-Fi network.

They simply need to:

Clone Repository
      ↓
Install Python
      ↓
Create Virtual Environment
      ↓
Install Requirements
      ↓
Run main.py

The application uses the webcam available on their own computer.


👥 Team

Development Team

Member	Role
harshithreddy05	Developer
Priyankareddy1762.afk Developer

Collaboration

This project was developed collaboratively using:

Git
GitHub
VS Code
Feature development
Testing and debugging


🔮 Future Improvements

The project can be extended with:

🎯 Improved gesture recognition accuracy
✋ Additional hand gestures
🤚 Two-hand gesture recognition
🔊 Voice feedback
🖥️ Graphical user interface
📊 Gesture statistics and history
🎮 Gesture-controlled applications
🖱️ Gesture-controlled mouse
🎵 Gesture-controlled media player
🌐 Web-based interface
🤖 Machine-learning-based gesture classification


📌 Use Cases

Hand gesture recognition can be used in many real-world applications:

♿ Accessibility
Enable users to interact with computers using gestures instead of traditional input devices.

🎮 Gaming
Use hand gestures as an alternative gaming input mechanism.

🖥️ Human-Computer Interaction
Create touch-free interfaces for computers and smart devices.

🏠 Smart Systems
Control smart devices using predefined hand gestures.

🎓 Education
Demonstrate practical applications of AI and computer vision.

📈 Learning Outcomes
Through this project, we explored:
Computer vision fundamentals
Real-time video processing
Hand landmark detection
MediaPipe
OpenCV
Python programming
Coordinate-based gesture recognition
Git and GitHub collaboration
Virtual environments
Dependency management

⭐ Support
If you find this project interesting, consider giving the repository a ⭐ on GitHub!

📜 License
This project is intended for educational and demonstration purposes.
<p align="center">

🤖 Built with Python + OpenCV + MediaPipe
Made with curiosity, code, and computer vision.

</p> ```