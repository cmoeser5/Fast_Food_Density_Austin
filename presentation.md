# Fast Food Density in Austin

### Our Questions?
* How does income influence fast food restaurant availabilty?
* What is the correlation between proximity of fast food and health issues?
* What is the correlation between income level and health issues?
* Is there any correlation between education levels and health issues?
* How does race relate to the factors of income and fast food availabilty?

### Hypothesis:

Individuals in low income brackets, low education levels and poor health conditions are closer in proximity to fast food restaurants.

### Data Set:

ACS Income Data: https://data.census.gov/cedsci/table?g=0500000US48453.140000&y=2017&tid=ACSST5Y2017.S1901&hidePreview=false

ACS Race Data: https://data.census.gov/cedsci/table?q=age%20sex%20race&g=0500000US48453.140000&y=2017&tid=ACSDP5Y2017.DP05&hidePreview=false

ACS Sex/Age/Education: https://data.census.gov/cedsci/table?q=18%20and%20over&g=0500000US48453.140000&y=2017&tid=ACSDT5Y2017.B15001&hidePreview=false

CDC Obesity Data: https://chronicdata.cdc.gov/500-Cities/500-Cities-Obesity-among-adults-aged-18-years/bjvu-3y7d

CDC Diabetes Data: https://chronicdata.cdc.gov/500-Cities/500-Cities-Diagnosed-diabetes-among-adults-aged-18/cn78-b9bj

CDC Blood Pressure: https://chronicdata.cdc.gov/500-Cities/500-Cities-High-blood-pressure-among-adults-aged-1/ebxs-yc6e

CDC Cholesterol: https://chronicdata.cdc.gov/500-Cities/500-Cities-High-cholesterol-among-adults-aged-18-y/mc6z-sjie

Google API: https://maps.googleapis.com/maps/api/place/nearbysearch/json 

Census Tracts: https://data.austintexas.gov/Locations-and-Maps/Census-Tracts-2010-MSA/e228-ig6a

Austin Streetline: https://data.austintexas.gov/Locations-and-Maps/Street-Centerline/m5w3-uea6


### Packages Used:
* Mapbox
* Plotly
* Matplotlib
* GeoPandas
* ArcGIS

### Actions and Tasks:
* Data Extraction
* Data Cleaning and Exploration
* Data Visualization
* Analysis and Conclusions

### Notebooks:
[Clean Code for CDC and ACS](https://github.com/zlinguist/project1/tree/master/Cleaning_Code)

[Clean Code fo Google API](https://github.com/zlinguist/project1/blob/master/google_api.ipynb)

[Clean CDC, ACS, and Google API CSV](https://github.com/zlinguist/project1/blob/master/Data/mrgdata_food.csv)

[Clean Code for Plotting Census Tract](https://github.com/zlinguist/project1/blob/master/mapping_resources/CT_Mapping_Script.ipynb)

### Analysis & Conclusions:
* Median Income of census tacts that are west of IH-35 is higher and most census tracts on east.
(https://github.com/zlinguist/project1/blob/master/mapping_resources/images/Median%20Income%20Census%20Tract.png)

* Number of FF restaurants are mainly clustered around downtown and UT area, though places like Riverside, Domain and MLK shows signs of restaurant clustering
(https://github.com/zlinguist/project1/blob/master/mapping_resources/images/Number%20of%20Fast%20Food%20in%20Census%20Tract.png)

* Fast food density was found to be negatively correlated with median income of a census tract in a linear regression. However, the highest positive correlations with fast food density were found to occur for the middle income groups, rather than for the lowest income groups.
 - The correlation between White Population and number of fast food restaurants is -0.14
 - The correlation between Black or African American Population and number of fast food restaurants is 0.01
 - The correlation between percentage of Income $75,999 to $99,999 and number of fast food restaurants is 0.14
 
(https://github.com/zlinguist/project1/blob/master/FF_Race_Income/med_inc_v_fast_food.jpg)
(https://github.com/zlinguist/project1/blob/master/FF_Race_Income/med_inc_v_black.jpg)
(https://github.com/zlinguist/project1/blob/master/FF_Race_Income/med_inc_v_white.jpg)

* There is a higher amount of fast food restaurants in census tracts with a higher percentage of middle-class income in Austin. (https://github.com/zlinguist/project1/blob/master/Images_Natalia/plot1.png)
(https://github.com/zlinguist/project1/blob/master/Images_Natalia/plot2.png)
(https://github.com/zlinguist/project1/blob/master/Images_Natalia/newplot%20(1).png)

* No strong statistical correlation between health outcomes of obesity and diabetes to fast food proximity.(https://github.com/zlinguist/project1/blob/master/food_den_disease/food_den_health.png)

* No statistical correlation can be shown when looking at income and health factors (Cholesterol, Diabetes, Obesity and Blood Pressure). 
(https://github.com/zlinguist/project1/blob/master/Income_Illness/Cholesterol_income.png)
(https://github.com/zlinguist/project1/blob/master/Income_Illness/Diabetes_income.png)
(https://github.com/zlinguist/project1/blob/master/Income_Illness/Obesity_levels_income.png)
(https://github.com/zlinguist/project1/blob/master/mapping_resources/images/Blood%20Pressure%20in%20Census%20Tract.png)
(https://github.com/zlinguist/project1/blob/master/Income_Illness/Blood_pressure_income.png)

* The conclusion drawn from the data set that has been used is that Diabetes is more with higher education within the female population.
(https://github.com/zlinguist/project1/blob/master/EDU_Hlth_FF/plot4.png)
(https://github.com/zlinguist/project1/blob/master/EDU_Hlth_FF/plot5.png)

Format: ![Alt Text](https://github.com/zlinguist/project1/blob/master/mapping_resources/images/Median%20Income%20Census%20Tract.png)


### Team Memebers: Akik Patel, Caroline Moeser, Jayeeta Dasmunshi, Kasmira Madina, Natalia Saavedra, Zach Childers 
