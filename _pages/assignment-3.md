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

Average cost of overnight accommodation in Amsterdam in the Netherlands from January 2019 to June 2023(in euros)

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

# import airbnb data
airbnb = pd.read_csv('listings.csv')

# calculate the number of rooms for each neighbourhood
neighbourhood = airbnb.neighbourhood.value_counts()

# plotting the result
fig = px.bar(neighbourhood, y='count', text_auto=True)
fig.show()
```
![neighbourhood](/images/newplot.png) 
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

#Get a specific address based on latitude and longitude
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

Here is part of [csvfile: location](/files/location.csv):

<div class="table-wrapper" markdown="block">
  
|      | location                                                                                                                                          | coordinate                              |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| 1    | Gemaal Jisperveldstraat, Jisperveldstraat, Noord, Zunderdorp, Amsterdam, Noord-Holland, Nederland, 1024 BC, Nederland                             | (52.401009, 4.9515278047393405)         |
| 2    | 82, Zoutkeetsplein, Zeeheldenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1013 MR, Nederland                                                 | (52.3886465, 4.8849671)                 |
| 3    | 125, Centrale Groothandelsmarkt, Food Center Amsterdam, West, Amsterdam, Noord-Holland, Nederland, 1051 LJ, Nederland                             | (52.3784157, 4.868362)                  |
| 4    | 66E, IJsbaanpad, Zuid, Amsterdam, Noord-Holland, Nederland, 1076 CW, Nederland                                                                    | (52.34091435, 4.8480442456550445)       |
| 5    | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland                        | (52.37197895, 4.884726800042784)        |
| 6    | 276, Maassluisstraat, Westlandgracht, Nieuw-West, Amsterdam, Noord-Holland, Nederland, 1062 GM, Nederland                                         | (52.3496149, 4.8358018)                 |
| 7    | 14, Zanddwarsstraat, Nieuwmarkt/Lastage, Centrum, Amsterdam, Noord-Holland, Nederland, 1011 HP, Nederland                                         | (52.370323, 4.899345)                   |
| 8    | Van Gessel Advocaten, 7, Amstelveld, Grachtengordel, Centrum, Amsterdam, Noord-Holland, Nederland, 1017 JD, Nederland                             | (52.3625768, 4.8980901)                 |
| 9    | Soembawastraat, Indische Buurt, Oost, Amsterdam, Noord-Holland, Nederland, 1095 VW, Nederland                                                     | (52.3644253, 4.943545118223069)         |
| 10   | 617, Keizersgracht, Grachtengordel, Centrum, Amsterdam, Noord-Holland, Nederland, 1017 DS, Nederland                                              | (52.3639102, 4.8938953)                 |
| 11   | 856, Westerdok, Centrum, Amsterdam, Noord-Holland, Nederland, 1013 BV, Nederland                                                                  | (52.3874861, 4.8920172)                 |
| 12   | 22, Heiligeweg, Centrum, Amsterdam, Noord-Holland, Nederland, 1012 XR, Nederland                                                                  | (52.3677894, 4.8909156)                 |
| 13   | Lewben Netherlands, 493, Herengracht, Gouden Bocht, Grachtengordel, Centrum, Amsterdam, Noord-Holland, Nederland, 1017 BT, Nederland              | (52.3656512, 4.8911304)                 |
| 14   | Het Scheepvaartmuseum, 1, Kattenburgerplein, Marineterrein, Oostelijke Eilanden, Centrum, Amsterdam, Noord-Holland, Nederland, 1018 KK, Nederland | (52.371676699999995, 4.915223006504673) |
| 15   | Van Nijenrodeweg, Buitenveldert, Zuid, Amsterdam, Noord-Holland, Nederland, 1083 CL, Nederland                                                    | (52.32783930581986, 4.8768000120565125) |
| 16   | 7-1, Binnen Brouwersstraat, Haarlemmerbuurt, Centrum, Amsterdam, Noord-Holland, Nederland, 1013 EE, Nederland                                     | (52.3802642, 4.8908935)                 |
| 17   | 174-1A, Czaar Peterstraat, Czaar Peterbuurt, Oostelijke Eilanden, Centrum, Amsterdam, Noord-Holland, Nederland, 1018 PX, Nederland                | (52.3711863, 4.9314646)                 |
| 18   | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland                        | (52.37197895, 4.884726800042784)        |
| 19   | 121, Lumierestraat, IJburg, Oost, Amsterdam, Noord-Holland, Nederland, 1087 JA, Nederland                                                         | (52.3556276, 5.0032216)                 |
| 20   | 40G, Nicolaas Witsenkade, Centrum, Amsterdam, Noord-Holland, Nederland, 1017 ZV, Nederland                                                        | (52.35805575, 4.897501820666131)        |
| ···  | ···                                                                                                                                               | ···                                     |
| 8367 | Kees Boekestraat, Frankendael, Oost, Amsterdam, Noord-Holland, Nederland, 1097 ED, Nederland                                                      | (52.34626555, 4.9216897336955725)       |
| 8368 | Venetiestraat, KNSM-eiland, Oostelijk Havengebied, Oost, Schellingwoude, Amsterdam, Noord-Holland, Nederland, 1019 NH, Nederland                  | (52.3770188759731, 4.946660318306404)   |
| 8369 | 52-2, Cornelis Trooststraat, Nieuwe Pijp, De Pijp, Zuid, Amsterdam, Noord-Holland, Nederland, 1072 JH, Nederland                                  | (52.3505252, 4.8890981)                 |
| 8370 | Magerhorst, Buitenveldert, Zuid, Amsterdam, Noord-Holland, Nederland, 1082 VA, Nederland                                                          | (52.33292437719005, 4.873597096865072)  |
| 8371 | 108-H, Nieuwe Kerkstraat, Weesperbuurt, Centrum, Amsterdam, Noord-Holland, Nederland, 1018 VM, Nederland                                          | (52.36435, 4.9069721)                   |
| 8372 | 2-1, Sluisstraat, Schinkelbuurt, Zuid, Amsterdam, Noord-Holland, Nederland, 1075 TE, Nederland                                                    | (52.3526631, 4.8557258)                 |
| 8373 | A'DAM Toren, 5, Overhoeksplein, Overhoeks, Noord, Amsterdam, Noord-Holland, Nederland, 1031 KS, Nederland                                         | (52.38377245, 4.902137831559482)        |
| 8374 | 101, Houthavenkade, Houthaven, West, Amsterdam, Noord-Holland, Nederland, 1014 ZB, Nederland                                                      | (52.3957477, 4.8799986)                 |
| 8375 | 16-1, Stolwijkstraat, Hoofddorperpleinbuurt, Zuid, Amsterdam, Noord-Holland, Nederland, 1059 XW, Nederland                                        | (52.3509847, 4.8482898)                 |
| 8376 | 35C, Kazernestraat, Centrum, Amsterdam, Noord-Holland, Nederland, 1018 CC, Nederland                                                              | (52.3644442, 4.9213587)                 |
| 8377 | 70, Van Swindendwarsstraat, Dapperbuurt, Oost, Amsterdam, Noord-Holland, Nederland, 1093 ZA, Nederland                                            | (52.3610996, 4.9257394)                 |
| 8378 | 119-1A, Spaarndammerstraat, Spaarndammerbuurt, West, Amsterdam, Noord-Holland, Nederland, 1013 TE, Nederland                                      | (52.3907436, 4.878113)                  |
| 8379 | Bos en Lommerplantsoen, Erasmuspark, West, Amsterdam, Noord-Holland, Nederland, 1055 SC, Nederland                                                | (52.37620198385094, 4.845430591553929)  |
| 8380 | 42-4, Sarphatipark, De Pijp, Zuid, Amsterdam, Noord-Holland, Nederland, 1073 CZ, Nederland                                                        | (52.3531466, 4.8948963)                 |
| 8381 | 43A, Transvaalstraat, Transvaalbuurt, Oost, Amsterdam, Noord-Holland, Nederland, 1092 HC, Nederland                                               | (52.3551787, 4.926256)                  |
| 8382 | 225A, Johan van Hasseltkade, Noord, Amsterdam, Noord-Holland, Nederland, 1032 LP, Nederland                                                       | (52.394626900000006, 4.906245857100501) |
| 8383 | 37A-1, Meidoornplein, Volewijck, Noord, Amsterdam, Noord-Holland, Nederland, 1031 GB, Nederland                                                   | (52.3880403, 4.9110192)                 |
| 8384 | Natuur is leuk, Brettenpad, Sloterdijk, West, Amsterdam, Noord-Holland, Nederland, 1014 BG, Nederland                                             | (52.3864113, 4.848104)                  |
| 8385 | Hotel Doria, Pijlsteeg, Burgwallen-Oude Zijde, Centrum, Amsterdam, Noord-Holland, Nederland, 1012 JL, Nederland                                   | (52.3724267, 4.894502)                  |
| 8386 | Eemsstraat, Rijnbuurt, Zuid, Amsterdam, Noord-Holland, Nederland, 1079 BS, Nederland                                                              | (52.34204645, 4.909319813263932)        |

</div>

We can see that not all addresses have the same format, but the second last position is the postcode, so we're going to extract the postcode information for each address.

```ruby
import pandas as pd
from collections import Counter

#Get the postcode from the address
Location = pd.read_csv('location.csv') 
street = []
for i, row in Location.iterrows():
    Location_split = row[1].split(',')
    street.append(Location_split[-2]) 

#Counting which postcodes appear most often
count = Counter(street)
postcode = pd.DataFrame(count, index=[0])
postcode.to_csv('postcode.csv', index=False)
```

Here are the top five [postcodes](/files/postcode.csv) in terms of occurrences:

| postcode | count |
| -------- | ----- |
|  1052 CH | 175   |
|  1012 AR | 47    |
|  1015 RR | 24    |
|  1011 TE | 21    |
|  1015 HJ | 20    |

We can see that 1052 CH appears 175 times far more than any other postcode. Next we will look at which addresses are at 1052 CH.

```ruby
#Filter out addresses containing the most frequently occurring postcodes
df = pd.DataFrame(street)
#To eliminate spaces in the postcode
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
```

These are the AirBnb's at [1052CH](/files/StreetName.csv):

|     | num  | location                                                                                                                   | coordinate                              | post | code |
| --- | ---- | -------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- | ---- | ---- |
| 1   | 5    | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 2   | 18   | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 3   | 24   | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 4   | 41   | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 5   | 46   | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 6   | 151  | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 7   | 320  | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 8   | 379  | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 9   | 386  | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 10  | 388  | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 11  | 443  | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 12  | 480  | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 13  | 495  | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 14  | 540  | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 15  | 661  | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 16  | 673  | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 17  | 739  | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 18  | 785  | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 19  | 788  | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 20  | 815  | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 21  | 823  | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 22  | 833  | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 23  | 853  | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 24  | 882  | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 25  | 975  | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 26  | 1006 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 27  | 1011 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 28  | 1079 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 29  | 1131 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 30  | 1253 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 31  | 1256 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 32  | 1310 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 33  | 1329 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 34  | 1367 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 35  | 1503 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 36  | 1524 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 37  | 1555 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 38  | 1585 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 39  | 1587 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 40  | 1635 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 41  | 1642 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 42  | 1676 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 43  | 1755 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 44  | 1787 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 45  | 1828 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 46  | 1878 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 47  | 1976 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 48  | 1994 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 49  | 2016 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 50  | 2049 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 51  | 2064 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 52  | 2086 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 53  | 2155 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 54  | 2165 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 55  | 2182 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 56  | 2202 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 57  | 2243 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 58  | 2247 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 59  | 2299 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 60  | 2311 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 61  | 2344 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 62  | 2345 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 63  | 2419 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 64  | 2424 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 65  | 2523 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 66  | 2530 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 67  | 2542 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 68  | 2581 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 69  | 2593 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 70  | 2616 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 71  | 2646 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 72  | 2675 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 73  | 2708 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 74  | 2709 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 75  | 2742 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 76  | 2898 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 77  | 2952 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 78  | 2958 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 79  | 2967 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 80  | 3040 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 81  | 3079 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 82  | 3256 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 83  | 3263 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 84  | 3269 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 85  | 3320 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 86  | 3338 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 87  | 3535 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 88  | 3549 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 89  | 3554 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 90  | 3586 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 91  | 3669 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 92  | 3706 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 93  | 3712 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 94  | 3723 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 95  | 3736 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 96  | 3767 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 97  | 3777 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 98  | 3811 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 99  | 3937 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 100 | 3951 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 101 | 3952 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 102 | 3954 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 103 | 4000 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 104 | 4018 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 105 | 4041 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 106 | 4082 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 107 | 4179 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 108 | 4202 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 109 | 4226 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 110 | 4248 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 111 | 4266 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 112 | 4361 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 113 | 4381 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 114 | 4387 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 115 | 4403 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 116 | 4404 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 117 | 4410 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 118 | 4455 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 119 | 4480 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 120 | 4499 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 121 | 4555 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 122 | 4557 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 123 | 4579 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 124 | 4581 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 125 | 4602 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 126 | 4688 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 127 | 4722 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 128 | 4727 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 129 | 4754 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 130 | 4867 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 131 | 4972 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 132 | 6057 | Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland                               | (52.383978040393785, 4.881098559021044) | 1052 | CH   |
| 133 | 6059 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 134 | 6075 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 135 | 6148 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 136 | 6216 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 137 | 6218 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 138 | 6228 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 139 | 6229 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 140 | 6266 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 141 | 6379 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 142 | 6416 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 143 | 6511 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 144 | 6521 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 145 | 6560 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 146 | 6693 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 147 | 6695 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 148 | 6731 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 149 | 6764 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 150 | 6767 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 151 | 6811 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 152 | 6830 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 153 | 6918 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 154 | 7040 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 155 | 7084 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 156 | 7170 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 157 | 7195 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 158 | 7235 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 159 | 7340 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 160 | 7424 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 161 | 7425 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 162 | 7488 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 163 | 7564 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 164 | 7581 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 165 | 7602 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 166 | 7647 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 167 | 7648 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 168 | 7657 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 169 | 7678 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 170 | 7680 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 171 | 7761 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 172 | 7806 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 173 | 7828 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |
| 174 | 7999 | Grachtengordel van Amsterdam, Nassaukade, Staatsliedenbuurt, West, Amsterdam, Noord-Holland, Nederland, 1052 CH, Nederland | (52.37197895, 4.884726800042784)        | 1052 | CH   |

Obviously the street called Nassaukade has the most Airbnb's.

### 4.Try to cross reference the data from the AirBnB dataset with the BBGA. Can you figure out if all apartments of AirBnB are designated as housing? Which number of apartments are not rented out all the time but are also used as normal housing?

```ruby
import pandas as pd
import matplotlib.pyplot as plt

airbnb = pd.read_csv('listings.csv')
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

# counting the numbers for each room type
count = []
for i in range(4):
    name = house_type[i]
    a = airbnb.query('room_type == @name')
    count.append(len(a))
print(count)
```

```ruby
['Hotel room', 'Entire home/apt', 'Private room', 'Shared room']
[54, 6477, 1813, 42]
```

```ruby
# check the amount of rooms which is available all year
rooms = sum(count)
num_rented = len(airbnb.query('availability_365 < 365'))
normal = rooms - num_rented
print(normal)
```

```
36
```

For this question, we were unsure about how to utilize the BBGA dataset, so all the responses are based on Airbnb data. Among the four room types, hotel rooms are not categorized as housing. Therefore, as an answer to the first question, 54 rooms were not designated as housing. Regarding the second question, we conducted a count of all properties with fewer than 365 available days, which totaled 8,350. Consequently, the remaining 36 properties have not been rented at all and are utilized as residential housing.

### 5.How many hotel rooms should be built if Amsterdam wants to accommodate the same number of tourists?

Referring to the data in Table, we assume that Amsterdam typically receives 786,000 overnight visitors in May. Adding 30,000 people to this number brings the expected number of overnight guests in Amsterdam in May to 816,000, which does not exceed the maximum number of guests Amsterdam can accommodate, so no additional hotel rooms are needed.
|Country of residence|Regions  |Periods       |Guests (x 1 000)|
|--------------------|---------|--------------|----------------|
|All countries       |Amsterdam|2022 September|649             |
|All countries       |Amsterdam|2022 October  |702             |
|All countries       |Amsterdam|2022 November |655             |
|All countries       |Amsterdam|2022 December |605             |
|All countries       |Amsterdam|2023 January* |575             |
|All countries       |Amsterdam|2023 February*|560             |
|All countries       |Amsterdam|2023 March*   |684             |
|All countries       |Amsterdam|2023 April*   |766             |
|All countries       |Amsterdam|2023 May*     |786             |
|All countries       |Amsterdam|2023 June*    |773             |
|All countries       |Amsterdam|2023 July*    |919             |
|All countries       |Amsterdam|2023 August*  |776             |

<span style="color:grey"> (Table, Hotels; guests, overnight stays, country of residence, region. Source: [Statistics Netherlands](https://www.cbs.nl/en-gb/figures/detail/82061ENG?q=amsterdam#shortTableDescription)) </span>

### 6.How many different licenses are issued?

```ruby
import pandas as pd
import matplotlib.pyplot as plt

airbnb = pd.read_csv('listings.csv')

num = [] 
num = []
name = []
airbnb_list = airbnb.transpose()
airbnb1 = airbnb_list.values.tolist()

# define a function to find duplicates
def find_duplicates(lst):
    return list(set([x for x in lst if lst.count(x) > 1]))

# find the duplicate house types
house_type = find_duplicates(airbnb1[8])

# find names and numbers for each house type
for i in house_type:
    # print(str(i[0]))
    sublist = airbnb.loc[airbnb['room_type'] == str(i)]
    num.append(sublist.shape[0])
    name.append(str(i))

# plotting
plt.barh(name, num)
plt.show()
```

In the Airbnb dataset, the last column contains license data, but understanding the types of licenses requires knowledge of the patterns associated with these licenses. After investigation, we determined that the types of licenses correspond to different room types. Therefore, the statistics on license types can be simplified into statistics on room type categories. The final results are illustrated in Figure 4. 

![license types](/images/Figure_7.png) 
<p style="text-align: center;"> <span style="color:grey"> (Figure 4, the statistics on license types) </span> </p>
