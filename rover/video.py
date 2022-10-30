from genericpath import exists
from sys import maxsize
from telnetlib import STATUS
import os
import os.path
from data import data
import random


class video(data):
    def __init__(self,_lat,_long,_battery_level,_vid_name,_size):
        super().__init__(_lat,_long,_battery_level)
        self.vid_name = str(self.datetime).replace(" ", "_") + ".mkv";
        self.size = 60 * random.randrange(40, 60)


    def write_to(self,file_name):
      
        if not os.path.exists(file_name):
            file = open(file_name,'w')
        else:
            file = open(file_name,'a')
            file.write("video:"
                +str(self.datetime)+','
                +str(self.lat)+','
                +str(self.long)+','
                +str(self.battery_level)
                +str(self.vid_name)+','
                +str(self.size)
                +'\n')
            
if __name__ == "__main__":
    print("Hi :D")
