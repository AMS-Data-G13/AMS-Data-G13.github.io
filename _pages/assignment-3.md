---
layout: archive
title: "Amsterdam Housing"
permalink: /assignment-3/
author_profile: true
---

### 1.What Amsterdam will receive from tourist tax if the event lasts a week and you will have 30.000 visitors?

According to City of Amsterdam, the details of the tourist tax are shown in Figure 1. However, from 2024 the tourist tax will rise to [12. 5%](https://www.amsterdam.nl/en/news/budget-2024/). And according to Statista, we learnt the average cost of an overnight stay in Amsterdam in Figure 2. 

![tourist tax](/images/tourist_tax.jpg) <br>
<span style="color:grey"> (Figure 1, Tourist Tax, resource: [City of Amsterdam](https://www.amsterdam.nl/en/municipal-taxes/tourist-tax-(toeristenbelasting)/)) </span> 

![average price](/images/AverageCost.jpg) <br>
<span style="color:grey"> (Figure 2, Average cost of overnight accommodation in Amsterdam, resource: [statista](https://www.statista.com/statistics/614061/overnight-accommodation-costs-amsterdam-city/)) </span>

As the event will take place in May, we refer to the average price of €294 per night in May 2023, and we assume that all 30,000 visitors will stay at the hotel. Then there will be two limiting scenarios.
* In the first case, each person is in a separate room: <br>
  (294 * 12.5% + 3) * 30000 * 7 = 8,347,500
* The second scenario is where everyone is sharing a room with someone else (double occupancy): <br>
  (294 * 12.5% + 3 * 2) * 15000 * 7 = 4,488,750

It is assumed that Amsterdam will receive between €4,488,750 and €8,347,500 in tourist tax.

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
<p style="text-align: center;"> <span style="color:grey"> (Figure 3, the amount of AirBnB locations per neighbourhood) </span> </p>

After aggregating all the Airbnb listings in Amsterdam by neighborhood, the statistical results we obtained are presented in Figure 3. It is evident that the De Baarsjes-Oud-West area has the highest number of Airbnb listings, while Bijlmer-Oost has the fewest.

### 3.Which street in Amsterdam has the most AirBnB apartments?

```ruby
import pandas as pd
from geopy.geocoders import Nominatim
import csv

airbnb = pd.read_csv('listings.csv') 
geolocator = Nominatim(user_agent="user_name")
Loc = airbnb[['latitude','longitude']]

file = 'location.csv'
header = ['location', 'coordinate']
with open(file,'w',encoding='utf-8',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
        
for i,row in Loc.iterrows(): 
    a = str(row['latitude']) 
    b = str(row['longitude']) 
    address = geolocator.reverse(a+","+b, timeout=None) 
    print(address)
        
    with open(file,'a+',encoding='utf-8',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(address)
        csvfile.close()
```
Part of [csvfile: location](/files/location.csv)

|        | location                                                                                                                                          | coordinate                              |  |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |  |
| 1      | Gemaal Jisperveldstraat, Jisperveldstraat, Noord, Zunderdorp, Amsterdam, Noord-Holland, Nederland, 1024 BC, Nederland                             | (52.401009, 4.9515278047393405)         |  |
| 2      | 82, Zoutkeetsplein, Zeeheldenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1013 MR, Nederland                                                 | (52.3886465, 4.8849671)                 |  |
| 3      | 125, Centrale Groothandelsmarkt, Food Center Amsterdam, West, Amsterdam, Noord-Holland, Nederland, 1051 LJ, Nederland                             | (52.3784157, 4.868362)                  |  |
| 4      | 66E, IJsbaanpad, Zuid, Amsterdam, Noord-Holland, Nederland, 1076 CW, Nederland                                                                    | (52.34091435, 4.8480442456550445)       |  |
| 5      | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland                        | (52.37197895, 4.884726800042784)        |  |
| 6      | 276, Maassluisstraat, Westlandgracht, Nieuw-West, Amsterdam, Noord-Holland, Nederland, 1062 GM, Nederland                                         | (52.3496149, 4.8358018)                 |  |
| 7      | 14, Zanddwarsstraat, Nieuwmarkt/Lastage, Centrum, Amsterdam, Noord-Holland, Nederland, 1011 HP, Nederland                                         | (52.370323, 4.899345)                   |  |
| 8      | Van Gessel Advocaten, 7, Amstelveld, Grachtengordel, Centrum, Amsterdam, Noord-Holland, Nederland, 1017 JD, Nederland                             | (52.3625768, 4.8980901)                 |  |
| 9      | Soembawastraat, Indische Buurt, Oost, Amsterdam, Noord-Holland, Nederland, 1095 VW, Nederland                                                     | (52.3644253, 4.943545118223069)         |  |
| 10     | 617, Keizersgracht, Grachtengordel, Centrum, Amsterdam, Noord-Holland, Nederland, 1017 DS, Nederland                                              | (52.3639102, 4.8938953)                 |  |
| 11     | 856, Westerdok, Centrum, Amsterdam, Noord-Holland, Nederland, 1013 BV, Nederland                                                                  | (52.3874861, 4.8920172)                 |  |
| 12     | 22, Heiligeweg, Centrum, Amsterdam, Noord-Holland, Nederland, 1012 XR, Nederland                                                                  | (52.3677894, 4.8909156)                 |  |
| 13     | Lewben Netherlands, 493, Herengracht, Gouden Bocht, Grachtengordel, Centrum, Amsterdam, Noord-Holland, Nederland, 1017 BT, Nederland              | (52.3656512, 4.8911304)                 |  |
| 14     | Het Scheepvaartmuseum, 1, Kattenburgerplein, Marineterrein, Oostelijke Eilanden, Centrum, Amsterdam, Noord-Holland, Nederland, 1018 KK, Nederland | (52.371676699999995, 4.915223006504673) |  |
| 15     | Van Nijenrodeweg, Buitenveldert, Zuid, Amsterdam, Noord-Holland, Nederland, 1083 CL, Nederland                                                    | (52.32783930581986, 4.8768000120565125) |  |
| 16     | 7-1, Binnen Brouwersstraat, Haarlemmerbuurt, Centrum, Amsterdam, Noord-Holland, Nederland, 1013 EE, Nederland                                     | (52.3802642, 4.8908935)                 |  |
| 17     | 174-1A, Czaar Peterstraat, Czaar Peterbuurt, Oostelijke Eilanden, Centrum, Amsterdam, Noord-Holland, Nederland, 1018 PX, Nederland                | (52.3711863, 4.9314646)                 |  |
| 18     | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland                        | (52.37197895, 4.884726800042784)        |  |
| 19     | 121, Lumierestraat, IJburg, Oost, Amsterdam, Noord-Holland, Nederland, 1087 JA, Nederland                                                         | (52.3556276, 5.0032216)                 |  |
| 20     | 40G, Nicolaas Witsenkade, Centrum, Amsterdam, Noord-Holland, Nederland, 1017 ZV, Nederland                                                        | (52.35805575, 4.897501820666131)        |  |
| \`\`\` | \`\`\`                                                                                                                                            | \`\`\`                                  |  |
| 8367   | Kees Boekestraat, Frankendael, Oost, Amsterdam, Noord-Holland, Nederland, 1097 ED, Nederland                                                      | (52.34626555, 4.9216897336955725)       |  |
| 8368   | Venetiestraat, KNSM-eiland, Oostelijk Havengebied, Oost, Schellingwoude, Amsterdam, Noord-Holland, Nederland, 1019 NH, Nederland                  | (52.3770188759731, 4.946660318306404)   |  |
| 8369   | 52-2, Cornelis Trooststraat, Nieuwe Pijp, De Pijp, Zuid, Amsterdam, Noord-Holland, Nederland, 1072 JH, Nederland                                  | (52.3505252, 4.8890981)                 |  |
| 8370   | Magerhorst, Buitenveldert, Zuid, Amsterdam, Noord-Holland, Nederland, 1082 VA, Nederland                                                          | (52.33292437719005, 4.873597096865072)  |  |
| 8371   | 108-H, Nieuwe Kerkstraat, Weesperbuurt, Centrum, Amsterdam, Noord-Holland, Nederland, 1018 VM, Nederland                                          | (52.36435, 4.9069721)                   |  |
| 8372   | 2-1, Sluisstraat, Schinkelbuurt, Zuid, Amsterdam, Noord-Holland, Nederland, 1075 TE, Nederland                                                    | (52.3526631, 4.8557258)                 |  |
| 8373   | A'DAM Toren, 5, Overhoeksplein, Overhoeks, Noord, Amsterdam, Noord-Holland, Nederland, 1031 KS, Nederland                                         | (52.38377245, 4.902137831559482)        |  |
| 8374   | 101, Houthavenkade, Houthaven, West, Amsterdam, Noord-Holland, Nederland, 1014 ZB, Nederland                                                      | (52.3957477, 4.8799986)                 |  |
| 8375   | 16-1, Stolwijkstraat, Hoofddorperpleinbuurt, Zuid, Amsterdam, Noord-Holland, Nederland, 1059 XW, Nederland                                        | (52.3509847, 4.8482898)                 |  |
| 8376   | 35C, Kazernestraat, Centrum, Amsterdam, Noord-Holland, Nederland, 1018 CC, Nederland                                                              | (52.3644442, 4.9213587)                 |  |
| 8377   | 70, Van Swindendwarsstraat, Dapperbuurt, Oost, Amsterdam, Noord-Holland, Nederland, 1093 ZA, Nederland                                            | (52.3610996, 4.9257394)                 |  |
| 8378   | 119-1A, Spaarndammerstraat, Spaarndammerbuurt, West, Amsterdam, Noord-Holland, Nederland, 1013 TE, Nederland                                      | (52.3907436, 4.878113)                  |  |
| 8379   | Bos en Lommerplantsoen, Erasmuspark, West, Amsterdam, Noord-Holland, Nederland, 1055 SC, Nederland                                                | (52.37620198385094, 4.845430591553929)  |  |
| 8380   | 42-4, Sarphatipark, De Pijp, Zuid, Amsterdam, Noord-Holland, Nederland, 1073 CZ, Nederland                                                        | (52.3531466, 4.8948963)                 |  |
| 8381   | 43A, Transvaalstraat, Transvaalbuurt, Oost, Amsterdam, Noord-Holland, Nederland, 1092 HC, Nederland                                               | (52.3551787, 4.926256)                  |  |
| 8382   | 225A, Johan van Hasseltkade, Noord, Amsterdam, Noord-Holland, Nederland, 1032 LP, Nederland                                                       | (52.394626900000006, 4.906245857100501) |  |
| 8383   | 37A-1, Meidoornplein, Volewijck, Noord, Amsterdam, Noord-Holland, Nederland, 1031 GB, Nederland                                                   | (52.3880403, 4.9110192)                 |  |
| 8384   | Natuur is leuk, Brettenpad, Sloterdijk, West, Amsterdam, Noord-Holland, Nederland, 1014 BG, Nederland                                             | (52.3864113, 4.848104)                  |  |
| 8385   | Hotel Doria, Pijlsteeg, Burgwallen-Oude Zijde, Centrum, Amsterdam, Noord-Holland, Nederland, 1012 JL, Nederland                                   | (52.3724267, 4.894502)                  |  |
| 8386   | Eemsstraat, Rijnbuurt, Zuid, Amsterdam, Noord-Holland, Nederland, 1079 BS, Nederland                                                              | (52.34204645, 4.909319813263932)        |  |

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
