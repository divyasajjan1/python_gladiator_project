# Level 2: - Implement a python code to find following values and interpret why these are useful and in which scenarios:

# 1)	Find Mean and Median of their respective heights, weights and Games played.
# 2)	Find Deviation and Standard deviation of height and weight.
# 3)	Perform the necessary operation to find linear regression model of effect of weight on games played (take games played as y and weight as x).

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import itertools

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

# Level 3: - 
# Question a:
# In the Marvel and DC teams, the players are randomly selected for a special tournament where the selection criteria include:
# •	The player must be above 180 cm in height.
# •	The player must have played more than 50 games.
# If one player is randomly chosen from each team, what is the probability that both selected players meet the selection criteria for the tournament?
# Question b:
# Consider that a team is formed by selecting one player from the Marvel team and two players from the DC team for an upcoming championship. The selection criteria include:
# •	At least one player selected should have a weight below 80 kg.
# •	The combined weight of the team should not exceed 250 kg.
# What is the probability of forming such a team, given that the selection is made randomly from the Marvel and DC teams?

# Separate players by team
marvel_team = df[df['team'] == 'Marvel']
dc_team = df[df['team'] == 'DC']

# Criteria: height > 180 cm and games > 50
marvel_selected_a = marvel_team[(marvel_team['height'] > 180) & (marvel_team['games'] > 50)]
dc_selected_a = dc_team[(dc_team['height'] > 180) & (dc_team['games'] > 50)]

# Probability for Marvel
p_marvel = len(marvel_selected_a) / len(marvel_team)
# Probability for DC
p_dc = len(dc_selected_a) / len(dc_team)

# Combined probability
p_both = p_marvel * p_dc
print("Question a - Probability that both selected players meet criteria:", p_both)


# Marvel players (list of indices)
marvel_indices = marvel_team.index.tolist()
# DC players
dc_indices = dc_team.index.tolist()

# Generate all combinations: 1 Marvel + 2 DC
team_combinations = list(itertools.product(marvel_indices, itertools.combinations(dc_indices, 2)))

valid_teams = 0
total_teams = len(team_combinations)

for marvel_idx, (dc1_idx, dc2_idx) in team_combinations:
    # Extract weights
    weights = [
        marvel_team.loc[marvel_idx, 'weight'],
        dc_team.loc[dc1_idx, 'weight'],
        dc_team.loc[dc2_idx, 'weight']
    ]
    
    # Check criteria
    if any(w < 80 for w in weights) and sum(weights) <= 250:
        valid_teams += 1

# Probability
p_team = valid_teams / total_teams
print("Question b - Probability of forming a valid team:", p_team)
