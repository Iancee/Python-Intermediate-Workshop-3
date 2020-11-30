#Script to back up feature layer as csv

from datetime import date
from arcgis import gis, features

import getpass

today = date.today().strftime('%Y%m%d')

username = 'Ian_Conroy_LearnArcGIS'

password = getpass.getpass()

print('Connecting to AGOL')
#Connect to AGOL org
gis = gis.GIS('https://learngis2.maps.arcgis.com', username, password)

#Set to feature service URL
#*****************************************************************************************************************************************************
f_lyr_URL = "https://services3.arcgis.com/U26uBjSD32d7xvm2/arcgis/rest/services/SF_GIS_Data/FeatureServer/0"
#*****************************************************************************************************************************************************

print('Creating feature layer and spatial dataframe')
#Create feature layer of feature services
f_lyr = features.FeatureLayer(f_lyr_URL, gis)

#Create spatial dataframes
f_lyr_sdf = features.GeoAccessor.from_layer(f_lyr)

print('Exporting spatial dataframe as a csv file')
#Export spatial dataframes as csv files
#********************************************************************************************************************
f_lyr_sdf.to_csv(r"C:\Users\ian.conroy\Desktop\Bay Geo Classes\Python Class\Intermediate Class Fall\Output_Folder\BikeRoutesBackup_{}.csv".format(today))
#********************************************************************************************************************
