import cv2
import datetime
import time
from sys import platform

class ComvisRecord:
    source = ""
    fps = 10
    path = ""
    duration = 10
    timeFormat = "%d-%m-%Y %H:%M:%S" if platform == "linux" else "%d-%m-%Y %H%M%S"
    cap = cv2.VideoCapture(source)
    size = (int(cap.get(3)), int(cap.get(4)))
    
    def __init__(self, source):
        self.source = source
        self.cap = cv2.VideoCapture(self.source)
        self.size = (int(self.cap.get(3)), int(self.cap.get(4)))
    
    def __init__(self, source, fps):
        self.source = source
        self.fps = fps
        self.cap = cv2.VideoCapture(self.source)
        self.size = (int(self.cap.get(3)), int(self.cap.get(4)))
    
    def __init__(self, source, fps, path):
        self.source = source
        self.fps = fps
        self.path = path
        self.cap = cv2.VideoCapture(self.source)
        self.size = (int(self.cap.get(3)), int(self.cap.get(4)))
    
    def __init__(self, source, fps, path, duration):
        self.source = source
        self.fps = fps
        self.path = path
        self.duration = duration
        self.cap = cv2.VideoCapture(self.source)
        self.size = (int(self.cap.get(3)), int(self.cap.get(4)))
    
    def setSource(self, source):
        self.source = source
        self.cap = cv2.VideoCapture(self.source)
        self.size = (int(self.cap.get(3)), int(self.cap.get(4)))
    
    def setDuration(self, duration):
        self.duration = duration
    
    def setFPS(self, fps):
        self.fps = fps
    
    def setPath(self, path):
        self.path = path
    
    def createWriter(self,tanggal):
        return cv2.VideoWriter(
            "{}{}.avi".format(
                self.path,
                tanggal.strftime(self.timeFormat)
            ), 
            cv2.VideoWriter_fourcc(*'MJPG'), 
            self.fps, 
            self.size
        )
    
    def run(self):
        result = self.createWriter(datetime.datetime.now())
        start = time.time()
        
        while(self.cap.isOpened()):
            ret, frame = self.cap.read()
            
            if (time.time()-start) > self.duration:
                result.release()
                result = self.createWriter(datetime.datetime.now())
                start = time.time()
            else:
                result.write(frame)
    
    def stop(self):
        self.cap.release()
        cv2.destroyAllWindows()
        