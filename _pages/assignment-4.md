---
layout: archive
title: "Amsterdam Transport"
permalink: /assignment-4/
author_profile: true
---

### 1.Find the centre of the nodes of the swimming route. [See this link](https://stackoverflow.com/questions/46238813/osmnx-get-coordinates-of-nodes-using-osm-id).

First, we selected the starting and ending points for our route, which were AMS Institute and the Rijksmuseum, respectively. We then identified the nearest points on the Amsterdam canals corresponding to these two locations. Using these two points, we plotted the shortest path, which became the course for our activity. The path is shown in Figure 1 (luckily it's over 5 km). Combining the knowledge from Assignments 1 and 2, we chose a route that avoided areas of poor water quality and was therefore a good choice.

![Route](/images/Figure_1.png)
<p style="text-align: center;"><span style="color:grey"> $\small (Figure 1, The Swimming Route)$ </span></p>

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
In Figure 1, the final chosen route is depicted in red, while other waterways and nodes are shown in white. 

$$Alt_{centre} = \frac{\sum_{i=1}^{n}{Alt_{node}}}{n}$$

$$Lat_{centre} = \frac{\sum_{i=1}^{n}{Lat_{node}}}{n}$$

When calculating the centre point, we added the coordinates of all points along the track and divided the sum by the number of points. This calculation yielded the corrected coordinates of the centre point, (52.36604662, 4.9001779899999995). The central point was then plotted on the map, as illustrated in Figure 2. 

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
![Spot](/images/Figure_2.png)
<p style="text-align: center;"><span style="color:grey"> (Figure 2, The Centre Point)</span></p>

### 2.Use the centre to find a suitable spot for the Event Headquarters.

### 3.Find the closest bus and tram stops at the start and finish of the swimming route. How many people can be transported within an hour.

### 4.Can you find which bus and tram lines these are, and can you find their routes?

### 5.Calculate the centrality of the start, finish, and centre node of the route. Which centrality calculation makes the most sense. [See this link](https://networkx.org/documentation/stable/reference/algorithms/centrality.html).

### 6.Find all cafes, restaurants near the finish line. Walking time smaller than 10 minutes.
