import pandas as pd

file_to_load = “Data/500_cities_Diagnosed_diabetes_among_adults_aged__18_years.csv”

df = pd.read_csv(file_to_load)
df.head()

df_austin = df[df[“CityName”] == “Austin”]

df_austin.reset_index().head()

# df_austin.drop(columns=[])
