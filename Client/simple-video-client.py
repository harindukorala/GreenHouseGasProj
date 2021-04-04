# import required libraries
from vidgear.gears import VideoGear
from vidgear.gears import WriteGear
from vidgear.gears import CamGear
import cv2
from datetime import datetime
import time

# configure options
options = {"CAP_PROP_FRAME_WIDTH":1280, "CAP_PROP_FRAME_HEIGHT":720, "CAP_PROP_FPS":25}
stream = CamGear(source=0, logging=True, **options).start() 

# sleep the camera 
time.sleep(2.0) 

#Construct the name for the video file 
output_params = {"-fourcc": "MJPG", "-fps": 25}
dt = datetime.now()
filename = '{}-{}-{}-{}-{}-{}.avi'.format(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, **output_params)

# Define writer with Non-compression mode and suitable output filename for e.g. `Output.mp4`
writer = WriteGear(output_filename = filename, compression_mode=False) 

# loop over
while True:

    # read frames from stream
    frame = stream.read()

    # check for frame if Nonetype
    if frame is None:
        break

    #New code for insering a timestamp for each frame
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,str(datetime.now()),(10,30), font, 1,(255,255,255),2,cv2.LINE_AA)
    
    # write frame to writer
    writer.write(frame)
    
    # Show output window
    cv2.imshow("Output Frame", frame)

    # check for 'q' key if pressed #Change wait key to 9 
    key = cv2.waitKey(9) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close video stream
stream.stop()

# safely close writer
writer.close()