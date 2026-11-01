#Hands Scroll Implementation


import time
import os

#Libraries
import cv2 #Camara Access

#Hand Tracking
import mediapipe as mp 
from mediapipe.tasks import python as mp_python
from mediapipe.tasks.python import vision

#Hand Scroll
import pyautogui


pyautogui.FAILSAFE = True

MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          "hand_landmarker.task")


#Hands Scroll
def fingers_scroll(points):
    pairs = [(4, 2), (8, 6), (12, 10), (16, 14), (20, 18)] #Tip and it's joint
    return [points[tip].y < points[joint].y for tip, joint in pairs]

def scroll_gesture(fingers):
    return fingers == [True, True, True, True, True]


def scroll_amount(previous_y, current_y, threshold=0.02, speed=5500):
    if previous_y is None: 

        return 0

    difference = previous_y - current_y #This becomes positive when hand moves up

    if abs(difference) < threshold:
        return 0
    return int(difference * speed)

#Fingers Zoom
def fingers_zoom(points):
    pairs = [(4, 2), (8, 6), (12, 10), (16, 14), (20, 18)]
    return [points[tip].y < points[joint].y for tip, joint in pairs]

def zoom_gesture(fingers):
    return fingers == [True, True, False, False, False]

def zoom_amount(previous_y, current_y, threshold=0.02, speed=1500):
    if previous_y is None: 
        return 0

    difference = previous_y - current_y

    if abs(difference) < threshold:
            return 0
    return int(difference * speed)




class Project:


    #Opens Camera
    def open_camera(self):
        cam = cv2.VideoCapture(0)

        if not cam.isOpened():
            print("Camera didnt Open")
            return None

        return cam


    #Uses mediepipe modules and runs it 
    def create_landmark_mediapipe(self):
        base_options = mp_python.BaseOptions(
            model_asset_path="hand_landmarker.task"
        )

        options = vision.HandLandmarkerOptions(
            base_options=base_options,
            running_mode =vision.RunningMode.VIDEO,
            num_hands=2,
        )

        return vision.HandLandmarker.create_from_options(options)


    #Hand Tracking with time/fps and mediapipe
    def hand_tracking(self):

        cam = self.open_camera()

        if cam is None: 
            return

        landmark = self.create_landmark_mediapipe()
        last_frame_time = time.time()

        while True:
            ret, frame = cam.read()

            if not ret: 
                break


            image_color = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            this_frame_time = time.time()
            fps = 1 / (this_frame_time - last_frame_time)
            last_frame_time = this_frame_time

                #Recognize Hands
            recognize_hands = mp.Image(image_format=mp.ImageFormat.SRGB, 
                                       data=image_color)

            time_stamp = int(time.time() * 1000)

            result = landmark.detect_for_video(recognize_hands, time_stamp)

            #Recognize and draw dots for recognicition
            if result.hand_landmarks: 
                h, w, c = frame.shape
                for hand in result.hand_landmarks:
                    for point in hand:
                        x, y = int(point.x * w), int(point.y * h)
                        cv2.circle(frame, (x, y), 
                                   10, (255, 0, 255),
                                   cv2.FILLED)


            cv2.putText(frame, str(int(fps)), (10, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)


            #Scroll with hand
            scroll_mode = False 

            #Hands Zoom
            zoom_mode = False

            if result.hand_landmarks:
                points = result.hand_landmarks[0]
                scroll_mode = scroll_gesture(fingers_scroll(points))
                zoom_mode = zoom_gesture(fingers_zoom(points))

                if scroll_mode:
                    current_y = points[8].y
                    amount = scroll_amount(previous_scroll_y, current_y)

                    if amount != 0:
                        pyautogui.scroll(amount)

                    previous_scroll_y = current_y

                if zoom_mode:
                    current_y = points[4].y
                    amount = zoom_amount(previous_zoom_y, current_y)

                    if amount != 0:
                        with pyautogui.hold("ctrl"):
                            pyautogui.scroll(amount)

                    previous_zoom_y = current_y

            if scroll_mode:
                cv2.putText(frame, "SCROLL", (10, 80),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)


            else: 
                previous_scroll_y = None

            if zoom_mode: 
                cv2.putText(frame, "ZOOM", (10, 120),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            else: 
                previous_zoom_y = None



            
            cv2.imshow("CamOutput", frame)

            if cv2.waitKey(1) == ord("q"):
                break


        landmark.close()
        cam.release()
        cv2.destroyAllWindows()




def main():
    project = Project()
    project.hand_tracking()



if __name__ == "__main__":
    main()




