# Intensification of Animal Agriculture: Watershed Effects

## Table of Contents

### Introduction
### Executive Summary
### Sources
### Methods
### Conclusions and Recommendations

### Introduction

In the past 30 years, we have seen a sizeable increase in the intensification and industrialization of animal agriculture in the United States. The main effect of this has been the transition from smaller, more distributed family farms to larger, more concentrated feedlot operations. When the distribution of livestock changes, the impacts of the externalities associated with animal agriculture change as well, most notably the ecological impact of having an extreme amount of livestock in a very small concentrated area. Livestock waste contains nutrients, most importantly organic nitrogen and phosphorous, that have the potential to degrade water quality through a process known as eutrophication. Effects include harmful algal blooms, fish kills, dead zones, and general ecological disruption that have caused billions of dollars of damage to property values, fishing, recreation, and tourism industries, and municipal water systems. Long term trends in animal agriculture can be observed from the USDA Census of Agriculture and used to approximate effects on local watersheds.

### Executive Summary

Livestock waste has the potential to cause both local and widespread ecological damage through a process called eutrophication. Waste nutrients that make their way into local waterways can cause ecological, financial, and human health damage to the local community. The business of animal agriculture in the United States has undergone a monumental change in the past 3-4 decades where the amount of distributed smaller operations have been replaced by much larger, centralized operations. In this report, these trends are examined on both the county level and watershed level. The impact of each major type of livestock is evaluated using the USDA Census of Agriculture and Survey of Agriculture data. Very extreme trends of geographical concentration and overall market growth are apparent across all livestock types, however hogs and milk cows present the most extreme cases. Also considered are waterways that contain impaired waters as defined by section 303(d) of the Clean Water Act. The amount of hog and layer chicken waste in a watershed was tied to whether that watershed contains impaired waters (p = 0.03 and p=0.007, respectively). This report provides a high level analysis of trends in animal agribusiness from 1980-2020 and is intended to spread awareness of ecological impacts of animal agriculture as well as open the dialogue for additional investigation into these trends.

### Sources

[USDA Census of Agriculture](ftp://ftp.nass.usda.gov/quickstats/)
[USDA - National Agricultural Statistics Service - Surveys - Cattle Inventory](https://www.nass.usda.gov/Surveys/Guide_to_NASS_Surveys/Cattle_Inventory/)
[USDA - National Agricultural Statistics Service - Surveys - Chickens and Eggs](https://www.nass.usda.gov/Surveys/Guide_to_NASS_Surveys/Chickens_and_Eggs/index.php)
[USDA - National Agricultural Statistics Service - Surveys - Hog Inventory](https://www.nass.usda.gov/Surveys/Guide_to_NASS_Surveys/Hog_Inventory/index.php)
[US Counties TIGER/Line Shapefile, 2017, nation, US, Current County and Equivalent National Shapefile](https://catalog.data.gov/dataset/tiger-line-shapefile-2017-nation-u-s-current-county-and-equivalent-national-shapefile)
[Literature Review of Contaminants in Livestock and Poultry Manure and Implications for Water Quality](https://nepis.epa.gov/Exe/ZyPDF.cgi/P100H2NI.PDF?Dockey=P100H2NI.PDF)
[303(d) Listed Impaired Waters NHDPlus Indexed Dataset with Program Attributes](https://www.epa.gov/waterdata/waters-geospatial-data-downloads#303dListedImpairedWaters)

### Methods

#### Selection

The USDA measures livestock head for each livestock type during it's census every 5 years. Data for additional years is also available from the survey, which occurs annually. These are both aggregated at the county, state, and national level; and beginning in census year 2007 are aggregated by HU6-level watershed. Combining the data from the census and the survey can be used to illustrate long-term trends in livestock head per county.

The following county, state, and national-aggregated columns were selected for each major livestock type:

Beef Cows:

- SURVEY|ANIMALS & PRODUCTS|LIVESTOCK|CATTLE|(EXCL MILK COWS & REPL HEIFERS)|ALL PRODUCTION PRACTICES|ALL UTILIZATION PRACTICES|INVENTORY|HEAD|CATTLE, (EXCL MILK COWS & REPL HEIFERS) - INVENTORY|TOTAL|NOT SPECIFIED
- SURVEY|ANIMALS & PRODUCTS|LIVESTOCK|CATTLE|COWS, BEEF|ALL PRODUCTION PRACTICES|ALL UTILIZATION PRACTICES|INVENTORY|HEAD|CATTLE, COWS, BEEF - INVENTORY|TOTAL|NOT SPECIFIED
- CENSUS|ANIMALS & PRODUCTS|LIVESTOCK|CATTLE|COWS, BEEF|ALL PRODUCTION PRACTICES|ALL UTILIZATION PRACTICES|INVENTORY|HEAD|CATTLE, COWS, BEEF - INVENTORY|TOTAL|NOT SPECIFIED

Milk Cows:

- SURVEY|ANIMALS & PRODUCTS|LIVESTOCK|CATTLE|COWS, MILK|ALL PRODUCTION PRACTICES|ALL UTILIZATION PRACTICES|INVENTORY|HEAD|CATTLE, COWS, MILK - INVENTORY|TOTAL|NOT SPECIFIED
- CENSUS|ANIMALS & PRODUCTS|LIVESTOCK|CATTLE|COWS, MILK|ALL PRODUCTION PRACTICES|ALL UTILIZATION PRACTICES|INVENTORY|HEAD|CATTLE, COWS, MILK - INVENTORY|TOTAL|NOT SPECIFIED
- SURVEY|ANIMALS & PRODUCTS|LIVESTOCK|CATTLE|COWS, MILK|ALL PRODUCTION PRACTICES|ALL UTILIZATION PRACTICES|INVENTORY, AVG|HEAD|CATTLE, COWS, MILK - INVENTORY, AVG, MEASURED IN HEAD|TOTAL|NOT SPECIFIED

Broiler Chickens:

- CENSUS|ANIMALS & PRODUCTS|POULTRY|CHICKENS|BROILERS|ALL PRODUCTION PRACTICES|ALL UTILIZATION PRACTICES|INVENTORY|HEAD|CHICKENS, BROILERS - INVENTORY|TOTAL|NOT SPECIFIED

Layer Chickens:

- SURVEY|ANIMALS & PRODUCTS|POULTRY|CHICKENS|(EXCL BROILERS)|ALL PRODUCTION PRACTICES|ALL UTILIZATION PRACTICES|INVENTORY|HEAD|CHICKENS, (EXCL BROILERS) - INVENTORY|TOTAL|NOT SPECIFIED
- SURVEY|ANIMALS & PRODUCTS|POULTRY|CHICKENS|LAYERS|ALL PRODUCTION PRACTICES|ALL UTILIZATION PRACTICES|INVENTORY, AVG|HEAD|CHICKENS, LAYERS - INVENTORY, AVG, MEASURED IN HEAD|TOTAL|NOT SPECIFIED
- SURVEY|ANIMALS & PRODUCTS|POULTRY|CHICKENS|LAYERS|ALL PRODUCTION PRACTICES|ALL UTILIZATION PRACTICES|INVENTORY|HEAD|CHICKENS, LAYERS - INVENTORY|TOTAL|NOT SPECIFIED
- CENSUS|ANIMALS & PRODUCTS|POULTRY|CHICKENS|LAYERS|ALL PRODUCTION PRACTICES|ALL UTILIZATION PRACTICES|INVENTORY|HEAD|CHICKENS, LAYERS - INVENTORY|TOTAL|NOT SPECIFIED

Hogs:

- SURVEY|ANIMALS & PRODUCTS|LIVESTOCK|HOGS|ALL CLASSES|ALL PRODUCTION PRACTICES|ALL UTILIZATION PRACTICES|INVENTORY|HEAD|HOGS - INVENTORY|TOTAL|NOT SPECIFIED
- CENSUS|ANIMALS & PRODUCTS|LIVESTOCK|HOGS|ALL CLASSES|ALL PRODUCTION PRACTICES|ALL UTILIZATION PRACTICES|INVENTORY|HEAD|HOGS - INVENTORY|TOTAL|NOT SPECIFIED

#### Processing

The USDA census and surveys withhold certain counties from a dataset if the value from that county can be used to identify a single operation. However, these counties can be approximated by taking the remainder of the state total not accounted for in the other counties and dividing it equally among the other counties. This should not skew the overall data too much because the withheld counties have a small amount of operations and thus a small total value. All withheld rows, designated as (D) in this dataset were imputed using this method.

In addition to these withheld values, there were many counties that were missing years and some counties missing entirely from the dataset. It is possible to use relationships both within the data, and across other datasets, to impute these values. The following methods were employed:

1. Linear Relationship Imputation

The value of interest is head inventory by county for each livestock type, and this can be related in a linear fashion to other variables like production, sales etc. For each linear relationship, a linear regression was performed between the variable of interest and the secondary variable, and the coefficient from this regression was used to infer the variable of interests in the counties and/or years where the secondary variable is available. For example, if the data for egg production by county is more complete than the data for layer chicken head by county, the egg production can be divided by a coefficient to infer the layer chicken head where it is missing. The relationships exploited for this type of imputation are as follows:

Beef Cows and Milk Cows:

- Beef cow inventory + milk cow inventory vs. total cattle inventory

Broiler Chickens:

- Broiler chicken inventory vs. broiler chicken production

Layer Chickens:

- Layer chicken inventory vs. egg production

Hogs:

- Hog inventory vs. hog sales
- Hog inventory vs. hog breeding inventory
- Hog inventory vs. hog pig crop

2. Stable Ratio Imputation

In addition to ratios between the value of interest and other measured variables, the ratios within the value of interest across aggregation levels can be used to impute missing values. For counties where that county's contribution to the state total is relatively stable, that ratio can be used to infer the county total where the state total is known. The same logic applies to state contribution to national. Since the state and national data is more complete than the county data, interpolating in this way can easily infer many missing values. For the purposes of this imputation, stable is defined as having a standard deviation of less than 2% in the ratio of county to state or state to nation.

3. Time Series Imputation

In counties where these ratios are not stable as defined above, the values over time must be treated as a time series. For these counties, time series imputation is performed using the Pandas library [.interpolate](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.interpolate.html) function with the "time" method on a time index to ensure appropriate spacing of points. 

#### Reaggregation

Now that we have reasonably complete livestock head by watershed, we can use this to infer the livestock head by watershed. The USDA began aggregating livestock amounts by USGS HUC6-level watershed in 2007 to shed light on the watershed impacts of animal agriculture. Geospatial relationships between counties and watersheds can be exploited to approximate this watershed aggregation allow for examination of long-term trends in livestock head per watershed. This approximation involves taking the head in a county and multiplying it by the portion of the watershed belonging to that county to get the contribution of that county to that watershed. This method of approximation rests on the assumption that livestock are distributed evenly across a county, which may not always be exact. These ratios of watershed belonging to each county were calculated using the GeoPandas library [.overlay](https://geopandas.org/reference/geopandas.overlay.html) method on the shapefiles of the US counties and HUC6 watersheds. All livestock types were reaggregated by watershed using these methods, and the total head was multiplied by the waste generation rate per head to compile the total animal waste per watershed for each year from 1980-2020.

#### Relationships

The total waste per watershed can be plotted using a choropleth map to show the watersheds with the highest nutrient loads per year. Looking across time for the past 40 years, we can see a transition from animal agriculture being most concentrated in midwestern states but being distributed relatively evenly there, to livestock being very concentrated in a select few watersheds. One watershed that appears to increase dramatically over time is in southern California, and contains Tulare County, which is home to an extremely high concentration and size of dairy operations. The other most notable area is a watershed in North Carolina that contains Duplin and Sampson counties, which have become the areas with the highest concentration of hogs in the nation with the pork industry centered there. Overall we can see a very visible trend of animal agriculture moving away from distributed smaller farms to highly concentrated industrial operations.

Section 303(d) of the Clean Water Act authorizes EPA to assist states, territories and authorized tribes in listing impaired waters and developing Total Maximum Daily Loads (TMDLs) for these waterbodies. A TMDL establishes the maximum amount of a pollutant allowed in a waterbody and serves as the starting point or planning tool for restoring water quality. We can examine the relationship between these impaired waters, as defined by section 303(d), and the watersheds most impacted by animal agriculture. For each livestock type we can split the watersheds into those containing impaired waters and those not containing impaired waters, and perform a hypothesis test on the equality of the mean waste per watershed for each group. After performing a t-test on the means for each livestock, layer chickens and hogs were the only two livestock types that have a significant relationship with whether a watershed contains impaired waters.

### Conclusions and Recommendations

With this high-level analysis of animal agriculture waste in watersheds, we were able to illustrate trends and impacts across time as a result of this industry. We were able to observe the concentration of dairy and pork production into a few small areas in the country, and we were able to link egg and pork production to watersheds that contain 303(d)-listed impared waters. The processes by which organic waste degrades waterways is a biological process, and therefore very complex and impacted by a lot of variables. There is significant research into this problem and one can employ a variety of tools to examine the relationships in places. The analysis contained herein lead to a variety of possible questions such as:
- Has animal agriculture reached its saturation point? 
- Will trends continue or reverse in the future?
- Among operations of the same size or in the same area, what practices are most effective to reduce impact on local ecology?
- What role does regulation and local politics play in the location and intensification of animal agriculture?