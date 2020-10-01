import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np


datafile = "../Data/mrgdata_food.csv"

df = pd.read_csv(datafile)

df_median = (
    pd.DataFrame([df["Median Income (dollars)"], df["Number of Fast Food"]])
    .transpose()
    .replace({"Median Income (dollars)": "-"}, 0)
    .astype("int64")
    .sort_values(by=["Median Income (dollars)"], ascending=True)
)

correlation = st.pearsonr(
    df_median["Median Income (dollars)"], df_median["Number of Fast Food"]
)
print(f"The correlation between both factors is {round(correlation[0],2)}")


from scipy.stats import linregress

(slope, intercept, rvalue, pvalue, stderr) = linregress(
    df_median["Median Income (dollars)"], df_median["Number of Fast Food"]
)
regress_values = [
    income * slope + intercept for income in df_median["Median Income (dollars)"]
]
line_eq = "y = " + str(slope) + "x + " + str(round(intercept, 2))
# line_eq
print(line_eq)
plt.scatter(df_median["Median Income (dollars)"], df_median["Number of Fast Food"])
plt.plot(df_median["Median Income (dollars)"], regress_values, "r-")
plt.title("Median Income vs. Number of Fast Food Restaurants")
plt.xlabel("Median Income ($)")
plt.ylabel("Fast Food Restaurant Density")
plt.show()


df_clean = df.replace("-", 0.0)

income_groups = [
    "Income < $10,000",
    "Income $10,000-$14,999",
    "Income $15,000-$24,999",
    "Income $25,000-$34,999",
    "Income $35,000-$49,999",
    "Income $50,000-$74,999",
    "Income $75,000-$99,999",
    "Income $100,000-$149,999",
    "Income $150,000-$199,999",
    "Income > $200,000",
]

for group in income_groups:
    correlation = st.pearsonr(
        df_clean[group].astype(float), df_median["Number of Fast Food"]
    )
    print(
        f"The correlation between percentage of {group} and number of fast food restaurants is {round(correlation[0],2)}\n"
    )
    
race_groups = ['White Population',
       'Black or African American Population',
       'American Indian and Alaska Native Population', 'Asian Population',
       'Native Hawaiian and Other Pacific Islander population',
       'Some Other Race Population']

for group in race_groups:
    correlation = st.pearsonr(df_clean[group].astype(float), df_median["Number of Fast Food"])
    print(f"The correlation between percentage of {group} and number of fast food restaurants is {round(correlation[0],2)}\n")
    
