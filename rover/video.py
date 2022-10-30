from genericpath import exists
from sys import maxsize
from telnetlib import STATUS
import os
import os.path
from data import data


class video(data):
    def __init__(self,_date,_time,_lat,_long,_altitude,_battery_level,_vid_name,_vid_data,_size):
        super().__init__(_date,_time,_lat,_long,_altitude,_battery_level)
        self.vid_name = _vid_name;
        self.vid_data = _vid_data;
        self.size = _size;

    def write_to(self,file_name):
      
        if not os.path.exists(file_name):
            file = open(file_name,'w')
        else:
            file = open(file_name,'a')
            file.write("video:"
                +str(self.date)+','
                +str(self.time)+','
                +str(self.lat)+','
                +str(self.long)+','
                +str(self.batery_level)
                +str(self.vid_name)+','
                +str(self.size)
                +'\n')
            

