
import database_coms as dbcoms
import xml.etree.ElementTree as ET
from rover import rover
import time
import os

if __name__ == "__main__":
    #db = dbcoms.DatabaseComs()
    #db.seedDatabase()

    r = rover(1,100,100,0);
    # r.dequeue()
    # i = 0;
    # while True:
    #     print(i)
    #     time.sleep(1)
    #     i+=1
    list = [1,2,3,4,5,6,7]
    r.write('test.txt')



    