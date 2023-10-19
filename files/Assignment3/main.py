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


## Some additional thoughts on the questions

import pandas as pd
import plotly.express as px
from geopy.geocoders import Nominatim
import csv
from collections import Counter

    #Question 2
    airbnb = pd.read_csv('listings.csv') 
    neighbourhood = airbnb.neighbourhood.value_counts()
    fig = px.bar(neighbourhood, y='count', text_auto=True, title="the amount of AirBnB locations per neighbourhood")
    fig.show()

    #Question 3
    geolocator = Nominatim(user_agent="user")
    Loc = airbnb[['latitude','longitude']] 

    file = 'location.csv'
    header = ['location', 'coordinate']
    with open(file,'w',encoding='utf-8',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)

    #Get a specific address based on latitude and longitude
    for i,row in Loc.iterrows(): 
        a = str(row['latitude']) 
        b = str(row['longitude']) 
        address = geolocator.reverse(a+","+b, timeout=None) 
        print(address)
        
        with open(file,'a+',encoding='utf-8',newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(address)
            csvfile.close()

     #Get the postcode from the address
     Location = pd.read_csv('location.csv') 
     street = []
     for i, row in Location.iterrows():
         Location_split = row[1].split(',')
         street.append(Location_split[-2]) 

     #Counting which postcodes appear most often
     count = Counter(street)
     print(count)
     postcode = pd.DataFrame(count, index=[0])
     print(postcode)
     postcode.to_csv('postcode.csv', index=False)

     #Filter out addresses containing the most frequently occurring postcodes
     df = pd.DataFrame(street)
     post = []
     code = []
     for i, row in df.iterrows():
         df_split = row[0].split(' ')
         post.append(df_split[1]) 
         code.append(df_split[-1])

     df1 = pd.DataFrame(post)
     df2 = pd.DataFrame(code)

     New_loc = pd.concat([Location,df1,df2],axis=1)
     New_loc.columns = ['num','location','coordinate','post','code']
     CH_1 = New_loc[New_loc['post'] == '1052']
     CH_2 = CH_1[CH_1['code'] == 'CH']

     StreetName = pd.DataFrame(CH_2)
     StreetName.to_csv('StreetName.csv',sep=',',index=True,header=True) 

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
