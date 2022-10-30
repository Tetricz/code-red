from genericpath import exists
from sys import maxsize
from telnetlib import STATUS
import queue
import csv
import os

class rover:
    def __init__(self,_id,_battery,_total_memory,_used_memory): #constructor
        self.id = _id;
        self.battery = _battery;
        self.total_memory = _total_memory;
        self.used_memory = _used_memory;
        self.status = 1;
        self.lat = 0
        self.long = 0
        self.q = queue.Queue(maxsize=10)


    
    def check_battery(self):
        if(self.battery <= 10):
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
            
    def create_file():
        pass;

    def dequeue(self):
        while self.q.qsize() != 0:
            print(self.q.get())
    def enqueue(self,job):
        self.q.put(job)

    def write(self,file_name):
        check = path_to_file = 'test.txt'
        if not check:
            file = open(file_name,'w')
            file.write('1')
        else:
            file = open(file_name,'a')
            file.write(str(self.id)+",\n")
            file.write(str(self.battery)+',\n')
            file.write(str(self.total_memory)+',\n')
            file.write(str(self.used_memory)+',\n')
            file.write(str(self.status)+',\n')
            file.write(str(self.lat)+',\n')
            file.write(str(self.long)+',\n')



    

    

        

        
            
        








