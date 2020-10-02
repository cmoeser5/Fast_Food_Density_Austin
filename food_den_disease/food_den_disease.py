%load_ext lab_black
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st

df = pd.read_csv(
    "../Data/mrgdata_food.csv",
    index_col="Census Tract",
    usecols=[
        "Census Tract",
        "Data_Value_bp",
        "Data_Value_chol",
        "Data_Value_dbt",
        "Data_Value_obs",
        "Lat_obs",
        "Lng_obs",
        "Total 18+ Population",
        "Number of Fast Food",
    ],
)
df

df["Number of Fast Food"].max()

# dropping NaNs
df = df.dropna()

# create a scatter of fast food restuarants and health issue
plt.scatter(
    df["Number of Fast Food"],
    df["Data_Value_dbt"],
    color="green",
    alpha=0.50,
    label="Diabetes",
)
plt.scatter(
    df["Number of Fast Food"],
    df["Data_Value_obs"],
    color="blue",
    alpha=0.50,
    label="Obesity",
)
plt.show()

# finding correlation between fast food and health issue
corr_obs = st.pearsonr(df["Number of Fast Food"], df["Data_Value_obs"])
corr_dbt = corr = st.pearsonr(df["Number of Fast Food"], df["Data_Value_dbt"])

print(f"The correlation between fast food and obesity is {round(corr_obs[0],2)}")
print(f"The correlation between fast food and diabetes is {round(corr_dbt[0],2)}")

# calculate the regression lines for dbt and obs
from scipy.stats import linregress

# diabetes line
(slope, intercept, rvalue, pvalue, stderr) = linregress(
    df["Number of Fast Food"], df["Data_Value_dbt"]
)
regress_values_dbt = [
    income * slope + intercept for income in df["Number of Fast Food"]
]
line_eq_dbt = "y = " + str(slope) + "x + " + str(round(intercept, 2))

# obesity line
(slope, intercept, rvalue, pvalue, stderr) = linregress(
    df["Number of Fast Food"], df["Data_Value_obs"]
)
regress_values_obs = [
    income * slope + intercept for income in df["Number of Fast Food"]
]
line_eq_obs = "y = " + str(slope) + "x + " + str(round(intercept, 2))


# create a scatter of fast food restuarants and health issue  with the regression line
print(f"Line equation for Diabetes {line_eq_dbt}")
print(f"Line equation for Diabetes {line_eq_obs}")
plt.scatter(
    df["Number of Fast Food"],
    df["Data_Value_dbt"],
    color="green",
    alpha=0.50,
    label="Diabetes",
)
plt.scatter(
    df["Number of Fast Food"],
    df["Data_Value_obs"],
    color="blue",
    alpha=0.50,
    label="Obesity",
)
plt.plot(df["Number of Fast Food"], regress_values_dbt, "r-")
plt.plot(df["Number of Fast Food"], regress_values_obs, "r-")
plt.xlabel("Number of Fast Food Restaurants")
plt.ylabel("Estimation of Health Issue (%)")
plt.title("Estimation of Health Issue vs Number of Fast Food Restaurants in Austin")
plt.legend()
plt.show()


print(
    f"The correlation between fast food restaurants in Austin and obesity is {round(corr_obs[0],2)}"
)
print(
    f"The correlation between fast food restaurants in Austin and diabetes is {round(corr_dbt[0],2)}"
)