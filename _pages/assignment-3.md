---
layout: archive
title: "Amsterdam Housing"
permalink: /assignment-3/
author_profile: true
---

### 1.What Amsterdam will receive from tourist tax if the event lasts a week and you will have 30.000 visitors?

### 2.Plot the amount of AirBnB locations per neighbourhood.

```ruby
import pandas as pd
import plotly.express as px

airbnb = pd.read_csv('listings.csv') 
neighbourhood = airbnb.neighbourhood.value_counts()
fig = px.bar(neighbourhood, y='count', text_auto=True)
fig.show()
```

![neighbourhood](/images/neighbourhood.png) 
<p style="text-align: center;"> <span style="color:grey"> $\small (Figure 1, the amount of AirBnB locations per neighbourhood)$ </span> </p>

After aggregating all the Airbnb listings in Amsterdam by neighborhood, the statistical results we obtained are presented in Figure 1. It is evident that the De Baarsjes-Oud-West area has the highest number of Airbnb listings, while Bijlmer-Oost has the fewest.

### 3.Which street in Amsterdam has the most AirBnB apartments?

```ruby
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
street.to_csv("street.csv") 
print(street)
```

Since the Airbnb dataset did not include street-level information, we utilized geolocation services to find the corresponding street names based on coordinates. Due to the time-consuming nature of this process, for the assignment, we randomly selected ten Airbnb rental properties, determined their addresses, and extracted the street names. The results are presented in Figure 2. (If street names were successfully identified for all properties, the subsequent statistical process should be similar to that described in Question 2.)

![street name](/images/Figure_6.png) 
<p style="text-align: center;"> <span style="color:grey"> $\small (Figure 2, the street names)$ </span> </p>

### 4.Try to cross reference the data from the AirBnB dataset with the BBGA. Can you figure out if all apartments of AirBnB are designated as housing? Which number of apartments are not rented out all the time but are also used as normal housing?

```ruby
count = [] 
for i in range(4): 
    name = house_type[i] 
    a = airbnb.query('room_type == @name') 
    count.append(len(a)) 
print(count) 
room_type_count = pd.DataFrame([count], columns = house_type) 
#Question 4-2 
num_rented = len(airbnb.query('availability_365 < 365')) 
print(num_rented)
```

For this question, we were unsure about how to utilize the BBGA dataset, so all the responses are based on Airbnb data. Among the four room types, hotel rooms are not categorized as housing. Therefore, as an answer to the first question, 54 rooms were not designated as housing. Regarding the second question, we conducted a count of all properties with fewer than 365 available days, which totaled 8,350. Consequently, the remaining 37 properties have not been rented at all and are utilized as residential housing.

### 5.How many hotel rooms should be built if Amsterdam wants to accommodate the same number of tourists?

### 6.How many different licenses are issued?

```ruby
plt.close("all") 
num = [] 
name = [] 
airbnb_list = airbnb.transpose() 
airbnb1 = airbnb_list.values.tolist() 
def find_duplicates(lst): 
    return list(set([x for x in lst if lst.count(x) > 1])) 
house_type = find_duplicates(airbnb1[8]) 
print(house_type) 
for i in house_type: 
    #print(str(i[0])) 
    sublist = airbnb.loc[airbnb['room_type'] == str(i)] 
    num.append(sublist.shape[0]) 
    name.append(str(i)) 
plt.barh(name, num) 
plt.show()
```

In the Airbnb dataset, the last column contains license data, but understanding the types of licenses requires knowledge of the patterns associated with these licenses. After investigation, we determined that the types of licenses correspond to different room types. Therefore, the statistics on license types can be simplified into statistics on room type categories. The final results are illustrated in Figure 3. 

![license types](/images/Figure_7.png) 
<p style="text-align: center;"> <span style="color:grey"> $\small (Figure 3, the statistics on license types)$ </span> </p>
