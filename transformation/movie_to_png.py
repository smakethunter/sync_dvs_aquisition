import cv2
import datetime
filename = '2016_0101_191702_002.MP4'
fps = 60
video_start = datetime.datetime.strptime(filename.split('.')[0], '%Y_%m%d_%H%M%S_%f')
timestamp = video_start.timestamp()
vidcap = cv2.VideoCapture(filename)
success, image = vidcap.read()
count = 0
print(video_start)
print(timestamp)
while success:
  timestamp += 1 / fps
  cv2.imwrite(f"frames/{timestamp}.jpg", image)     # save frame as JPEG file
  success, image = vidcap.read()
  # print('Read a new frame: ', success)
