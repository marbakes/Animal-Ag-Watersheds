import geopandas as gpd
import fiona
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from shapely.geometry import Polygon
from mpl_toolkits.axes_grid1 import make_axes_locatable
import warnings
warnings.filterwarnings('ignore', 'GeoSeries.notna', UserWarning)

hucs = gpd.read_file("Data/Sources/WBD_National_GDB.gdb", driver='FileGDB', layer='WBDHU6')

counties = gpd.read_file("Data/Sources/tl_2017_us_county")

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
usa = world[world['iso_a3'] == 'USA']
usac = gpd.clip(usa, Polygon([(-130, 20), (-130, 55), (-60, 55), (-60, 20), (-130, 20)]))

hucs_clipped = hucs.copy()

hucs_clipped = hucs.copy()
for i in hucs_clipped.index:
    try:
        if gpd.clip(hucs_clipped.loc[[i]], usac).shape[0] == 0:
            hucs_clipped.drop(i, inplace = True)
        else:
            hucs_clipped.loc[[i]] = gpd.clip(hucs_clipped.loc[[i]], usac)
    except:
        pass
counties_clipped = gpd.clip(counties, usac)

def counties_map(df_file, plot_title, density = True, state_col = 'STATE_ANSI', county_col = 'COUNTY_ANSI', value_col = 'VALUE', colormap = 'magma'):
    df = pd.read_csv(df_file, dtype = 'str')
    df[value_col] = df[value_col].astype(float)
    
    if density:
        full_gdf = gpd.GeoDataFrame(pd.merge(left = df[[state_col, county_col, value_col]],
        right = counties_clipped[['STATEFP', 'COUNTYFP', 'geometry', 'ALAND', 'AWATER']],
        left_on = [state_col, county_col],
        right_on = ['STATEFP', 'COUNTYFP'],
        how = 'inner'))
        full_gdf['SQKM'] = (full_gdf['ALAND'] + full_gdf['AWATER']) / 1000000
        full_gdf[value_col] = full_gdf[value_col] / full_gdf['SQKM']
        vmax = full_gdf[value_col].quantile(0.99)
    else:
        vmax = df[value_col].quantile(0.99)

    for year in df['YEAR'].unique():

        fig, ax = plt.subplots(1, 1, figsize = (14, 12))

        divider = make_axes_locatable(ax)

        cax = divider.append_axes("right", size="3%", pad=0.03)

        usac.plot(color = plt.get_cmap(colormap)(0), linewidth = 0.1, ax = ax)
        gdf = gpd.GeoDataFrame(pd.merge(left = df.loc[df['YEAR'] == year, [state_col, county_col, value_col]],
        right = counties_clipped[['STATEFP', 'COUNTYFP', 'geometry', 'ALAND', 'AWATER']],
        left_on = [state_col, county_col],
        right_on = ['STATEFP', 'COUNTYFP'],
        how = 'inner'))
        
        if density:
            gdf['SQKM'] = (gdf['ALAND'] + gdf['AWATER']) / 1000000
            gdf[value_col] = gdf[value_col] / gdf['SQKM']
        
        gdf.plot(column = value_col, legend = True, vmin = 0, vmax = vmax, cmap = colormap, ax = ax, cax = cax)
        ax.axis('off')
        if density:
            plt.suptitle(f"{plot_title} per Square Kilometer, by County, {year}", fontsize = '16', y = 0.8)
        else:            
            plt.suptitle(f"{plot_title} by County, {year}", fontsize = '16', y = 0.8)
        plt.tight_layout()
        plt.savefig(f'Plots/Maps/{plot_title}County{year}.jpg')
        plt.close()

def watersheds_map(df_file, plot_title, density = True, huc_col = 'HUC', value_col = 'total', colormap = 'magma', quantile = 0.99):
    df = pd.read_csv(df_file, dtype = 'str')
    df[value_col] = df[value_col].astype(float)
    
    if density:
        full_gdf = gpd.GeoDataFrame(pd.merge(left = df,
        right = hucs_clipped[['HUC6', 'geometry', 'AREASQKM']],
        left_on = ['HUC'],
        right_on = ['HUC6'],
        how = 'inner'))
        full_gdf[value_col] = full_gdf[value_col] / full_gdf['AREASQKM']
        vmax = full_gdf[value_col].quantile(quantile)
        
    else:
        vmax = df[value_col].quantile(quantile)
    
    for year in df['YEAR'].unique():

        fig, ax = plt.subplots(1, 1, figsize = (14, 12))

        divider = make_axes_locatable(ax)

        cax = divider.append_axes("right", size="3%", pad=0.03)

        usac.plot(color = plt.get_cmap(colormap)(0), linewidth = 0.1, ax = ax)
        hucs_clipped.boundary.plot(color = 'w', linewidth = 0.2, ax = ax)
        gdf = gpd.GeoDataFrame(pd.merge(left = df.loc[df['YEAR'] == year],
        right = hucs_clipped[['HUC6', 'geometry', 'AREASQKM']],
        left_on = ['HUC'],
        right_on = ['HUC6'],
        how = 'inner'))
        if density:
            gdf[value_col] = gdf[value_col] / gdf['AREASQKM']
        gdf.plot(column = value_col, legend = True, vmin = 0, vmax = vmax, cmap = colormap, ax = ax, cax = cax)
        ax.axis('off')
        if density:
            plt.suptitle(f"{plot_title} per Square Kilometer, by Watershed, {year}", fontsize = '16', y = 0.8)
        else:
            plt.suptitle(f"{plot_title}, by Watershed, {year}", fontsize = '16', y = 0.8)
        plt.tight_layout()
        plt.savefig(f'Plots/Maps/{plot_title}WatershedDensity{year}.jpg')
        plt.close()