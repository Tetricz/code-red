from abc import abstractmethod
import os
import os.path

class data:


    def __init__(self,_date,_time,_lat,_long,_altitude,_battery_level):
        self.date = _date;
        self.time = _time;
        self.lat = _lat;
        self.long = _long;
        self.altitude = _altitude;
        self.batery_level = _battery_level;
    @abstractmethod
    def _debug_print():
        pass
    @abstractmethod
    def write_to(self,file_name):
        pass


