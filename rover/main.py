
import database_coms as dbcoms
from rover import rover
from video import video
from weather import weather

if __name__ == "__main__":
    db = dbcoms.DatabaseComs()
    r = rover(None, None, None, None)
    r.get_velocity(50.0,50.05,20.0,70.0)
    r.check_battery()

    r = rover(1,100,100,0);
    v = video(1,1,1,1,1,1,1,1,1)
    w = weather(1,1,1,1,1,1,1,1,1,1,1)
    r.write_to_ssd('ssd.txt',v)
    r.write_to_ssd('ssd.txt',w)
    
    db.close()
