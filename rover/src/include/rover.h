#ifndef ROVER_H
#define ROVER_H
#include<iostream>



class rover {
private:
    std::string name;
    float battery;
    float total_memory;
    float memory_used;

public:
    rover(std::string _name, float _batter, float _total_mem, float _mem_used) {
        name         = _name;
        battery      = _batter;
        total_memory = _total_mem;
        memory_used  = _mem_used;
    }
};
#endif