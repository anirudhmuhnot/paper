from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
from folium import plugins
from folium.plugins import HeatMap
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import folium

#df_traffic = pd.read_csv('../input/ukTrafficAADF.csv')
df_acc = pd.read_csv('/home/anirudhibmgcp2/dashapp/drivingBehaviour/data/accidents_2005_to_2007.csv', dtype=object)

map_hooray = folium.Map(location=[51.5074, 0.1278],
                    zoom_start = 13)

# Ensure you're handing it floats
df_acc['Latitude'] = df_acc['Latitude'].astype(float)
df_acc['Longitude'] = df_acc['Longitude'].astype(float)

# Filter the DF for rows, then columns, then remove NaNs
heat_df = df_acc[df_acc['Speed_limit']=='30'] # Reducing data size so it runs faster
heat_df = heat_df[heat_df['Year']=='2007'] # Reducing data size so it runs faster
heat_df = heat_df[['Latitude', 'Longitude']]
heat_df = heat_df.dropna(axis=0, subset=['Latitude','Longitude'])

# List comprehension to make out list of lists
heat_data = [[row['Latitude'],row['Longitude']] for index, row in heat_df.iterrows()]
# Plot it on the map
HeatMap(heat_data).add_to(map_hooray)

#convert for Iframe
mapp = map_hooray.get_root().render()

layout = html.Div(className='container',style={},children=[
        html.H4(className='blue-text',children=['Accident hotspots in UK']),
        html.Center(html.Iframe(srcDoc=mapp,style={'min-height':'55vh','width':'100%','border':'black'})),
        html.Br(),
        html.H3(className='blue-text',children=['London Live feed and predicted hotspots(by Lokesh Dangi)'])
        ])

