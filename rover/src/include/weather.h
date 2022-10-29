#ifndef WEATHER_H
#define WEATHER_H
#include "data.h"
class weather: private data {
private:
    float temp;
    float humidity;
    float atomsphereic_pressure;
    int visibility;
    int wind_speed;
public:
    void debug_print()
    {
        std::cout << std::setw(20) << std::setfill('=') << std::endl;
        std::cout << "DATA_TYPE" << "WEATHER" << std::endl;
        std::cout << "DATE: " << date << std::endl;
        std::cout << "TIME: " << time << std::endl;
        // std::out << "INTERNET: " << internet.first() << " " << internet.first << std::endl;
        std::cout << "ALTITUDE: " << altitude << std::endl;
        std::cout << "BATERY LEVEL: " << battery_level << std::endl;

        std::cout << "TEMP: " <<  temp << std::endl;
        std::cout << "HUMIDITY: " << humidity << std::endl;
        std::cout << "ATMOSPHERE_PRESSURE: " << atomsphereic_pressure << std::endl;
        std::cout << "VISIBILITY: " << visibility << std::endl;
        std::cout << "WIND SPEED: " << wind_speed << std::endl;

    }
};
#endif