import pyrealsense2 as rs
import mediapipe as mp
import cv2
import numpy as np
import datetime as dt
import pyautogui as pag
import subprocess
import webbrowser
import time
from app_gui import main

font = cv2.FONT_HERSHEY_SIMPLEX
org = (20, 100)
fontScale = .5
color = (0,50,255)
thickness = 1

# ====== Realsense ======
realsense_ctx = rs.context()
connected_devices = [] # List of serial numbers for present cameras
for i in range(len(realsense_ctx.devices)):
    detected_camera = realsense_ctx.devices[i].get_info(rs.camera_info.serial_number)
    print(f"{detected_camera}")
    connected_devices.append(detected_camera)
device = connected_devices[0] # In this example we are only using one camera
pipeline = rs.pipeline()
config = rs.config()
background_removed_color = 50 # Light Black

# ====== Mediapipe ======
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


# ====== Enable Streams ======
config.enable_device(device)

# # For worse FPS, but better resolution:
# stream_res_x = 1280
# stream_res_y = 720
# # For better FPS. but worse resolution:
stream_res_x = 640
stream_res_y = 480

stream_fps = 30

config.enable_stream(rs.stream.depth, stream_res_x, stream_res_y, rs.format.z16, stream_fps)
config.enable_stream(rs.stream.color, stream_res_x, stream_res_y, rs.format.bgr8, stream_fps)
profile = pipeline.start(config)

align_to = rs.stream.color
align = rs.align(align_to)

# ====== Get depth Scale ======
depth_sensor = profile.get_device().first_depth_sensor()
depth_scale = depth_sensor.get_depth_scale()
print(f"\tDepth Scale for Camera SN {device} is: {depth_scale}")

# ====== Set clipping distance ======
clipping_distance_in_meters = 100
clipping_distance = clipping_distance_in_meters / depth_scale
print(f"\tConfiguration Successful for SN {device}")

# ====== Get and process images ====== 
print(f"Starting to capture images on SN: {device}")





x,y,w,h = 0,0,0,0
#Open White Screen for edge detection
url = 'https://www.ledr.com/colours/white.htm'
webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
webbrowser.get('chrome').open(url)
time.sleep(0.5)
pag.press('f11')

for i in range(100):
    # Wait for a new frame from the RealSense camera
    frames = ....
    color_frame = .....
    if not color_frame:
        continue

    # Convert the color frame to OpenCV format
    color_image = .....
    # Detect the rectangle in the color image
    gray = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        # Filter out small contours
        if cv2.contourArea(contour) > 500:
            # TODO: Perform further processing to identify the rectangle if necessary
            x, y, w, h =.....

            # Draw the rectangle with green borders
            cv2.rectangle(color_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Print the coordinates of the corners
            print("Coordinates of the corners:")
            print(f"Top-left: ({x}, {y})")
            print(f"Top-right: ({x + w}, {y})")
            print(f"Bottom-left: ({x}, {y + h})")
            print(f"Bottom-right: ({x + w}, {y + h})")

    # Display the color image with the projected rectangle
    cv2.imshow("RealSense", color_image)

    # Exit the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


x_screen = x
w = w*3
y_screen = y
h = h*2.25

px, py = 0, 0

#background detection
for i in range(200):
    frames_bg = ....
    aligned_frames_bg = .....
    aligned_depth_frame_bg =.....
    color_frame_bg = .....

pag.press('f11')
pag.hotkey('ctrl', 'w')

# Process images
depth_image_bg = ....
depth_image_flipped_bg = ....
color_image_bg = ....

depth_image_bg_3d = np.dstack((depth_image_bg,depth_image_bg,depth_image_bg)) #Depth image is 1 channel, while color image is 3

while True:
    start_time = dt.datetime.today().timestamp()

    # Get and align frames
    frames = ....
    aligned_frames = ....
    aligned_depth_frame = ....
    color_frame = ....
    
    if not aligned_depth_frame or not color_frame:
        continue

    # Process images
         depth_image_bg = ....
         depth_image_flipped_bg = ....
         color_image_bg = ....


    depth_image_3d = np.dstack((depth_image,depth_image,depth_image)) #Depth image is 1 channel, while color image is 3
    
    
    
    
    depth_diff = np.abs(depth_image_bg.astype(float) - depth_image.astype(float))
    maximum = 0
    for i in range(10):
        for j in range(10):
            if maximum < depth_diff[i][j]: 
                maximum = depth_diff[i][j] 
        #print("\n")
    distance_threshold = maximum  * 2  # Adjust this threshold as needed
    background_mask = np.where(depth_diff < distance_threshold, 0, 255).astype(np.uint8)
    # Apply the background mask to the color image
    background_removed = cv2.bitwise_and(color_image, color_image, mask=background_mask)
    
    
    
    
    depth_colormap = cv2.applyColorMap(....)

    images = cv2.flip(background_removed,1)
    color_image = cv2.flip(color_image,1)
    color_images_rgb = cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB)

    # Process hands
    results = hands.process(color_images_rgb)
    if results.multi_hand_landmarks:
        number_of_hands = len(results.multi_hand_landmarks)
        i=0
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(images, handLms, mpHands.HAND_CONNECTIONS)
            org2 = (20, org[1]+(20*(i+1)))
            hand_side_classification_list = results.multi_handedness[i]
            hand_side = hand_side_classification_list.classification[0].label
            index_finger_tip = results.multi_hand_landmarks[i].landmark[8]
            
            x = int(index_finger_tip.x*len(depth_image_flipped[0]))
            y = int(index_finger_tip.y*len(depth_image_flipped))
            if x >= len(depth_image_flipped[0]):
                x = ....
            if y >= len(depth_image_flipped):
                y = ....
            ift_distance =.....# meters
            screen_distance = ..... * ......
            ift_distance_feet = ..... * 3.281 # feet
            images = cv2.putText(images, f"Screen Distance: {screen_distance:0.3} m  Hand Distance: ({ift_distance:0.3} m) away", org2, font, fontScale, color, thickness, cv2.LINE_AA)
            
            #mapping
            actual_x, actual_y = 0,0
            if index_finger_tip.x * 1920 > x and index_finger_tip.x * 1920 < x + w and index_finger_tip.y * 1080 > y and index_finger_tip.y * 1080 < y + h:
                actual_x = int(((....)*1920 - ....*3) *1920 / w) 
                actual_y = int(((....)*1080 - ....*2.25) *1080 / h)
                print("Hi ", (1-index_finger_tip.x)*1920, (index_finger_tip.y)*1080)
                print("check ", x_screen*3, y_screen*2.25)
                print("Actual ", actual_x, actual_y)
            if actual_x > 0 and actual_x < 1920 and actual_y > 0 and actual_y < 1080:
                if abs(screen_distance - ift_distance) < 0.3 :

                    #gestures
                    thumb_tip = ....
                    index_tip = ....
                    distance = np.sqrt((....)*2 + (.....)*2)

                    # if distance < 0.1:
                    #     main()
                    # elif distance < 0.2:
                    #     print("Thumbs")


                    if abs(screen_distance - ift_distance) < 0.3:
                        
                        #click
                        if(hand_side == "Right"):
                            pag.click(actual_x, actual_y)
                            print(f"Screen Distance: {screen_distance:0.3} m  Hand Distance: ({ift_distance:0.3}")
                            print("Click")
                           # time.sleep(0.3)

                        # drag
                        elif(hand_side == "Left"):
                            if px == 0 and py == 0:
                                px,py = actual_x, actual_y
                                print("Calibrate kr rha hu")
                            else:
                                pag.mouseDown(px, py, button='left')
                                pag.moveTo(actual_x, actual_y)
                                pag.mouseUp()
                                print("Drag kr rha hu me")
                                print(f"Screen Distance: {screen_distance:0.3} m  Hand Distance: ({ift_distance:0.3}")
                    pag.moveTo(actual_x, actual_y)
                    print("Close")
                else :
                    print("Far Away")
            else:
                print("Hi ", (1-index_finger_tip.x)*1920, (index_finger_tip.y)*1080)
                print("check ", x_screen*3, y_screen*2.25)
                print("Outside Screen")
            i+=1
            px,py = actual_x, actual_y
        images = cv2.putText(images, f"Hands: {number_of_hands}", org, font, fontScale, color, thickness, cv2.LINE_AA)

    else:
        images = cv2.putText(images,"No Hands", org, font, fontScale, color, thickness, cv2.LINE_AA)


    # Display FPS
    time_diff = dt.datetime.today().timestamp() - start_time
    fps = int(1 / time_diff)
    org3 = (20, org[1] + 60)
    images = cv2.putText(images, f"FPS: {fps}", org3, font, fontScale, color, thickness, cv2.LINE_AA)

    name_of_window = 'SN: ' + str(device)

    # Display images 
    cv2.namedWindow(name_of_window, cv2.WINDOW_AUTOSIZE)
    cv2.imshow(name_of_window, images)
    key = cv2.waitKey(1)
    # Press esc or 'q' to close the image window
    if key & 0xFF == ord('q') or key == 27:
        print(f"User pressed break key for SN: {device}")
        break

print(f"Application Closing")
pipeline.stop()
print(f"Application Closed.")