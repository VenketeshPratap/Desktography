import cv2
import datetime as dt
import numpy as np
import pyautogui as pag
import pyrealsense2 as rs
import mediapipe as mp
from Contour import detect_rectangle_contour
from background_removal import perform_background_removal
from hand_tracking import perform_hand_tracking
from utility import convert_depth_to_distance, convert_distance_to_feet

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


# ====== Set clipping distance ======


# ====== Get and process images ====== 
print(f"Starting to capture images on SN: {device}")




# ====== Detect Screen Contour in Image ====== 
x,y,w,h = detect_rectangle_contour(frames, color_frame)

x_screen = x
w = w*3
y_screen = y
h = h*2.25

px, py = 0, 0

# ====== Get Background Image for future removal ====== 
for i in range(200):
#    ......
# ........