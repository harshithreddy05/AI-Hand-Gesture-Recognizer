import cv2
import mediapipe as mp
from gesture_recognition import recognize_gesture

from mediapipe.tasks import python
from mediapipe.tasks.python import vision


# -----------------------------------
# Model location
# -----------------------------------

MODEL_PATH = "models/hand_landmarker.task"


# -----------------------------------
# MediaPipe Hand Landmarker
# -----------------------------------

base_options = python.BaseOptions(
    model_asset_path=MODEL_PATH
)

options = vision.HandLandmarkerOptions(
    base_options=base_options,
    running_mode=vision.RunningMode.VIDEO,
    num_hands=1,
    min_hand_detection_confidence=0.5,
    min_hand_presence_confidence=0.5,
    min_tracking_confidence=0.5
)

landmarker = vision.HandLandmarker.create_from_options(
    options
)


# -----------------------------------
# Open camera
# -----------------------------------

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("❌ Could not open camera")
    exit()

print("✅ AI Hand Detection started!")
print("Press Q to quit.")


frame_number = 0


# -----------------------------------
# Main loop
# -----------------------------------

while True:

    success, frame = camera.read()

    if not success:
        print("❌ Could not read camera frame")
        break

    # Mirror camera
    frame = cv2.flip(frame, 1)

    # Convert BGR → RGB
    rgb_frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    # Create MediaPipe image
    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb_frame
    )

    # Timestamp must increase
    timestamp_ms = frame_number * 33
    frame_number += 1

    # Detect hand
    result = landmarker.detect_for_video(
        mp_image,
        timestamp_ms
    )


    # -----------------------------------
    # Draw hand landmarks
    # -----------------------------------

    if result.hand_landmarks:

        height, width, _ = frame.shape

        for hand in result.hand_landmarks:

            points = []

            # Convert normalized coordinates
            # to screen coordinates

            for landmark in hand:

                x = int(landmark.x * width)
                y = int(landmark.y * height)

                points.append((x, y))

            # Recognize gesture
            gesture = recognize_gesture(points)

            #Display gesture
            cv2.putText(
                frame,
                gesture,
                (30, 60),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.5,
                (0, 255, 0),
                3
            )

            # Draw landmark
            for x, y in points:
                cv2.circle(
                    frame,
                    (x, y),
                    5,
                    (0, 255, 0),
                    -1
                )


            # Hand connections
            connections = [

                # Thumb
                (0, 1),
                (1, 2),
                (2, 3),
                (3, 4),

                # Index finger
                (0, 5),
                (5, 6),
                (6, 7),
                (7, 8),

                # Middle finger
                (0, 9),
                (9, 10),
                (10, 11),
                (11, 12),

                # Ring finger
                (0, 13),
                (13, 14),
                (14, 15),
                (15, 16),

                # Pinky
                (0, 17),
                (17, 18),
                (18, 19),
                (19, 20),

                # Palm
                (5, 9),
                (9, 13),
                (13, 17)
            ]


            for start, end in connections:

                cv2.line(
                    frame,
                    points[start],
                    points[end],
                    (0, 255, 0),
                    2
                )


    # -----------------------------------
    # Display
    # -----------------------------------

    cv2.imshow(
        "AI Hand Gesture Recognizer",
        frame
    )


    # Quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# -----------------------------------
# Cleanup
# -----------------------------------

camera.release()

landmarker.close()

cv2.destroyAllWindows()

print("Camera closed.")