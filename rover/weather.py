from data import data
import os
import os.path

class weather(data):
    temp = None;
    humidity = None;
    atmospheric_pressure = None;
    visibility = None;
    wind_speed = None;
    def __init__(self,_date,_time,
                _lat,_long,_altitude,
                _battery_level,_temp,
                _humidity,_atmospheric_pressure,
                _visibility,_wind_speed):
        super().__init__(_date,_time,_lat,_long,_altitude,_battery_level)
        self.temp = _temp;
        self.humidity = _humidity;
        self.atmospheric_pressure = _atmospheric_pressure;
        self.visibility = _visibility;
        self.wind_speed = _wind_speed;
    def debug_print(self):
        print('DATE: ' , self.date)
        print('TIME: ' , self.time)
        print('LAT: ' , self.lat)
        print('LONG: ' , self.long)
        print('ALTITUDE: ' , self.altitude)
        print('TEMP: ' , self.temp)
        print('HUMIDITY: ' , self.humidity)
        print('ATMOSPHERIC_PRESSURE: ' , self.atmospheric_pressure)
        print('VISIBILITY: ' , self.visibility)
        print('WIND_SPEED: ' , self.wind_speed)

    def write_to(self,file_name):
      
        if not os.path.exists(file_name):
            file = open(file_name,'w')
        else:
            file = open(file_name,'a')
            file.write("weather:"
                +str(self.date)+','
                +str(self.time)+','
                +str(self.lat)+','
                +str(self.long)+','
                +str(self.batery_level)
                +str(self.temp)+','
                +str(self.humidity)
                +str(self.atmospheric_pressure)
                +str(self.visibility)
                +str(self.wind_speed)
                +'\n')





    
