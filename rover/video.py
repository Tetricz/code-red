from data import data
import random

class video(data):
    def __init__(self,_lat,_long,_battery_level,_vid_name,_size):
        super().__init__(_lat,_long,_battery_level)
        self.vid_name = str(self.datetime).replace(" ", "_") + ".mkv";
        self.size = 60 * random.randrange(40, 60)


if __name__ == "__main__":
    print("Hi :D")