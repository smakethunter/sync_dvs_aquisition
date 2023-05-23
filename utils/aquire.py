import cv2
import datetime
vid = cv2.VideoCapture(0)
  
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
  
    # Display the resulting frame
    cv2.imshow('frame', frame)
    print("writing frames")
    cv2.imwrite(f'/Users/smaket/PycharmProjects/sync_dvs_aquisition/tests/aquire_test/{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")}.png', frame)
  
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()