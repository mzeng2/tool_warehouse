import pandas as pd 
import geopandas as gpd
from shapely.geometry import Polygon

df0 = pd.read_csv('your_csv.csv',encoding='gb18030')

block_id = df0['ID']

df_layer = pd.DataFrame()

for j in range(len(block_id)):

    df_tmp1 = df0.iloc[j,0:3]
    df_tmp1['coordination'] = df_tmp1['lng_lat'].split(';')

    cord_list = df_tmp1['coordination']

    for k in range(len(cord_list)):
        data = {'id':df_tmp1['ID'],'block_name': df_tmp1['name'],'coordination': cord_list[k]}
        df_tmp2 = pd.DataFrame(data,index=[0])

        df_layer = pd.concat([df_layer,df_tmp2])

df_layer['lng'] = df_layer['coordination'].astype(str).str.split(',').str[0]
df_layer['lat'] = df_layer['coordination'].astype(str).str.split(',').str[1]

df_out = df_layer.groupby(['id','block_name']).apply(lambda df: Polygon([(x,y) for x, y in zip(df['lng'],df['lat'])])).to_frame(name = 'geometry')

df_out = gpd.GeoDataFrame(df_out, crs = 'EPSG:4326')
    
df_out.to_file('your_shapefile.shp',encoding='gb18030')