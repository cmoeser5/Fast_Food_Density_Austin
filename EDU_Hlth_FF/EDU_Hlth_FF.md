# Questions?
* Is there any correlation between education levels and health issues ?
  Can we establish an relationship between education levels ,health issues and Fast Food Density in Austin?
### Hypothesis:
The relationship between education and health is never a simple one. Poor health not only results from lower educational attainment, it can also cause educational setbacks and interfere with education. Health conditions like Diabetes have an effect on educational outcomes.

### Data Set:

ACS Sex/Age/Education: https://data.census.gov/cedsci/table?q=18%20and%20over&g=0500000US48453.140000&y=2017&tid=ACSDT5Y2017.B15001&hidePreview=false

CDC Obesity Data: https://chronicdata.cdc.gov/500-Cities/500-Cities-Obesity-among-adults-aged-18-years/bjvu-3y7d

CDC Diabetes Data: https://chronicdata.cdc.gov/500-Cities/500-Cities-Diagnosed-diabetes-among-adults-aged-18/cn78-b9bj

CDC Blood Pressure: https://chronicdata.cdc.gov/500-Cities/500-Cities-High-blood-pressure-among-adults-aged-1/ebxs-yc6e

CDC Cholesterol: https://chronicdata.cdc.gov/500-Cities/500-Cities-High-cholesterol-among-adults-aged-18-y/mc6z-sjie

Google API: https://maps.googleapis.com/maps/api/place/nearbysearch/json 



### Packages Used:
* pandas 
* Matplotlib
* GeoPandas

# Analysis & observation

To find out the correlation between health and education , we have taken the data dump from two government sources which is CDC and Census. After the data was pulled from the sources , we have cleaned the data to baseline our csv file.
With the baselined cleaned data, the files were joined with panda to make a single data repository with Census Tract as the primary key.
Using scatter plots , first the relationship between 18+ population and diseases ( Diabetes, Blood Pressure and Obesity ) were extracted from which the disease that was least was identified which in this case was Diabetes. From that , the relationship between diabetes and male/female population was established which concluded that Diabetes was more in the female population. The last correlation drawn was between education in female population  vs diabetes.
The conclusion drawn from the data set that has been used is that Diabetes is more with higher education within the female population.

Also we observed that fast food density in Austin is less in the area where diabetic female  population high. 


