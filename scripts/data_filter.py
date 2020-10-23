#%%
import pandas as pd

data_df = pd.read_csv('Police_Department_Incident_Reports__2018_to_Present.csv')
parking_meter_df = pd.read_csv('Parking_Meters.csv')
# %%
filtered_data_df = data_df.filter(['Incident Datetime', 'Incident Description', 'Analysis Neighborhood', 'Intersection', 'point'], axis=1)
filtered_data_df = filtered_data_df.loc[[desc.startswith('Vehicle, Stolen') for desc in filtered_data_df['Incident Description']], :]
filtered_data_df.to_csv('Filtered_Incident_Report.csv')
# %%
filtered_parking_meter_df = parking_meter_df.filter(['PARKING_SPACE_ID', 'POST_ID', 'ACTIVE_METER_FLAG', 'STREET_NAME', 'shape'], axis=1)
filtered_parking_meter_df = filtered_parking_meter_df[filtered_parking_meter_df['ACTIVE_METER_FLAG']=='M']
filtered_parking_meter_df.drop(['ACTIVE_METER_FLAG'], axis=1, inplace=True)
filtered_parking_meter_df.to_csv('Filtered_Parking_Meter.csv')