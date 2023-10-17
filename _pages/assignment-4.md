---
layout: archive
title: "Amsterdam Transport"
permalink: /assignment-4/
author_profile: true
---

### 1.Find the centre of the nodes of the swimming route. [See this link](https://stackoverflow.com/questions/46238813/osmnx-get-coordinates-of-nodes-using-osm-id).

First, we selected the starting and ending points for our route, which were AMS Institute and the Rijksmuseum, respectively. We then identified the nearest points on the Amsterdam canals corresponding to these two locations. 

```ruby
ox.config(use_cache=True, log_console=True) 
city = ox.graph_from_place('Amsterdam', retain_all=False, truncate_by_edge=False, 
                        simplify=True, custom_filter='["waterway"~"canal"]') 
#print(city.nodes) 
#fig, ax = ox.plot.plot_graph(city) 
location = ox.geocode("Kattenburgerstraat 5, Amsterdam, Netherlands") 
location_to = ox.geocode("Museumstraat 1, Amsterdam, Netherlands") 
nodes = ox.distance.nearest_nodes(city, location[1], location[0], return_dist=True) 
nodes_to = ox.distance.nearest_nodes(city, location_to[1], location_to[0], return_dist=True) 
path = ox.shortest_path(city, nodes[0], nodes_to[0]) 
print(path) 
pt = ox.graph_to_gdfs(city, edges=False).unary_union.centroid 
bbox = ox.utils_geo.bbox_from_point(location, dist=5000) 
fig, ax = ox.plot_graph_route(city, path, bbox=bbox, show=False, close=False) 
```

Using these two points, we plotted the shortest path, which became the course for our activity. The path is shown in Figure 1 (luckily it's over 5 km). Combining the knowledge from Assignments 1 and 2, we chose a route that avoided areas of poor water quality and was therefore a good choice.

![Route](/images/Figure_1.png) <p style="text-align: center;"> <span style="color:grey"> $\small (Figure 1, The Swimming Route)$ </span> </p>

In Figure 1, the final chosen route is depicted in red, while other waterways and nodes are shown in white. 

$$Alt_{centre} = \frac{\sum_{i=1}^{n}{Alt_{node}}}{n}$$

$$Lat_{centre} = \frac{\sum_{i=1}^{n}{Lat_{node}}}{n}$$

```ruby
lat = 0 
lon = 0 
for points in path: 
    lat += city.nodes[points]['x'] 
    lon += city.nodes[points]['y'] 
lat_center = lat / len(path) 
lon_center = lon / len(path) 
center_point = (lon_center, lat_center) 
print(center_point) 
ax.scatter(lon_center, lat_center, c='blue') 
plt.show()
```

When calculating the centre point, we added the coordinates of all points along the track and divided the sum by the number of points. This calculation yielded the corrected coordinates of the centre point, (52.36604662, 4.9001779899999995). The central point was then plotted on the map, as illustrated in Figure 2. 

![Spot](/images/Figure_2.png) <p style="text-align: center;"> <span style="color:grey"> $\small (Figure 2, The Centre Point)$ </span> </p>

### 2.Use the centre to find a suitable spot for the Event Headquarters.

```ruby
city_whole = (ox.graph_from_place('Amsterdam, Netherlands', simplify=True)) 
nodes_centre = ox.distance.nearest_nodes(city_whole, center_point[1], center_point[0], return_dist=True) 
pt = ox.graph_to_gdfs(city, edges=False).unary_union.centroid 
bbox = ox.utils_geo.bbox_from_point(center_point, dist=5000) 
fig, ax1 = ox.plot_graph(city_whole, bbox=bbox, show=True, close= False) 
ax1.scatter(center_point[0], center_point[1], c='blue') 
plt.show()
```

From the centre point, we found the nearest location on the map of Amsterdam, as shown in Figure 3. The post code of this location is 1018 DP Amsterdam and is close to Jonas Daniël Meijerplein.The area has a lot of open space, making it a viable location. In addition, it is easily accessible to all nodes on the track, making it a reasonable choice.

![Spot](/images/Figure_3.png) <p style="text-align: center;"> <span style="color:grey"> $\small (Figure 3, A Suitable Spot)$ </span> </p>


### 3.Find the closest bus and tram stops at the start and finish of the swimming route. How many people can be transported within an hour.

```ruby
try: 
    bus_stop = ox.features.features_from_point(location, tags={'public_transport': 'stop_position'}, dist=500) 
    bus_stop.to_csv("bus_stop.csv") 
    print(bus_stop.name) 
except: 
    print("no station in @‘dist’ metres") 
try: 
    bus_stop_to = ox.features.features_from_point(location_to, tags = {'public_transport': 'stop_position'}, dist=500) 
    bus_stop_to.to_csv() 
    bus_stop_to.to_csv("bus_stop_to.csv") 
    print(bus_stop_to.name) 
except: 
    print("no station in @‘dist’ metres")
```

Initially, considering pedestrian accessibility, we searched for stations within a certain radius of the start and end points. We chose a search radius of 500 metres. Table 1 shows the list of stations collected.

| close_to | bus | tram | name                           | geometry                     |
| -------- | --- | ---- | ------------------------------ | ---------------------------- |
| start    | yes |      | Amsterdam, Piet Heinkade       | POINT (4.9135819 52.3773362) |
| start    |     | yes  | Muziekgebouw                   | POINT (4.9134308 52.3772063) |
| start    |     | yes  | Muziekgebouw                   | POINT (4.912547 52.3772761)  |
| start    |     | yes  | Kattenburgerstraat             | POINT (4.9211099 52.3761672) |
| start    | yes |      | Amsterdam, Kattenburgerstraat  | POINT (4.9184891 52.372718)  |
| start    | yes |      | Amsterdam, Kattenburgerstraat  | POINT (4.9179263 52.372271)  |
| start    | yes |      | Amsterdam, IJ tunnel           | POINT (4.9094406 52.3722719) |
| start    | yes |      | Amsterdam, Kattenburg          | POINT (4.9205741 52.3764724) |
| start    | yes |      | Amsterdam, Piet Heinkade       | POINT (4.9140766 52.377227)  |
| finish   |     | yes  | Concertgebouw                  | POINT (4.8796377 52.3566951) |
| finish   |     | yes  | Rijksmuseum                    | POINT (4.887104 52.3609734)  |
| finish   |     | yes  | Vijzelgracht                   | POINT (4.8909623 52.3599031) |
| finish   |     | yes  | Concertgebouw                  | POINT (4.8795995 52.3560193) |
| finish   |     | yes  | Museumplein                    | POINT (4.8812446 52.358854)  |
| finish   |     | yes  | Vijzelgracht                   | POINT (4.8921024 52.3595051) |
| finish   |     | yes  | Concertgebouw                  | POINT (4.8791804 52.3559245) |
| finish   |     | yes  | Concertgebouw                  | POINT (4.8798 52.3564107)    |
| finish   | yes |      | Amsterdam, Leidseplein         | POINT (4.8806142 52.3625646) |
| finish   |     | yes  | Leidseplein                    | POINT (4.8830722 52.3634714) |
| finish   |     | yes  | Vijzelgracht                   | POINT (4.8910303 52.3600132) |
| finish   |     | yes  | Van Baerlestraat               | POINT (4.878318 52.3584538)  |
| finish   |     | yes  | Van Baerlestraat               | POINT (4.8781266 52.3587793) |
| finish   |     | yes  | Leidseplein                    | POINT (4.8829633 52.3642229) |
| finish   |     | yes  | Rijksmuseum                    | POINT (4.8873395 52.3608307) |
| finish   | yes |      | Amsterdam, Ferdinand Bolstraat | POINT (4.8918514 52.3579917) |
| finish   | yes |      | Amsterdam, Leidseplein         | POINT (4.8810441 52.3620635) |
| finish   | yes |      | Amsterdam, Ruysdaelkade        | POINT (4.8865615 52.3602454) |
| finish   | yes |      | Amsterdam, Ruysdaelkade        | POINT (4.8865688 52.3603257) |
| finish   | yes |      | Amsterdam, Ferdinand Bolstraat | POINT (4.8923047 52.3579616) |
| finish   |     | yes  | Marie Heinekenplein            | POINT (4.8907033 52.3570037) |
| finish   |     | yes  | Marie Heinekenplein            | POINT (4.8907718 52.3571177) |
| finish   |     | yes  | Leidseplein                    | POINT (4.8810698 52.3632085) |
| finish   | yes |      | Concertgebouw                  | POINT (4.8785466 52.3554983) |
| finish   | yes |      | Vijzelgracht                   | POINT (4.8910469 52.3606866) |
| finish   | yes |      | Vijzelgracht                   | POINT (4.8912207 52.3606661) |
| finish   |     | yes  | Vijzelgracht                   | POINT (4.8925358 52.3594772) |
| finish   | yes |      | Amsterdam, Leidseplein         | POINT (4.8809776 52.3631402) |
| finish   |     | yes  | Weteringcircuit                | POINT (4.8923379 52.3593327) |
| finish   | yes |      | Concertgebouw                  | POINT (4.8795913 52.3560311) |
| finish   | yes |      | Concertgebouw                  | POINT (4.8796233 52.3566894) |
| finish   | yes |      | Concertgebouw                  | POINT (4.8798146 52.3564161) |
| finish   |     | yes  | Museumplein                    | POINT (4.8806042 52.3587143) |
| finish   |     | yes  | Museumplein                    | POINT (4.880612 52.3586985)  |
| finish   | yes |      | Amsterdam, Museumplein         | POINT (4.8808204 52.3586774) |

In the estimation, we have assumed an average arrival frequency of 5 buses per hour and 4 trams per hour (source: [Public transport in Amsterdam](https://www.introducingamsterdam.com/public-transport?_gl=1*q6cymw*_up*MQ..*_ga*MTI1NTU0Mjk1OS4xNjk3NTUyMjAw*_ga_216706797*MTY5NzU1MjIwMC4xLjAuMTY5NzU1MjIwMC4wLjAuMA..)). In addition, we estimate that the maximum capacity of each bus is 30 passengers and that of each tram is 50 passengers. Based on these rough estimates, we can calculate that the maximum interchange capacities of the stations near the origin and the terminus in an hour are 1,150 and 6,450 respectively.

### 4.Can you find which bus and tram lines these are, and can you find their routes?

### 5.Calculate the centrality of the start, finish, and centre node of the route. Which centrality calculation makes the most sense. [See this link](https://networkx.org/documentation/stable/reference/algorithms/centrality.html).

### 6.Find all cafes, restaurants near the finish line. Walking time smaller than 10 minutes.

```ruby
plt.close('all') 
graph = ox.graph_from_point(location_to, dist=2100) 
poi = ox.features.features_from_point(location_to, tags={'amenity': ['cafe','restaurant']}, dist=750) 
target_node = ox.distance.nearest_nodes(graph, location_to[1], location_to[0], return_dist=True) 
pt = ox.graph_to_gdfs(city_whole, edges=False).unary_union.centroid 
bbox = ox.utils_geo.bbox_from_point(location_to, dist=2100) 
fig2, ax2 = ox.plot_graph(city_whole, bbox=bbox, show=False, close=False) 
name = [] 
for row in poi.T.T.itertuples(): 
    try: 
        orig = getattr(row, 'geometry') 
        name1 = getattr(row, 'name') 
        orig_node = ox.distance.nearest_nodes(graph, orig.x, orig.y, return_dist=True) 
        length = nx.shortest_path_length(G=graph, source=orig_node[0], target=target_node[0], weight='length') 
        if length <750: 
            name.append(name1) 
            ax2.scatter(orig.x, orig.y, c='blue') 
    except: 
        pass 
plt.show() 
plt.savefig("4.jpg") 
print(name)
```
