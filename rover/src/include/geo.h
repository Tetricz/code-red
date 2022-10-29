#ifndef GEO_H
#define GEO_H
#include"data.h"

class geo: private data {
private:
    std::string event_type;
public:
    void debug_print()
    {
        std::cout << std::setw(20) << std::setfill('=') << std::endl;
        std::cout << "DATA_TYPE: " << "GEOGRAPHICAL" << std::endl;
        std::cout << "DATE: " << date << std::endl;
        std::cout << "TIME: " << time << std::endl;
        std::cout << "INTERNET: " << internet.first() << " " << internet.first << std::endl;
        std::cout << "ALTITUDE: " << altitude << std::endl;
        std::cout << "BATERY LEVEL: " << battery_level << std::endl;
        std::cout << "EVENT_TYPE: " << event_type << std::endl;
    }
};  
#endif
