from data import data

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



a = weather(1,1,1,1,1,1,1,1,1,1,1);
a.debug_print();