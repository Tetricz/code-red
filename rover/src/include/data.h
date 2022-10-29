#ifndef DATA_H
#define DATA_H
#include<iostream>
#include<utility>
#include<iomanip>

class data {
protected:
    std::string date;
    std::string time;
    std::pair<bool,std::string> internet;
    std::string location;
    float altitude;
    float battery_level;
    virtual void debug_print() = 0;
};

#endif