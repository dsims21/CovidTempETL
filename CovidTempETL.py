import pandas as pd
from datetime import datetime

def convert_to_date(inputDate):
    date = datetime.strptime(str(inputDate), '%Y%m%d')
    return datetime.strftime(date,'%Y-%m-%d')

colnames=['station_id', 'date', 'observation_type', 'observation_value']
weatherDF = pd.read_csv("2020.csv", usecols=[0,1,2,3], names=colnames, header=None)

stationsDF = pd.read_csv("ground_station_custom_locations_world.csv",)
filter = stationsDF["Country"]=="United States of America"
stationsDF.where(filter, inplace = True)
stationsDF.dropna(inplace=True)

url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
covidDF = pd.read_csv(url)

# Add the word 'county' to each row in 'county'
# This is because the weather data has the word 'county'
# and will need to be joined on that column.

covidDF['county'] = covidDF['county'].astype(str) + ' county'

# for index, row in covidDF.iterrows():
#     county = str(covidDF.loc[covidDF.index[index], 'county']) + ' county'
#     covidDF.loc[covidDF.index[index], 'county'] = county

#Changing date format to match other files.
#There's probably a better way to do this.
#weatherDF['date'] = weatherDF['date'].apply(convert_to_date)

for index, row in weatherDF.iterrows():
    date = datetime.strptime(str(weatherDF.loc[weatherDF.index[index], 'date']), '%Y%m%d')
    weatherDF.loc[weatherDF.index[index], 'date'] = datetime.strftime(date,'%Y-%m-%d')




print('Done')
