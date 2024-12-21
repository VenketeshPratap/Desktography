import cv2
import numpy as  np

def detect_rectangle_contour(frames, color_frame):
    if not color_frame:
        return

    # Convert the color frame to OpenCV format
    color_image = np.asanyarray(color_frame.get_data())

    # TODO: Perform projection mapping and obtain the projected rectangle

    # Detect the rectangle in the color image
   
    
    for contour in contours:
        # Filter out small contours
        if cv2.contourArea(contour) > 500:
            # TODO: Perform further processing to identify the rectangle if necessary
            x, y, w, h = cv2.boundingRect(contour)

            # Draw the rectangle with green borders
           

            # Print the coordinates of the corners
           

    # Display the color image with the projected rectangle
    cv2.imshow("RealSense", color_image)
    return x,y,w,h
