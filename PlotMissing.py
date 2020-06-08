import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def data_holes(filename, title):

    df = pd.read_csv(filename)
    
    if 'AGG_LEVEL_DESC' in df.columns:
    
        county_rows = df[df['AGG_LEVEL_DESC'] == 'COUNTY']
    
    else:
        county_rows = df

    rep_df = pd.DataFrame(pd.read_csv('Data/Sources/qs.animals_products_20200516.txt', sep='\t', dtype = 'str').groupby('STATE_NAME').nunique()['COUNTY_NAME']).reset_index().rename(columns = {'COUNTY_NAME': 'all_counties'})

    for year in county_rows.groupby('YEAR').nunique().sort_index().index.values:

        cy = pd.merge(left = rep_df.copy(),
                 right = pd.DataFrame(county_rows.loc[county_rows['YEAR'] == year].groupby('STATE_NAME').nunique()['COUNTY_NAME']).reset_index().rename(columns = {'COUNTY_NAME': 'n_counties'}),
                 on = 'STATE_NAME',
                 how = 'left').fillna(0)

        cy[f'{str(year)}'] = cy['n_counties'] / cy['all_counties']

        rep_df = pd.merge(left = rep_df,
                right = cy[['STATE_NAME', f'{str(year)}']],
                on = 'STATE_NAME',
                how = 'left')

    plt.figure(figsize = (14, 14))
    sns.heatmap(rep_df.set_index('STATE_NAME').drop(index = ['US TOTAL', 'OTHER STATES'], columns = 'all_counties'), cmap = 'bone', vmin = 0, vmax = 1)
    plt.title(f"Proportion of Total Counties Represented by Year\n{title}")
    plt.savefig(f'Plots/data_holes_{title}')
    plt.close()