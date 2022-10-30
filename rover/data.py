from abc import abstractmethod
from datetime import datetime

class data:

    _datetime      = None;
    _lat           = None;
    _long          = None;
    _battery_level = None;

    def __init__(self,_lat,_long,_battery_level):
        self.datetime = datetime.now();
        self.lat = _lat;
        self.long = _long;
        self.battery_level = _battery_level;
    @abstractmethod
    def _debug_print():
        pass


if __name__ == "__main__":
    print("Hi :D")