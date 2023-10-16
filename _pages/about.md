---
permalink: /
title: "Water: Paralympics in the Canals of Amsterdam"
excerpt: "About"
author_profile: true
toc: true
redirect_from: 
  - /about/
  - /about.html
---

Paris is hosting the Paralympics in 2024. One of the events at the Paralympics is an open water swimming event in the Seine (apparently the water is clean or so the French say). Since the City of Amsterdam thinks it is better than Paris, they want to host an event before the Paralympics, snubbing the Parisians. The idea is to host a 5km. open water swimming event through the canals of Amsterdam. You are asked by the municipality of Amsterdam to advise on the feasibility of the event from the perspective of the safety of the partaking athletes from an environmental perspective. The event is going to be hosted in May.

Assignment 1 - Paralympics
------
* The event can’t have an impact on commercial water transport.
* It would be appreciated if the event also has small impact on the routes of the canal boats.
* What is the pollution level of the canals and is there data from all the canals? You can swim next to the AMS but the water there is heavily monitored, is this the same for the rest of Amsterdam?
* Think of a few data sets that are of use for giving a proper advice to the municipality.
* What type of data format is the information you found stored in? Are they Excel files, csv files or some other format? Try to open the files and see if they are human readable (e.g., are they text files or binary – in this case you see a lot of weird characters).
* Is the data stored numerical?
* You know how to read simple text files and a csv file from the first workshop. If you find other data formats, try to find a suitable Python library that can read that format.
* If you have geospatial data, can you figure out how the data is geometrically represented (points, lines, surfaces, hyperplanes)?
* If it is temporal data, what is the interval?

Assignment 2 - TourBoats
------
The Municipality is worried that the canal- and support boats might pollute the air with their diesel engines. Since the Municipality wants to create ideal conditions for the swimmers so they can set records (always nice for PR), it is your task to figure out if their concern is warranted and what should or could be done to improve conditions. Next to that, Amsterdam 
wants to advertise this event as a Neutral Energy Event©™® (NEE).

* How many of the canal boats currently in use are diesel/fossil fuel driven and how many boats are electrical driven?
* Are there peak times for the canal boats? 
* Try to compare the energy use of the canal boats to some other activities in the city. Use canal boats more or less energy in relation to their carbon footprint compared to these other activities?
* Would you consider it economically feasible?
* How many support boats and vehicles are needed for the Paralympics event only.
* If only clean energy can be used, how many solar panels or wind turbines are needed?
* Is it possible to accommodate these facilities within the city?
* Would their be any effect on the water quality if there are less/no canal boats using fossil fules?

Assignment 3 - Housing
------
For this exercise you need the data from [this website](https://data.amsterdam.nl/datasets/rl6-35tFAw2Ljw/basisbestand-gebieden-amsterdam-bbga/). Download the Basis Bestand Gebieden Amsterdam (BBGA), both the data and the documentation. You already have the AirBnB data from Amsterdam from the workshop exercise.

The Municipality of Amsterdam is in a love hate relationship with AirBnb, see for example [this](https://thenextweb.com/news/four-months-after-its-hunt-for-illegal-hotels-amsterdam-lightens-restrictions-on-airbnb-rentals) and [this](https://www.theguardian.com/travel/2020/sep/14/airbnb-appeals-to-dutch-high-court-retain-double-fees) article. Amsterdam wants to get a bit of insight in the number of tourists that will make use of AirBnB. Can you advise on or calculate for Amsterdam:

* What Amsterdam will receive from tourist tax if the event lasts a week and you will have 30.000 visitors?
* Plot the amount of AirBnB locations per neighbourhood.
* Which street in Amsterdam has the most AirBnB apartments?
* Try to cross reference the data from the AirBnB dataset with the BBGA. Can you figure out if all apartments of AirBnB are designated as housing? Which number of apartments are not rented out all the time but are also used as normal housing?
* How many hotel rooms should be built if Amsterdam wants to accommodate the same number of tourists?
* How many different licenses are issued?

Assignment 4 - Transport
------
For this exercise you have chosen a route in Amsterdam for the canal swimming event. Preferably you have this route calculated using Python. You can set a start point and an end point and then try to find a route that has a certain distance (min. 5 km.)

The Municipality wants you to find a location for the Event Headquarters. They decided it would be best if this E.H. is as close to the centre of the swimming route. There is a bit of a concern for the after party and the stream of visitors. They want you to quantify the number of visitors that can reach the event and the capacity for festivities after the event.

* Find the centre of the nodes of the swimming route. [See this link](https://stackoverflow.com/questions/46238813/osmnx-get-coordinates-of-nodes-using-osm-id).
* Use the centre to find a suitable spot for the Event Headquarters.
* Find the closest bus and tram stops at the start and finish of the swimming route. How many people can be transported within an hour.
* Can you find which bus and tram lines these are, and can you find their routes?
* Calculate the centrality of the start, finish, and centre node of the route. Which centrality calculation makes the most sense. [See this link](https://networkx.org/documentation/stable/reference/algorithms/centrality.html).
* Find all cafes, restaurants near the finish line. Walking time smaller than 10 minutes.
