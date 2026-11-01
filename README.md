Title: HANDFLOW
A Python-Based Desktop Utility for Touchless Computer Control

Video Demo: https://youtu.be/78sE_fJVLQ4

The idea behind HANDFLOW came to me while watching Avengers Endgame: Encore. I saw Tony Stark using hand 
gestures to zoom, interact with simulations, and manipulate objects without physically touching a computer.
That inspired me to build something similar using Python. As someone who spends a lot of time reading documents and studying on a computer, 
I wanted a way to scroll through long documents without constantly reaching for my mouse or trackpad. I also started thinking about 
people who frequently give presentations, attend conferences, or teach and need to interact with their computers from a distance.

For example, my mom frequently participates in conferences. Whenever she needs to change a slide, scroll 
through a document, or zoom in on something she is presenting, she has to approach her computer to perform 
the action manually. That is where HANDFLOW comes in.

My goal was to create a simple, accessible tool that allows users to control scrolling and zooming through 
hand gestures captured by a webcam, making computer interaction more convenient and hands-free.

HANDFLOW is a Python-based desktop utility that uses real-time hand tracking and gesture recognition to enable touchless 
scrolling and zoom control through a webcam. The software uses OpenCV to access the webcam and MediaPipe to detect and 
track 21 landmarks on the hand. Based on the detected hand position and finger configuration, the program identifies specific 
gestures and triggers corresponding actions through PyAutoGUI.

Features:
-- Real-Time Hand Tracking: Detects and tracks 21 hand landmarks using MediaPipe.
-- Gesture Recognition: Recognizes specific finger configurations to determine the active control mode.
-- Touchless Scrolling: Raises all five fingers to activate scrolling.
-- Touchless Zoom Control: Raises only the index finger to activate zoom control.
-- Hand Movement Detection: Moving the hand upward or downward triggers the corresponding scrolling or zooming action.
-- Visual Mode Indicator: Displays the currently active mode, either SCROLL or ZOOM, in the top-left corner of the webcam window.
-- Webcam-Based Interaction: Uses a webcam to detect gestures without requiring additional hardware.

How It Works:
HANDFLOW combines three main technologies: OpenCV, MediaPipe, and PyAutoGUI.

1. OpenCV — Webcam Access

OpenCV, accessed through the cv2 module, allows the application to access the computer's webcam and capture video frames in real time.
These frames provide the visual input needed for hand tracking. The webcam window also displays the detected hand and the currently active control mode.
To close the application, press the q key while the webcam window is active.

2. MediaPipe — Hand Tracking and Landmark Detection

MediaPipe processes the captured frames to detect the hand and identify its 21 landmarks. These landmarks represent key points on 
the hand, including the fingertips and joints. The application uses the detected landmarks to analyze the hand's position and finger 
configuration. This information helps determine which gesture the user is performing.
The project also requires MediaPipe's hand landmark model file, hand_landmarker.task, to initialize the hand landmark detection system.

3. PyAutoGUI — Computer Control

PyAutoGUI allows Python to interact with the computer by simulating input actions.
Once the application recognizes a supported gesture, it uses PyAutoGUI to execute the corresponding scrolling or zooming action.
The application combines the detected finger configuration with hand movement to determine when and how these actions should occur. 
This helps prevent unintended interactions when the hand is visible but the user has not activated a supported gesture.


Gesture Controls:

All five fingers raised -- Activate scrolling mode
Only the index finger raised -- Activate zoom mode
Move hand upward in scrolling mode -- Scroll up
Move hand downward in scrolling mode -- Scroll down
Move hand upward in zoom mode -- Zoom in
Move hand downward in zoom mode -- Zoom out

Technologies Used:
Python: Main programming language.
OpenCV (opencv-python): Webcam access and video frame processing.
MediaPipe: Real-time hand tracking and landmark detection.
PyAutoGUI: Automated computer input for scrolling and zoom control.


These are the requirements before running HANDFLOW:
Python installed.
A working webcam.
The required Python libraries -- You can see them in the requirements.txt file
The MediaPipe hand landmark model file, hand_landmarker.task.
