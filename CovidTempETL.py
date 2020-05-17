import pandas as pd
from datetime import datetime

counter  =0

def convert_to_date(inputDate):
    date = datetime.strptime(str(inputDate), '%Y%m%d')
    global counter
    counter += 1
    print(counter)
    return datetime.strftime(date,'%Y-%m-%d')


### EXTRACT ##

# Weather
colnames=['station_id', 'date', 'observation_type', 'observation_value']
weatherDF = pd.read_csv("2020.csv", usecols=[0,1,2,3], names=colnames, header=None)

# Ground Stations
stationsDF = pd.read_csv("ground_station_custom_locations_world.csv",)

# Covid19 Cases/Deaths by State/County
url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
covidDF = pd.read_csv(url)

### TRANSFORM ###

# Adding the word 'county' to match other files.
covidDF['county'] = covidDF['county'].astype(str) + ' county'

# Changing date format to match other files.
# (This currently takes a long time.)
weatherDF['date'] = weatherDF['date'].apply(convert_to_date)


### Filter ###

# Filter Stations to US only
filter = stationsDF["Country"]=="United States of America"
stationsDF.where(filter, inplace = True)
stationsDF.dropna(inplace=True)


### AGGREGATE ### (Do we need to so some averaging of temps?)


### JOIN ###

#Start by left joining
joinedDF = weatherDF.merge(stationsDF, left_on='station_id', right_on='ID')

print('Done')
