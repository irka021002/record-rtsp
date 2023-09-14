import cv2
import datetime
import time
import json

if __name__ == "__main__":
    with open("config.json", "r") as jsonfile:
        config = json.load(jsonfile)
    
    start = time.time()
    tanggal = datetime.datetime.now()
    cap = cv2.VideoCapture(config["videoSource"])
    size = (int(cap.get(3)), int(cap.get(4)))
    
    result = cv2.VideoWriter("{}{}.avi".format(config["filePath"],tanggal.strftime("%d-%m-%Y %H%M%S")), cv2.VideoWriter_fourcc(*'MJPG'), 10, size)
    
    while(cap.isOpened()):
        ret, frame = cap.read()
        
        if (time.time() - start) > config["duration"]:
            print("Video tersave")
            tanggal = datetime.datetime.now()
            result.release()
            result = cv2.VideoWriter("{}{}.avi".format(config["filePath"],tanggal.strftime("%d-%m-%Y %H%M%S")), cv2.VideoWriter_fourcc(*'MJPG'), 10, size)
            start = time.time()
        else:
            result.write(frame)
        
    cap.release()
    cv2.destroyAllWindows()