#ifndef ROVER_H
#define ROVER_H

#define GB 1
#define MB 0.001
#define KB 0.000001

#include<iostream>



class rover {
private:
    std::string name;
    float battery;
    float total_memory; // 1 = 1 gb // 1.24 = 1 gig + 240 mb
    float used_memory;  


public:
    rover(std::string _name, float _batter, float _total_mem, float _mem_used) {
        name         = _name;
        battery      = _batter;
        total_memory = _total_mem;
        used_memory  = _mem_used;
    }

};
#endif