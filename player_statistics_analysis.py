import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

#Read data
df = pd.read_csv('team_dc_marvel.csv')
print(df.head())

# 1) Find Mean and Median of their respective heights, weights and Games played.

mean_values = df[['height', 'weight', 'games']].mean()
median_values = df[['height', 'weight', 'games']].median()
print("Mean Values:\n", mean_values)
print("Median Values:\n", median_values)

# 2) Find Deviation and Standard deviation of height and weight.

# Deviation
height_mean = df["height"].mean()
weight_mean = df["weight"].mean()

df["height_deviation"] = df["height"] - height_mean
df["weight_deviation"] = df["weight"] - weight_mean
print("Height Deviations:\n", df["height_deviation"])
print("Weight Deviations:\n", df["weight_deviation"])

# Standard Deviation
std_height = df["height"].std()
std_weight = df["weight"].std()

print("Standard Deviation of Height:", std_height)
print("Standard Deviation of Weight:", std_weight)

# 3)	Perform the necessary operation to find linear regression model of effect 
# of weight on games played (take games played as y and weight as x).

#Games Played = β0 + β1 × Weight

# Independent variable (X)
X = df[['weight']]
# Dependent variable (y)
y = df['games']

# Create and train model
model = LinearRegression()
model.fit(X, y)

# Results
intercept = model.intercept_
coefficient = model.coef_[0]

print("Intercept:", intercept)
print("Coefficient (weight -> games):", coefficient)