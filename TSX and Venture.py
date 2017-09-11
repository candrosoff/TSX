


#some tsx and tsx venture summary data and plots for September 8 2017

import pandas as pd
import csv
df=pd.read_csv("mig_report.csv")

df.sort_values(["Sector"])
sectors=df["Sector"]
import matplotlib.pyplot as plt

sector_groups=df.groupby(sectors)
sector_groups_count=sector_groups["Sector"].count()
#print(sector_groups_count)
explode = (.1, .1, .1,.1,.1,.1,.1,.1,.1,.1,.1,.1)
sector_groups_count.plot.pie(autopct='%1.1f%%',explode=explode,figsize=(10,10))
plt.show()




market_cap=sector_groups.sum()
explode = (.1, .1, .1,.1,.1,.1,.1,.1,.1,.1,.1,.1)
market_cap["QMV($)"].plot.pie(explode=explode,figsize=(10,10),autopct='%1.1f%%')
plt.show()



hq_location=df.groupby("HQ Location")
hq=hq_location["HQ Location"].count()
hq.plot.bar(figsize=(12,4))
plt.show()



#now showing only Canadian locations


province=["AB","BC","ON","MB","NL","NB","QC","SK","PE"]
prov_hq=hq[hq.index.isin(province)]
prov_hq=prov_hq.sort_values(ascending=True)

prov_hq.plot.bar(figsize=(12,4),color="red")

plt.show()
