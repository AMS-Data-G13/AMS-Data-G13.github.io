---
layout: archive
title: "Amsterdam Transport"
permalink: /assignment-4/
author_profile: true
---

First, we selected the starting and ending points for our route, which were AMS Institute and the Rijksmuseum, respectively. We then identified the nearest points on the Amsterdam canals corresponding to these two locations. 

```ruby
import osmnx as ox
import networkx as nx
import pickle
import matplotlib.pyplot as plt
import pandas as pd

# 4.0 plotting the route
ox.config(use_cache=True, log_console=True) 
city = ox.graph_from_place('Amsterdam', retain_all=False, truncate_by_edge=False, 
                        simplify=True, custom_filter='["waterway"~"canal"]') 

# the starting and finishing point is AMS institute and the national museum
location = ox.geocode("Kattenburgerstraat 5, Amsterdam, Netherlands") 
location_to = ox.geocode("Museumstraat 1, Amsterdam, Netherlands") 
nodes = ox.distance.nearest_nodes(city, location[1], location[0], return_dist=True) 
nodes_to = ox.distance.nearest_nodes(city, location_to[1], location_to[0], return_dist=True)

# finding the route along the canal
path = ox.shortest_path(city, nodes[0], nodes_to[0]) 
# print(path)

# plotting
pt = ox.graph_to_gdfs(city, edges=False).unary_union.centroid 
bbox = ox.utils_geo.bbox_from_point(location, dist=5000) 
fig, ax = ox.plot_graph_route(city, path, bbox=bbox, show=False, close=False) 
```

Using these two points, we plotted the shortest path, which became the course for our activity. The path is shown in Figure 1 (luckily it's over 5 km). Combining the knowledge from Assignments 1 and 2, we chose a route that avoided areas of poor water quality and was therefore a good choice.

![Route](/images/Figure_1.png) 
<p style="text-align: center;"> <span style="color:grey"> (Figure 1, the swimming route) </span> </p>

In Figure 1, the final chosen route is depicted in red, while other waterways and nodes are shown in white. 

### 1.Find the centre of the nodes of the swimming route. [See this link](https://stackoverflow.com/questions/46238813/osmnx-get-coordinates-of-nodes-using-osm-id).

$$Alt_{centre} = \frac{\sum_{i=1}^{n}{Alt_{node}}}{n}$$

$$Lat_{centre} = \frac{\sum_{i=1}^{n}{Lat_{node}}}{n}$$

```ruby
# calculating the cordinates of the center point
lat = 0 
lon = 0 
for points in path: 
    lat += city.nodes[points]['x'] 
    lon += city.nodes[points]['y'] 
lat_center = lat / len(path) 
lon_center = lon / len(path) 
center_point = (lon_center, lat_center) 
print(center_point)

# plotting
ax.scatter(lon_center, lat_center, c='blue') 
plt.show()
```

When calculating the centre point, we added the coordinates of all points along the track and divided the sum by the number of points. This calculation yielded the corrected coordinates of the centre point, (52.36604662, 4.9001779899999995). The central point was then plotted on the map, as illustrated in Figure 2. 

![Spot](/images/Figure_2.png) 
<p style="text-align: center;"> <span style="color:grey"> (Figure 2, the centre point) </span> </p>

### 2.Use the centre to find a suitable spot for the Event Headquarters.

```ruby
# finding the whole map and finding the center node from the map
city_whole = (ox.graph_from_place('Amsterdam, Netherlands', simplify=True)) 
nodes_centre = ox.distance.nearest_nodes(city_whole, center_point[1], center_point[0], return_dist=True)

# plotting
pt = ox.graph_to_gdfs(city, edges=False).unary_union.centroid 
bbox = ox.utils_geo.bbox_from_point(center_point, dist=5000) 
fig, ax1 = ox.plot_graph(city_whole, bbox=bbox, show=True, close= False) 
ax1.scatter(center_point[0], center_point[1], c='blue') 
plt.show()
```

From the centre point, we found the nearest location on the map of Amsterdam, as shown in Figure 3. The post code of this location is 1018 DP Amsterdam and is close to Jonas Daniël Meijerplein.The area has a lot of open space, making it a viable location. In addition, it is easily accessible to all nodes on the track, making it a reasonable choice.

![Spot](/images/Figure_3.png) 
<p style="text-align: center;"> <span style="color:grey"> (Figure 3, a suitable spot) </span> </p>


### 3.Find the closest bus and tram stops at the start and finish of the swimming route. How many people can be transported within an hour.

```ruby
#finding the bus and tram stops near the starting point
try: 
    bus_stop = ox.features.features_from_point(location, tags={'public_transport': 'stop_position'}, dist=500) 
    bus_stop.to_csv("bus_stop.csv") 
    print(bus_stop.name) 
except: 
    print("no station in @‘dist’ metres")

# finding the bus and tram stops near the ending point
try: 
    bus_stop_to = ox.features.features_from_point(location_to, tags = {'public_transport': 'stop_position'}, dist=500) 
    bus_stop_to.to_csv("bus_stop_to.csv") 
    print(bus_stop_to.name) 
except: 
    print("no station in @‘dist’ metres")
```

Initially, considering pedestrian accessibility, we searched for stations within a certain radius of the start and end points. We chose a search radius of 500 metres. Table 1 shows the list of stations collected.

[Table 1](/files/Table1.xlsx)

| Close_to | Bus | Tram | Name                           | Geometry                     |
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

```ruby
# finding the bus route,but the code is not showing any route, reason unknown
tags = {'route': 'bus'}
gdfox = ox.features_from_point(location_to, tags, dist=1000)
print(gdfox)
```

### 5.Calculate the centrality of the start, finish, and centre node of the route. Which centrality calculation makes the most sense. [See this link](https://networkx.org/documentation/stable/reference/algorithms/centrality.html).

Closeness centrality measures how easily a node can reach other nodes in a network. It's used to determine the point's accessibility within a network. Nodes with high closeness centrality are closer, in terms of network connections, to other nodes. In a geographic context, this reflects that these points are more accessible, similar to how central locations in a city are more easily reachable from other places. Therefore, we choose closeness centrality to give support evidence for the choosing of the points.

```ruby
# finding the map
graph = ox.graph_from_point(center_point, dist=5000)

# finding the nodes close to the start/center/end point
nodes = ox.distance.nearest_nodes(graph, location[1], location[0], return_dist=True)
nodes_to = ox.distance.nearest_nodes(graph, location_to[1], location_to[0], return_dist=True)
nodes_cen = ox.distance.nearest_nodes(graph, center_point[1], center_point[0], return_dist=True)

# calculate centrality
start_centrality = nx.closeness_centrality(graph, nodes[0])
cen_centrality = nx.closeness_centrality(graph, nodes_cen[0])
end_centrality = nx.closeness_centrality(graph, nodes_to[0])
print(start_centrality,cen_centrality,end_centrality)
```

|Point       |Node                |
|------------|--------------------|
|Start point |0.014975167550752658|
|Center point|0.016698413110206794|
|End point   |0.014168299848680767|

The results are largely consistent with our expectations. The center point is indeed closer to the center of Amsterdam, which makes it more accessible to other points on the map. However, it's important to note that the calculated results can vary based on factors such as the selected map size and the parameters used, including the choice of the center point.

### 6.Find all cafes, restaurants near the finish line. Walking time smaller than 10 minutes.

```ruby
# finding the map near the ending point
plt.close('all') 
graph = ox.graph_from_point(location_to, dist=2100)

# extracting all the cafes and restaurants within 750 radius
poi = ox.features.features_from_point(location_to, tags={'amenity': ['cafe','restaurant']}, dist=750) 
target_node = ox.distance.nearest_nodes(graph, location_to[1], location_to[0], return_dist=True) 
pt = ox.graph_to_gdfs(city_whole, edges=False).unary_union.centroid 
bbox = ox.utils_geo.bbox_from_point(location_to, dist=2100) 
fig2, ax2 = ox.plot_graph(city_whole, bbox=bbox, show=False, close=False)

# examine the shortest distance, if it is within 10 minutes walk(750m)
name = []
i = 0
for row in poi.T.T.itertuples():
    try:
        orig = getattr(row, 'geometry')
        name1 = getattr(row, 'name')
        orig_node = ox.distance.nearest_nodes(graph, orig.x, orig.y, return_dist=True)
        length = nx.shortest_path_length(G=graph, source=orig_node[0], target=target_node[0], weight='length')
        if length <750:
            name.append(name1)
            ax2.scatter(orig.x, orig.y, c='blue')
            i += 1
            if i == 1:
                listing1 = pd.DataFrame(
                    {"amenity":[getattr(row, 'amenity')],"length":[length],"name":[getattr(row, 'name')],
                     "geometry":[getattr(row, 'geometry')],"description":[getattr(row, 'description')]})
            else:
                listing = pd.DataFrame(
                    {"amenity": [getattr(row, 'amenity')], "length": [length], "name": [getattr(row, 'name')],
                     "geometry": [getattr(row, 'geometry')], "description": [getattr(row, 'description')]})
                listing1 = pd.concat([listing1, listing], ignore_index=True)

    except:
        pass
listing1.to_csv("listing.csv")

# plotting
plt.show() 
plt.savefig("4.jpg") 
print(name)
```

![Cafe](/images/Figure_4.png) 
<p style="text-align: center;"> <span style="color:grey"> (Figure 4, all nearby cafes and restaurants) </span> </p>

[Table 2](/files/name_listing.csv)

|num|amenity   |length |name                                 |geometry                    |
|---|----------|-------|-------------------------------------|----------------------------|
|1  |restaurant|703.303|Waaghals                             |POINT (4.889014 52.3571286) |
|2  |cafe      |644.229|Café Americain                       |POINT (4.8813718 52.3638967)|
|3  |restaurant|542.675|Bollywood Indian Restaurant          |POINT (4.8844033 52.3639694)|
|4  |restaurant|542.675|Puri Mas Indonesisch Restaurant      |POINT (4.8845382 52.3641036)|
|5  |restaurant|625.788|Brasserie Keyzer                     |POINT (4.8792088 52.3568126)|
|6  |restaurant|545.967|Small Talk                           |POINT (4.878408 52.3579755) |
|7  |restaurant|703.303|ISSHIN                               |POINT (4.8886451 52.3570377)|
|8  |restaurant|425.239|Otaru                                |POINT (4.8888704 52.3584175)|
|9  |restaurant|311.648|Sama Sebo                            |POINT (4.8831414 52.3606764)|
|10 |restaurant|557.641|Maxies                               |POINT (4.8797621 52.3600875)|
|11 |restaurant|430.877|Hard Rock Cafe                       |POINT (4.8833077 52.3621869)|
|12 |restaurant|605.926|Hosokawa                             |POINT (4.8827502 52.3629202)|
|13 |restaurant|430.266|Wagamama                             |POINT (4.8831541 52.3625079)|
|14 |restaurant|430.877|Maximus Steak House                  |POINT (4.8834726 52.3622945)|
|15 |restaurant|520.712|De Balie                             |POINT (4.883101 52.36312)   |
|16 |cafe      |694.408|Starbucks                            |POINT (4.8836352 52.3645106)|
|17 |cafe      |584.227|Superskunk Coffeeshop                |POINT (4.8851485 52.3642612)|
|18 |restaurant|542.675|Piccolino                            |POINT (4.8852731 52.3636053)|
|19 |restaurant|353.062|Momo                                 |POINT (4.8825862 52.3615027)|
|20 |restaurant|511.865|Oma                                  |POINT (4.8851836 52.3630587)|
|21 |restaurant|634.081|Stoop & Stoop Eetcafé                |POINT (4.8838952 52.3642795)|
|22 |restaurant|634.081|Pancake Corner Restaurant            |POINT (4.88345 52.3640344)  |
|23 |restaurant|522.801|Palladium Restaurant Club            |POINT (4.8835286 52.3635772)|
|24 |restaurant|652.319|Nam Kee                              |POINT (4.8911961 52.3574253)|
|25 |restaurant|677.521|de Oesterbar                         |POINT (4.8827741 52.3647013)|
|26 |restaurant|542.675|Antonio's Restaurante                |POINT (4.88489 52.3636482)  |
|27 |restaurant|542.675|Bojo                                 |POINT (4.8847921 52.3639322)|
|28 |restaurant|542.675|Chicano's                            |POINT (4.8847449 52.363749) |
|29 |restaurant|511.865|De blauwe Hollander                  |POINT (4.8847235 52.3635484)|
|30 |restaurant|542.675|El Rancho                            |POINT (4.8845402 52.3638816)|
|31 |restaurant|694.408|Greek                                |POINT (4.8841943 52.3643571)|
|32 |restaurant|694.408|Los Amigos                           |POINT (4.8842525 52.3642942)|
|33 |restaurant|634.081|Mimo                                 |POINT (4.8843814 52.3642096)|
|34 |restaurant|542.675|Mykonos                              |POINT (4.8846815 52.3640102)|
|35 |restaurant|694.408|O' Sole Mio                          |POINT (4.8841433 52.3644198)|
|36 |restaurant|511.865|Peppino                              |POINT (4.8846075 52.3634912)|
|37 |restaurant|694.408|Pisa                                 |POINT (4.8839811 52.3644852)|
|38 |restaurant|634.081|Royal Thai                           |POINT (4.8842311 52.3641259)|
|39 |restaurant|542.675|Tapas                                |POINT (4.8849795 52.3637854)|
|40 |restaurant|511.865|Mr Tong's                            |POINT (4.8848237 52.3633343)|
|41 |restaurant|542.675|Zorba de Griek                       |POINT (4.8851083 52.3637257)|
|42 |restaurant|634.081|Do Brasil                            |POINT (4.8840332 52.3641938)|
|43 |restaurant|511.865|il Palio                             |POINT (4.8849115 52.3633969)|
|44 |restaurant|511.865|Mama                                 |POINT (4.8846914 52.3631784)|
|45 |restaurant|511.865|Ceppi’s                              |POINT (4.8850519 52.3628586)|
|46 |restaurant|542.675|El Patio Granada                     |POINT (4.8854166 52.3635176)|
|47 |restaurant|511.865|Leeuw                                |POINT (4.8848025 52.3630944)|
|48 |restaurant|511.865|Madras                               |POINT (4.8848499 52.3630641)|
|49 |restaurant|511.865|Maya                                 |POINT (4.8844538 52.3636051)|
|50 |restaurant|338.413|Mayur                                |POINT (4.8861759 52.3623426)|
|51 |restaurant|509.305|In de Buurt                          |POINT (4.8845121 52.3630261)|
|52 |restaurant|542.675|Porto Carrara                        |POINT (4.8852647 52.3634013)|
|53 |restaurant|511.865|Sherpa                               |POINT (4.8847519 52.3631367)|
|54 |restaurant|511.865|Taste of Culture                     |POINT (4.8851368 52.3631049)|
|55 |restaurant|542.675|El Vino                              |POINT (4.8848889 52.3639005)|
|56 |restaurant|542.675|Granada                              |POINT (4.8853422 52.3636437)|
|57 |restaurant|584.227|Japan Inn                            |POINT (4.8854331 52.3638952)|
|58 |restaurant|542.675|Los Argentinos                       |POINT (4.8854787 52.3637143)|
|59 |restaurant|542.675|Moshi Moshi                          |POINT (4.8854104 52.36368)  |
|60 |restaurant|694.408|The Guru of India                    |POINT (4.8828626 52.3650182)|
|61 |restaurant|491.747|Pancake Corner                       |POINT (4.8838974 52.3628007)|
|62 |restaurant|697.253|De Smoeshaan                         |POINT (4.8805712 52.3640307)|
|63 |restaurant|731.813|Café Loetje                          |POINT (4.8842366 52.3543672)|
|64 |restaurant|207.754|Srikandi                             |POINT (4.8836467 52.3614794)|
|65 |restaurant|634.081|Maximus Pizzeria - Steakhouse        |POINT (4.8836566 52.3641394)|
|66 |restaurant|677.521|Sumo                                 |POINT (4.882715 52.3647599) |
|67 |restaurant|643.662|Kaasbar                              |POINT (4.8905157 52.3572817)|
|68 |restaurant|698.081|Yuan's Hot Pot                       |POINT (4.8904953 52.3570239)|
|69 |restaurant|652.319|Taj                                  |POINT (4.891031 52.3574228) |
|70 |restaurant|724.995|Simpel                               |POINT (4.8907851 52.3565041)|
|71 |restaurant|724.995|Soju Bar                             |POINT (4.8907691 52.3564272)|
|72 |restaurant|724.995|The Seafood Bar                      |POINT (4.8904068 52.3564701)|
|73 |restaurant|718.614|Monte Verde                          |POINT (4.8872973 52.3547524)|
|74 |restaurant|700.448|De kleine Valk                       |POINT (4.891505 52.3573485) |
|75 |restaurant|718.614|Juuls                                |POINT (4.8874016 52.3547449)|
|76 |restaurant|475.684|Lombardo's                           |POINT (4.8887021 52.3635469)|
|77 |cafe      |475.684|Stach cafe                           |POINT (4.8884551 52.3633122)|
|78 |cafe      |584.227|Bocca Coffee Roasters                |POINT (4.8868127 52.3644463)|
|79 |cafe      |634.081|Satellite Sportscafe                 |POINT (4.8834687 52.3640476)|
|80 |restaurant|511.865|Picchino                             |POINT (4.8849034 52.3632077)|
|81 |cafe      |542.675|Cafe het Hok                         |POINT (4.8851645 52.363487) |
|82 |restaurant|542.675|Mama Impasto                         |POINT (4.8850062 52.3634868)|
|83 |restaurant|542.675|Eetcafé                              |POINT (4.8848555 52.3635486)|
|84 |restaurant|509.305|Castell                              |POINT (4.8848679 52.3628166)|
|85 |restaurant|509.305|Restaurant Dubbel                    |POINT (4.8850714 52.3627171)|
|86 |cafe      |624.961|Café&#124;Brasserie Stadsschouwburg       |POINT (4.882281 52.3639853) |
|87 |restaurant|338.413|Winebar Shiraz                       |POINT (4.8857879 52.3623691)|
|88 |restaurant|430.266|The Avocado Show                     |POINT (4.8835362 52.3625483)|
|89 |cafe      |584.227|Coffeeshop Easytimes                 |POINT (4.8850229 52.3643312)|
|90 |restaurant|584.227|Poké Perfect                         |POINT (4.8857331 52.3638861)|
|91 |cafe      |474.842|B&B                                  |POINT (4.8824617 52.3623251)|
|92 |restaurant|542.675|Tacos & Tequila                      |POINT (4.8855319 52.3634016)|
|93 |restaurant|205.118|Le Rendez-vous                       |POINT (4.8863852 52.361421) |
|94 |restaurant|694.408|Full Moon Garden                     |POINT (4.883854 52.3646327) |
|95 |cafe      |658.512|Village Bagels                       |POINT (4.8920333 52.3623655)|
|96 |restaurant|600.187|Carrousel                            |POINT (4.891748 52.3589849) |
|97 |restaurant|693.674|Myrabelle                            |POINT (4.8918915 52.3619155)|
|98 |restaurant|681.735|Piet de Leeuw                        |POINT (4.8921422 52.361512) |
|99 |restaurant|681.735|Sukhothai Thanee                     |POINT (4.8924177 52.3614727)|
|100|cafe      |608.813|Bar Do                               |POINT (4.8915062 52.3609252)|
|101|restaurant|608.813|Proper. Indofood                     |POINT (4.8914637 52.3607992)|
|102|restaurant|608.813|SUSHI GK                             |POINT (4.8914356 52.3606912)|
|103|restaurant|567.575|Iboenda                              |POINT (4.8914217 52.3606013)|
|104|cafe      |384.402|Back to Black coffee bar and roastery|POINT (4.8885688 52.3610387)|
|105|cafe      |567.575|Luuk's                               |POINT (4.8913927 52.3605653)|
|106|restaurant|403.134|Levant                               |POINT (4.8873509 52.361025) |
|107|restaurant|745.257|Oresti's Taverna                     |POINT (4.8783821 52.3634426)|
|108|restaurant|578.59 |Pompa Tapas Bar                      |POINT (4.8779295 52.3581174)|
|109|cafe      |578.59 |The Coffee District                  |POINT (4.8776367 52.3580174)|
|110|restaurant|404.016|Patou                                |POINT (4.8813254 52.3602398)|
|111|restaurant|662.271|L' Entrecote et les dames            |POINT (4.8805264 52.3556659)|
|112|restaurant|662.271|Bouf                                 |POINT (4.8805564 52.3556121)|
|113|restaurant|743.492|Anjappar                             |POINT (4.8806241 52.3548123)|
|114|restaurant|703.303|Rainbowl                             |POINT (4.8886429 52.3569857)|
|115|restaurant|703.303|Van 't Spit                          |POINT (4.888619 52.3567873) |
|116|cafe      |643.662|Bakers & Roasters                    |POINT (4.8899479 52.3572951)|
|117|restaurant|511.865|Chicanos / Tex Mex                   |POINT (4.8843666 52.3636279)|
|118|restaurant|589.052|Solo                                 |POINT (4.8803931 52.3560295)|
|119|restaurant|475.684|Vatten Ramen                         |POINT (4.888799 52.3633111) |
|120|restaurant|516.948|Taiko                                |POINT (4.87924 52.3585627)  |
|121|restaurant|603.921|La Storia della Vita                 |POINT (4.8922941 52.3596722)|
|122|cafe      |151.799|                                     |POINT (4.8857446 52.3597769)|
|123|restaurant|595.333|San George                           |POINT (4.8796087 52.3629726)|
|124|cafe      |502.485|Restaurant Stedelijk                 |POINT (4.8794436 52.3574939)|
|125|restaurant|473.36 |Buffet van Odette                    |POINT (4.8889892 52.3622855)|
|126|restaurant|35.034 |Rijks                                |POINT (4.8842926 52.3595984)|
|127|restaurant|576.097|Lavinia Good Food                    |POINT (4.8898054 52.3631654)|
|128|restaurant|662.271|Martinot                             |POINT (4.8806877 52.3555304)|
|129|restaurant|677.521|New York Steakhouse                  |POINT (4.8831308 52.364509) |
|130|restaurant|542.675|The Pantry                           |POINT (4.8849563 52.3634594)|
|131|restaurant|718.614|Izakaya                              |POINT (4.8875769 52.3545104)|
|132|cafe      |634.081|Easy Internet Cafe                   |POINT (4.8837681 52.3640142)|
|133|cafe      |643.662|Bakers & Roasters                    |POINT (4.889846 52.3573122) |
|134|restaurant|647.235|Siriphon                             |POINT (4.8898758 52.3575399)|
|135|cafe      |632.032|Corner Bakery Amsterdam              |POINT (4.8840259 52.3547327)|
|136|cafe      |511.865|The Rookies                          |POINT (4.8852296 52.3629689)|
|137|restaurant|509.305|Sumo                                 |POINT (4.8838817 52.3633312)|
|138|cafe      |658.512|de Fles                              |POINT (4.892228 52.3623331) |
|139|cafe      |354.039|brasserie zuiderbad                  |POINT (4.8860801 52.357493) |
|140|restaurant|368.975|Le Tambourin                         |POINT (4.881202 52.3582777) |
|141|restaurant|698.081|Yuan's Hot Pot                       |POINT (4.8905324 52.3569617)|
|142|restaurant|703.467|Padina Bar                           |POINT (4.893177 52.357783)  |
|143|restaurant|546.04 |The Pancake Club                     |POINT (4.8813295 52.3626071)|
|144|restaurant|700.448|Vegan Junk Food Bar                  |POINT (4.8916033 52.3572501)|
|145|restaurant|664.529|Kailash Parbat                       |POINT (4.8924555 52.3596549)|
|146|restaurant|724.995|The Beefsteak Club                   |POINT (4.8904706 52.3565873)|
|147|cafe      |710.476|café De Tulp                         |POINT (4.8916761 52.3569168)|
|148|cafe      |164.562|Kiosk Rembrandt Van Gogh             |POINT (4.8831125 52.3592175)|
|149|restaurant|658.512|Tokyo Ramen                          |POINT (4.8920385 52.3624137)|
|150|restaurant|714.409|Eggs Benaddicted                     |POINT (4.8849343 52.3643939)|
|151|restaurant|511.865|Pier 62                              |POINT (4.8847851 52.3631098)|
|152|restaurant|694.408|Gandhi                               |POINT (4.8829781 52.3649437)|
|153|cafe      |548.835|Chimney Cake Bakery & Café           |POINT (4.879167 52.356934)  |
|154|cafe      |408.368|Blushing                             |POINT (4.8803835 52.3587949)|
|155|restaurant|743.492|Anjappar                             |POINT (4.8806009 52.3547972)|
|156|cafe      |714.409|Eggs Benaddicted                     |POINT (4.884987 52.3643561) |
|157|restaurant|686.907|AN                                   |POINT (4.8937415 52.3593592)|
|158|restaurant|694.408|                                     |POINT (4.8840819 52.3644521)|
|159|restaurant|542.675|Hongdae Amsterdam                    |POINT (4.8848957 52.3638537)|
|160|restaurant|703.467|                                     |POINT (4.8931742 52.35772)  |
|161|restaurant|717.7  |Joost                                |POINT (4.8780303 52.3625932)|
|162|restaurant|487.423|Grand Café Lido                      |POINT (4.8819472 52.3625269)|
|163|cafe      |634.081|Get Down                             |POINT (4.8838071 52.3639818)|
