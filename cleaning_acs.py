#Import data
import pandas as pd
file_to_load = 'Data/ACSDP5Y2017.DP05_data_with_overlays_2020-09-23T174627.csv'
df = pd.read_csv(file_to_load, usecols = ['GEO_ID', 'DP05_0001E', 'DP05_0002E','DP05_0003E', 'DP05_0064E', 'DP05_0065E', 'DP05_0066E', 'DP05_0067E', 'DP05_0068E', 'DP05_0069E'    ])
df.head()

#Rename data
df = df.rename(columns={"GEO_ID": "Census_Tract",
                        "DP05_0001E": "Total Population",
                        "DP05_0002E": "Total Male", 
                       "DP05_0003E": "Total Female",
                       "DP05_0064E": "White Population",
                       "DP05_0065E": "Black or African American Population",
                       "DP05_0066E": "American Indian and Alaska Native Population",
                       "DP05_0067E": "Asian Population",
                       "DP05_0068E": "Native Hawaiian and Other Pacific Islander population",
                       "DP05_0069E": "Some Other Race Population"})
df

#Drop and Reset
df.drop(df.index[0], inplace=True)
df
df.reset_index()

#Split Census Tract Column
df[['GEO_ID', 'Census Tract']] = df.Census_Tract.apply(
    lambda x: pd.Series(str(x).split('US'))
)
df

# Export cleaned data
df.drop(columns = ['Census_Tract'], inplace=True)
df
df.to_csv('Data/cleaned_race_acs.csv')