# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # question 2

    # import airbnb data
    airbnb = pd.read_csv('listings.csv')
    neighbourhood = pd.read_csv('neighbourhoods.csv')
    # calculate the number of rooms for each neighbourhood
    num = []
    name = []
    neighbourlist = neighbourhood.values.tolist()
    for i in neighbourlist:
        sublist = airbnb.loc[airbnb['neighbourhood'] == str(i[0])]
        num.append(sublist.shape[0])
        name.append(str(i[0]))

    # plotting the result
    plt.barh(name, num)
    plt.show()


    # question 3

    '''
    geolocator = Nominatim(user_agent="lenovo")
    airbnb1 = airbnb.sample(n=10) #randomly choose 10 rows for showing
    Loc = airbnb1[['latitude','longitude']]
    street = []
    for ind,row in Loc.iterrows():
        a = str(row['latitude'])
        b = str(row['longitude'])
        address = geolocator.reverse(a+","+b)
        address_split = address.address.split(',')
        street.append(address_split[1])
    print(street)

    '''

    # question6

    plt.close("all")
    num = []
    name = []
    airbnb_list = airbnb.transpose()
    airbnb1 = airbnb_list.values.tolist()

    # define a function to find duplicates
    def find_duplicates(lst):
        return list(set([x for x in lst if lst.count(x) > 1]))

    # find the duplicate house types
    house_type = find_duplicates(airbnb1[8])
    print(house_type)

    # find names and numbers for each house type
    for i in house_type:
        # print(str(i[0]))
        sublist = airbnb.loc[airbnb['room_type'] == str(i)]
        num.append(sublist.shape[0])
        name.append(str(i))
    # plotting
    plt.barh(name, num)
    plt.show()

    #Question4-1

    # counting the numbers for each room type
    count = []
    for i in range(4):
        name = house_type[i]
        a = airbnb.query('room_type == @name')
        count.append(len(a))
    print(count)
    room_type_count = pd.DataFrame([count], columns = house_type)
    #Question 4-2
    # check the amount of rooms which is available all year
    num_rented = len(airbnb.query('availability_365 < 365'))
    print(num_rented)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
