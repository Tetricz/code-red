from genericpath import exists
from random import randrange
from sys import maxsize
from telnetlib import STATUS
import queue
import csv
import os
import random
from video import video
import os.path
from data import data


class rover:
    def __init__(self,_id,_battery,_total_memory,_used_memory): #constructor
        self.id = _id
        self.battery = _battery
        self.total_memory = _total_memory
        self.used_memory = _used_memory

    def get_velocity(self, x1, y1, x2, y2):
        x = x1 - x2
        y = y1 - y2
        direction = (y/x)
        return direction

    def check_battery(self):
        if(self.battery <= 10.0):
            self.status = 5
    def upload():
        pass;
    def movement(self):
        if(self.status == 1):
            pass
        elif(self.status == 2):
            pass
        elif(self.status == 3):
            pass
        elif(self.status == 4):
            pass
        elif(self.status == 5):
            pass

    def dequeue(self):
        while self.q.qsize() != 0:
            print(self.q.get())
    def enqueue(self,job):
        self.q.put(job)

    def write(self,file_name):
      
        if not os.path.exists(file_name):
            file = open(file_name,'w')
        else:
            file = open(file_name,'a')

        file.write(str(self.id)+",\n")
        file.write(str(self.battery)+',\n')
        file.write(str(self.total_memory)+',\n')
        file.write(str(self.used_memory)+',\n')
        file.write(str(self.status)+',\n')
        file.write(str(self.lat)+',\n')
        file.write(str(self.long)+',\n')



    def write_to_ssd(self,file_name,data_type):
        check = os.path.exists('ssd.txt')
        if not check:
            file = open(file_name,'w')
        else:
            file = open(file_name,'a')
            
        data_type.write_to(file_name)

    def set_storage(self):
        self.used_memory = random.randrange(0, 15000)
    
    def check_storage(self):
        self.set_storage()
        return self.used_memory

        
        
        



if __name__ == "__main__":
    v = video(0,0,100,"name",80.0)
    v.debug()

    

    

        

        
            
        








