# Requirements

## Data collection

* Weather events
* Internet availability switching on or off
* Geographical events

## Rover design assumptions

* OS and Applications are stored on own memory
* Seperate data storage for collections

### Mem Emulation

Contructor:

* Rover Name/ID
* Set Total Memory (Arbitrary based on the storage in the machine)
* Set Free Memory (Available for data collection) Fill only to 90%, leave 10% for overfill protection

#### General Collection

* Date and Time
* Location
* Internet Connectivity
* Battery Level

#### Video Recorder

* HD Video
* Relatively high bitrate (10-20mb/s)

#### Weather events data

* Temp
* Humidity
* Atmosphere Pressure
* Daylight
* Wind speed

#### Geographical events

* Altitude
* Ravines
* Cliffs
* Hills
* Craters

These are barriers. A box grid that highlights an area of the map
