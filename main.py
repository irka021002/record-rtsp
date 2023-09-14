import ComvisRecorder
import json

if __name__ == "__main__":
    with open("config.json", "r") as jsonfile:
        config = json.load(jsonfile)
    
    recorder = ComvisRecorder(config["source"],config["fps"],config["path"],config["duration"])
    
    recorder.run()
    
    