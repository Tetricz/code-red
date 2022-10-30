# CodeRed

## Team Rand() LyondellBasell Challenge

The team made an attempt at all the different issues. 

We used SQL databases with data entry/retrieval with python. 
The web server is hosted on flask, a micro web dev python platform.
The webpage is developed using HTML, CSS, and javascript.

The original object of the project was to make an interactive webpage that displayed both the personal and rover pov. 

The rover's pov would contain an interactive map that would update in real-time as a perspective of rover movement. The rover's page would also contain the current sensor reading for the rover along with storage and battery power. 

The personal's pov, which was decided to just error out, was to show the last location of the rover known and the endpoint of the rover.

The past routes would have given searchable filters for the data. The rover's uploaded information would become a new entry point in the past routes.
------------------

## Challenege: LyondellBasell
------------------
Don't run out of Resources!

LYB's team has encountered a few issues when developing Field Applications for Autonomous and Personal Devices off-world!  
Do you have what it take to accompany them in hteir oddyssey and help these Devices find their way back home?

* Coordinates: 23.42, 34.56
* Power: 26%
* Available Storage: 56%
* Wi-Fi Availability: None

HD Video will be recorded, since internet connectivity will be sparse, we need to make sure our devices are able to go back to a zone to replenish our resources. Give multiple solutions to the problems.

In Discord or booth to ask questions and get more information.

### Pros

Create an application personalizes and/or optimizes the ecommerce shopping experience of a consumer.

Examples:

A mobile application that allows a consumer to provide a picture of an item and ir performs a search to find similar items at retail locations and highlights the best price.

### Side Quests
------------------

* Best UI
* Best Beginner hack
* Best Use of Cloud
* Most Sustainable

### Sub Challenges
------------------
### Issue 1
Implement a mechanism to prevent Devices from running out of space while recording Field Events during Field Activities – such as detecting the rate in which the space is consumed by a Field Application and directing Autonomous or Personal Devices to the nearest Internet Availability Zone before the Device runs out of space.

### Issue 2
Implement a mechanism to prevent Devices from running out of battery while recording Field Events during Field Activities – such as detecting the rate in which battery is being depleted at during the usage of a Field Application and directing Autonomous or Personal Devices to the nearest Charging Station before the Device runs out of battery.

### Issue 3
Implement a mechanism that would allow Devices to use an offline copy of a map so Devices can be directed to the nearest Replenish Zone to replenish Space or Power. This mechanism should also record updates to the map so they can be later applied to the centralized map version.


### Hints
------------------
### Issue 1 & 2
1. Assume Devices are Andriod and use Andrio API
2. Implent Space/Power depletion Autonomous Device instructions to head to the suggested location or by implementing an activity for Personnel to be notified and get directions to head to a suggested location.
3.Personal may need nudge to follow path,  they should but a nudge is good.

### Issue 3
1. implement or mock and focus on solving other issues such as Issues One and Two
2. wouldn’t need any Dependency Injection, this simplifies implementing any solutions for it.
3. Devices to be Android based and use Android’s APIs to keep track of the Device’s location and the availability of internet connectivity.
------------------


