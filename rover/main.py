
import database_coms as dbcoms
from rover import rover
import time
import os

if __name__ == "__main__":
    db = dbcoms.DatabaseComs()
    r = rover(None, None, None, None)
    r.get_velocity(50.0,50.05,20.0,70.0)
    r.check_battery()

    db.close()

