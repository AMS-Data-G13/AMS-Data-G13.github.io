# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import osmnx as ox
import networkx as nx
import pickle
import matplotlib.pyplot as plt

# Press the green button in the gutter to run the script.
import pandas as pd

if __name__ == '__main__':
    # Assignment4 transport

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
    # plotting
    pt = ox.graph_to_gdfs(city, edges=False).unary_union.centroid
    bbox = ox.utils_geo.bbox_from_point(location, dist=5000)
    fig, ax = ox.plot_graph_route(city, path, bbox=bbox, show=True, close=False)


    # question1  finding the centre of the nodes

    # calculating the cordinates of the center point
    lat = 0
    lon = 0
    for points in path:
        lat += city.nodes[points]['x']
        lon += city.nodes[points]['y']
    lat_center = lat / len(path)
    lon_center = lon / len(path)
    center_point = (lon_center, lat_center)
    # plotting
    ax.scatter(lon_center, lat_center, c='blue')
    plt.show()


    # question2

    # finding the whole map and finding the center node from the map
    city_whole = (ox.graph_from_place('Amsterdam, Netherlands', simplify=True))
    nodes_centre = ox.distance.nearest_nodes(city_whole, center_point[1], center_point[0], return_dist=True)
    # plotting
    pt = ox.graph_to_gdfs(city, edges=False).unary_union.centroid
    bbox = ox.utils_geo.bbox_from_point(center_point, dist=5000)
    fig, ax1 = ox.plot_graph(city_whole, bbox=bbox, show=True, close= False)
    ax1.scatter(center_point[0], center_point[1], c='blue')
    plt.show()

    # question3

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


    #question4

    # finding the bus route,but the code is not showing any route, reason unknown
    tags = {'route': 'bus'}
    gdfox = ox.features_from_point(location_to, tags, dist=1000)
    print(gdfox)



    #question 5

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

    #question6

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



