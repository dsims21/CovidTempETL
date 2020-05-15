import pandas as pd
from datetime import datetime

def convert_to_date(inputDate):
    date = datetime.strptime(str(inputDate), '%Y%m%d')
    return datetime.strftime(date,'%Y-%m-%d')


colnames=['station_id', 'date', 'observation_type', 'observation_value']
weatherDF = pd.read_csv("2020.csv", usecols=[0,1,2,3], names=colnames, header=None)

stationsDF = pd.read_csv("ground_station_custom_locations_world.csv",)

covidDF = pd.read_csv("us-counties.csv",)



#Changing date format to match other files.
#There's probably a better way to do this.
#weatherDF['date'] = weatherDF['date'].apply(convert_to_date)
for index, row in weatherDF.iterrows():
    date = datetime.strptime(str(weatherDF.loc[weatherDF.index[index], 'date']), '%Y%m%d')
    weatherDF.loc[weatherDF.index[index], 'date'] = datetime.strftime(date,'%Y-%m-%d')

print('hi')
