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

    def check_battery():
        pass;
    def upload():
        pass;
    def movement():
        pass;


if __name__ == "__main__":
    r = rover(None, None, None, None)
    r.get_velocity(50.0,50.05,20.0,70.0)