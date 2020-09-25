import pandas as pd

file_to_load = “Data/500_cities_Diagnosed_diabetes_among_adults_aged__18_years.csv”

df = pd.read_csv(file_to_load)
df.head()

df_austin = df[df[“CityName”] == “Austin”]

df_austin.reset_index().head()

df_austin = df_austin.drop(
    columns=[
        “DataSource”,
        “Data_Value_Footnote_Symbol”,
        “Data_Value_Footnote”,
        “CategoryID”,
        “Short_Question_Text”,
        “Data_Value_Unit”,
        “DataValueTypeID”,
        “Data_Value_Type”,
        “Data_Value”,
        “Low_Confidence_Limit”,
        “High_Confidence_Limit”,
        “CityFIPS”,
    ]
)
df_austin = df_austin[df_austin[“GeographicLevel”] == “Census Tract”]
df_austin[[“Lat”, “Lng”]] = df_austin.GeoLocation.apply(
    lambda x: pd.Series(str(x).split(“,”))
)
df_austin[[“Lat”]] = df_austin.Lat.apply(lambda x: pd.Series(x[1:]))
df_austin[[“Lng”]] = df_austin.Lng.apply(lambda x: pd.Series(x[:-1]))
df_austin
8:57
df_austin.to_csv(“Data/cleaned_diabetes_cdc.csv”)
