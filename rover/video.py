from data import data

class video(data):
    def __init__(self,_date,_time,_lat,_long,_altitude,_battery_level,_vid_name,_vid_data,_size):
        super().__init__(_date,_time,_lat,_long,_altitude,_battery_level)
        self.vid_name = _vid_name;
        self.vid_data = _vid_data;
        self.size = _size;