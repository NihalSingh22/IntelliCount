# Import the OpenCV library for computer vision tasks
import cv2
# Import the NumPy library for numerical operations (not used in this snippet but might be useful for further modifications)
import numpy as np

# Start capturing video from a video file named 'video.mp4'
video_capture = cv2.VideoCapture('video.mp4')

line_pos = 550
offset = 5      # allowable error between pixel
vehicleCounter = 0
min_width = 80
min_height = 80

#initialize Subtructor - subtracts the background from the video

algorithm = cv2.bgsegm.createBackgroundSubtractorMOG()


def center(x,y,w,h):
    x_1 = int(w/2)
    y_1 = int(h/2)
    computeX = x + x_1
    computeY = y + y_1

    return computeX , computeY

detectCounter = []



# Loop indefinitely (until the user presses the 'Enter' key)
while True:
    # Read a frame from the video
    ret, frame = video_capture.read()
    greyObj = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blurr = cv2.GaussianBlur(greyObj,(3,3),5)

    # each frame application
    image_sub = algorithm.apply(blurr)
    
    dilate = cv2.dilate(image_sub,np.ones((5,5)))

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))

    dilate_data = cv2.morphologyEx(dilate,cv2.MORPH_CLOSE,kernel)
    dilate_data = cv2.morphologyEx(dilate_data,cv2.MORPH_CLOSE,kernel)
    counter,h = cv2.findContours(dilate_data,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    cv2.line(frame,(25,line_pos),(1200,line_pos),(50,205,50),4)

    for (i,j) in enumerate(counter):
        x,y,w,h = cv2.boundingRect(j)
        validate = (w>=min_width) and (h>=min_height)
        if not validate:
            continue 

        cv2.rectangle(frame,(x,y), (x+w,y+h),(255,37,37),3)
        cv2.putText(frame,"Vehicle" + str(vehicleCounter), (x,y-20), cv2.FONT_HERSHEY_COMPLEX,2,(200,200,255),4)

        cent = center(x,y,w,h)

        detectCounter.append(cent)

        cv2.circle(frame,cent,5,(0,0,255),-1)

        for (x,y) in detectCounter:
            if y<(line_pos+offset) and y>(line_pos-offset):
                vehicleCounter +=1 

                cv2.line(frame,(25,line_pos),(1200,line_pos),(0,205,250),4)

                detectCounter.remove((x,y))

                print("Vehicle Counter - " + str(vehicleCounter))


    cv2.putText(frame,"Vehicle Counter : " + str(vehicleCounter), (450,70), cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),5)

    #cv2.imshow('Detector Video', dilate_data)

    # If frame reading was not successful, break from the loop
    if not ret:
        break

    # Display the current frame in a window named 'Original Video'
    cv2.imshow('Original Video', frame)

    # Wait for 1 millisecond and check if the 'Enter' key (key code 13) is pressed
    if cv2.waitKey(1) == 13:
        break

# Release the video capture object and close all OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
