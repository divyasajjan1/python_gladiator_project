# Level 4: 
from Marvel_DC_project import Player, marvel_players, dc_players

# Scenario 1: Performance Analysis Logic
# Given the data on the Marvel and DC teams, you want to analyze the overall performance 
# of the players based on their height, weight, and games played.

# Question: Considering the height, weight, and games played, determine the player with the 
# highest overall performance among both teams. Explain your selection process and the metrics
# considered for evaluating performance. Also, discuss any potential biases or limitations in 
# this analysis.

def get_performance_report(players):
    """
    Analyzes performance by normalizing stats and applying weighted averages.
    Metrics: Height (20%), Weight (20%), Games Played (60%)
    """
    # Extract lists for Min-Max Scaling
    h_vals = [p.height for p in players]
    w_vals = [p.weight for p in players]
    g_vals = [p.games for p in players]

    report = []
    for p in players:
        # Min-Max Normalization: (value - min) / (max - min)
        # This brings all metrics into a 0 to 1 range
        norm_h = (p.height - min(h_vals)) / (max(h_vals) - min(h_vals))
        norm_w = (p.weight - min(w_vals)) / (max(w_vals) - min(w_vals))
        norm_g = (p.games - min(g_vals)) / (max(g_vals) - min(g_vals))

        # Scoring: High emphasis on Experience (Games Played)
        score = (norm_h * 0.2) + (norm_w * 0.2) + (norm_g * 0.6)
        report.append({"player": p, "score": round(score, 4)})
    
    return report

# Scenario 2: Team Composition Strategy
# As a coach or team manager, you are tasked with optimizing the team composition for both 
# Marvel and DC teams to maximize their chances of winning in upcoming tournaments. However, 
# you have constraints based on player attributes such as height, weight, and experience 
# (games played).

# Question: Propose a team composition strategy for Marvel and DC teams that balances player 
# attributes like height, weight, and experience. How would you select players for each team 
# to ensure diversity in skill sets while maintaining team cohesion? Discuss the rationale 
# behind your strategy and any trade-offs involved in player selection.

def analyze_team_strategy(team_players, team_name):
    """
    Selects a balanced trio based on distinct archetypes:
    1. The Veteran (Experience)
    2. The Tank (Physicality/Weight)
    3. The All-Rounder (Best Height-to-Weight balance)
    """
    veteran = max(team_players, key=lambda p: p.games)
    tank = max(team_players, key=lambda p: p.weight)
    
    # All-rounder: High games and balanced BMI-like ratio
    all_rounder = max(team_players, key=lambda p: (p.games * 0.5) + (p.height / p.weight))

    return {
        "Team": team_name,
        "Veteran/Leader": veteran.name,
        "Tank/Enforcer": tank.name,
        "Versatile/Support": all_rounder.name
    }

# --- Execution and Reporting ---

all_stars = marvel_players + dc_players
performance_data = get_performance_report(all_stars)

# 1. Determine MVP
mvp_entry = max(performance_data, key=lambda x: x['score'])
mvp = mvp_entry['player']

print("--- LEVEL 4: SCENARIO 1 - PERFORMANCE ANALYSIS ---")
print(f"The highest performing player is: {mvp.name} ({mvp.team})")
print(f"Overall Performance Score: {mvp_entry['score']}")
print("\n[EXPLANATION]:")
print("1. Metrics: We used a weighted index of Height(20%), Weight(20%), and Games(60%).")
print("2. Normalization: Min-Max scaling was applied to ensure 'Games Played' (up to 305) "
      "did not numerically overwhelm 'Height' (approx 180).")
print("3. Biases: This model favors veterans. A young, highly skilled player with few "
      "games played would score poorly despite high physical potential.")

print("\n" + "-"*50 + "\n")

print("--- LEVEL 4: SCENARIO 2 - TEAM COMPOSITION STRATEGY ---")
for players, name in [(marvel_players, "Marvel"), (dc_players, "DC")]:
    strategy = analyze_team_strategy(players, name)
    print(f"Strategy for {name}:")
    for role, p_name in strategy.items():
        if role != "Team":
            print(f"  - {role}: {p_name}")

print("\n[RATIONALE]:")
print("To ensure diversity, we avoided picking the 'top 3' by a single metric. "
      "Instead, we selected based on roles (Leadership, Physicality, and Versatility) "
      "to ensure team cohesion and the ability to handle various tournament challenges.")