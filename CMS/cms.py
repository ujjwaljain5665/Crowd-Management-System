from mylib.centroidtracker import CentroidTracker
from mylib.trackableobject import TrackableObject
import numpy as np
import argparse
import imutils
import dlib
import cv2

import pygame
from pygame.locals import *
from pygame import mixer
pygame.init()
mixer.init()

def playsound():
    mixer.music.load("D:/CODES/Projects/Python/MAJOR/CMS/sound.wav")
    mixer.music.play()

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--prototxt", required=False,
                help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", required=True,
                help="path to Caffe pre-trained model")
ap.add_argument("-i", "--input", type=str,
                help="path to optional input video file")
ap.add_argument("-o", "--output", type=str,
                help="path to optional output video file")
# confidence default 0.4
ap.add_argument("-c", "--confidence", type=float, default=0.4,
                help="minimum probability to filter weak detections")
ap.add_argument("-s", "--skip-frames", type=int, default=30,
                help="# of skip frames between detections")
args = vars(ap.parse_args())
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
             "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
             "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
               "sofa", "train", "tvmonitor"]
net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])
ct = CentroidTracker(maxDisappeared=40, maxDistance=50)
Threshold=8
capacity="Max Capacity "+str(Threshold)
trackers = []
trackableObjects1 = {}
trackableObjects2 = {}
status = "No Space Available"
totalFrames = 0
totalDown = 0
totalUp = 0
x = []
empty = []
empty1 = []
flag=False

cam1=cv2.VideoCapture('D:/CODES/Projects/Python/MAJOR/CMS/videos/video.mp4')
cam2=cv2.VideoCapture('D:/CODES/Projects/Python/MAJOR/CMS/videos/video.mp4')

def function(frame,trackableObjects,rgb):
    W = None
    H = None
    global trackers
    global totalFrames
    global totalDown
    global totalUp
    global empty 
    global empty1
    
    if W is None or H is None:
        (H, W) = frame.shape[:2]
        
    rects = []
    if totalFrames % args["skip_frames"] == 0:
        trackers = []
        
        blob = cv2.dnn.blobFromImage(frame, 0.007843, (W, H), 127.5)
        net.setInput(blob)
        detections = net.forward()

        for i in np.arange(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > args["confidence"]:
                idx = int(detections[0, 0, i, 1])
                if CLASSES[idx] != "person":
                    continue
                box = detections[0, 0, i, 3:7] * np.array([W, H, W, H])
                (startX, startY, endX, endY) = box.astype("int")
                tracker = dlib.correlation_tracker()
                rect = dlib.rectangle(startX, startY, endX, endY)
                tracker.start_track(rgb, rect)
                trackers.append(tracker)
    else:
        for tracker in trackers:
            tracker.update(rgb)
            pos = tracker.get_position()
            startX = int(pos.left())
            startY = int(pos.top())
            endX = int(pos.right())
            endY = int(pos.bottom())
            rects.append((startX, startY, endX, endY))
    cv2.line(frame, (0, H // 2), (W, H // 2), (0, 0, 0), 3)
    objects = ct.update(rects)
    
    for (objectID, centroid) in objects.items():
        to = trackableObjects.get(objectID, None)
        if to is None:
            to = TrackableObject(objectID, centroid)
        else:
            y = [c[1] for c in to.centroids]
            direction = centroid[1] - np.mean(y)
            to.centroids.append(centroid)
            if not to.counted:
                if direction < 0 and centroid[1] < H // 2:
                    totalUp += 1
                    empty.append(1)
                    to.counted = True
                elif direction > 0 and centroid[1] > H // 2:
                    totalDown += 1
                    empty1.append(1)
                    to.counted = True
        trackableObjects[objectID] = to
        


def Crowd():
    global totalFrames
    while True:
        ret1,frame1=cam1.read()
        ret2,frame2=cam2.read()
    
        if ret1==True:
            frame1 = imutils.resize(frame1, width = 500)
            rgb1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
            function(frame1,trackableObjects1,rgb1)
        else:
            frame1=cv2.imread("D:/CODES/Projects/Python/MAJOR/CMS/Images/image.jpg")
            frame1=cv2.resize(frame1,(300,300))
            mixer.music.stop()
        
        if ret2==True:
            frame2 = imutils.resize(frame2, width = 500)
            rgb2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)
            function(frame2,trackableObjects2,rgb2)
        else:
            frame2=cv2.imread("D:/CODES/Projects/Python/MAJOR/CMS/Images/image.jpg")
            frame2=cv2.resize(frame2,(300,300))
            mixer.music.stop()
        
    
        # x=abs(totalUp-totalDown)
        x=abs(len(empty1)-len(empty))
        if abs(len(empty1)-len(empty)) >= Threshold:
            status="No Space Available"
        else:
            status="Space Available"

        info = [
	    	("Exit", len(empty)),
	    	("Enter", len(empty1)),
	    	("Status", status),
	    	]
        info2 = [
	    ("Total people inside", x),
	    ]
        
        if status=="No Space Available":
            if flag==False:
                playsound()
                flag=True
        else:
            flag=False
            mixer.music.stop()
    
        result=cv2.imread("D:/CODES/Projects/Python/MAJOR/CMS/Images/bg.jpg")
        result = cv2.resize(result,(500,300))
        for (i, (k, v)) in enumerate(info):
            text = "{}: {}".format(k, v)
            cv2.putText(result, text, (10, 300 - ((i * 100) + 20)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        
        for (i, (k, v)) in enumerate(info2):
            text = "{}: {}".format(k, v)
            cv2.putText(result, text, (265, 300 - ((i * 100) + 60)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
		
        cv2.putText(result, capacity, (265, 330 - ((i * 100) + 60)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        
        rframe=cv2.hconcat([frame1,frame2])
        cv2.imshow("CMS", rframe)
        cv2.imshow("Result", result)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
        totalFrames += 1
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    Crowd()
    pygame.quit()