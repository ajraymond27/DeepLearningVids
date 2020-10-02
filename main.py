import cv2


video = cv2.VideoCapture('SampleVideo_1280x720_10mb.mp4')
success,image = video.read()
count = 0

while success:
    cv2.imwrite("frame%d.jpg" % count, image)
    success,image = video.read()
    print('Read frame: ', success)
    count +=1

