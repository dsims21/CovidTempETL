import pandas as pd


colnames=['station_id', 'date', 'observation_type', 'observation_value']
weatherDF = pd.read_csv("2020.csv", usecols=[0,1,2,3], names=colnames, header=None)

stationsDF = pd.read_csv("ground_station_custom_locations_world.csv",)

covidDF = pd.read_csv("us-counties.csv",)



for index, row in weatherDF.iterrows():
    weatherDF.loc[weatherDF.index[index], 'Country'] = 1