""" There are two teams namely ‘Marvel’ and ‘DC’ having 5 players each. Their individual data has to be stored in the following manner: - 
Level 1: - Store these data without using any Database through classes and resolve the Following queries: - 
>1.1) Implement a python code that finds the probability of selection of 2 from Marvel and 3 from DC teams. 
>1.2) List all those stars who are heavier than SpiderMan and taller than Henery. 
>1.3) List all those stars who have played more than 100 games and are heavier than Captain America. 
>1.4) For the given dataset representing stars from the Marvel and DC teams, if a metaverse is to be formed where the summation of the stats (height, weight, and games played) of any star is greater than 350 units, then display the names of all the stars meeting this criterion. 
1.5) If all these have to be stored in a database implementation then perform the necessary code. """

from math import comb
from typing import List

class Player:
    def __init__(self, team: str, s_no: int, name: str, height_cm: int, weight_kg: int, games_played: int):
        self.team = team
        self.s_no = s_no
        self.name = name
        self.height = height_cm
        self.weight = weight_kg
        self.games = games_played

    def total_stats(self) -> int:
        return self.height + self.weight + self.games

    def __repr__(self):
        return f"{self.name} ({self.team})"

class Team:
    def __init__(self, name: str, players: List[Player]):
        self.name = name
        self.players = players

# --- Build the two teams from the provided data ---
marvel_players = [
    Player("Marvel", 1, "IronMan", 182, 90, 105),
    Player("Marvel", 2, "Thor", 187, 120, 75),
    Player("Marvel", 3, "Captain America", 184, 85, 205),
    Player("Marvel", 4, "SpiderMan", 175, 75, 45),
    Player("Marvel", 5, "Hulk", 179, 290, 210),
]

dc_players = [
    Player("DC", 1, "BatMan", 180, 85, 105),
    Player("DC", 2, "SuperMan", 189, 95, 305),
    Player("DC", 3, "Harvedent", 181, 75, 55),
    Player("DC", 4, "Henery", 176, 87, 125),
    Player("DC", 5, "Heralt", 184, 100, 145),
]

marvel = Team("Marvel", marvel_players)
dc = Team("DC", dc_players)

all_players = marvel.players + dc.players

# --- 1.1 Probability of selecting 2 from Marvel and 3 from DC when choosing 5 at random from total 10 ---
def probability_choose_2_M_3_D():
    # total ways to choose 5 from 10:
    total = comb(10, 5)
    # ways to choose 2 from Marvel (5) and 3 from DC (5):
    favorable = comb(5, 2) * comb(5, 3)
    return favorable, total, favorable / total

fav, tot, prob = probability_choose_2_M_3_D()
print("1.1) Probability calculation:")
print(f"    favorable = C(5,2)*C(5,3) = {fav}")
print(f"    total = C(10,5) = {tot}")
print(f"    probability = {fav}/{tot} = {prob:.6f} (≈ {prob*100:.2f}%)")
print()

# --- 1.2 List stars heavier than SpiderMan and taller than Henery ---
def heavier_than_spiderman_and_taller_than_henery(players: List[Player]):
    spiderman = next(p for p in players if p.name == "SpiderMan")
    henery = next(p for p in players if p.name == "Henery")
    return [p for p in players if p.weight > spiderman.weight and p.height > henery.height]

res_1_2 = heavier_than_spiderman_and_taller_than_henery(all_players)
print("1.2) Stars heavier than SpiderMan and taller than Henery:")
for p in res_1_2:
    print(f"    - {p.name} ({p.team}): height={p.height}, weight={p.weight}")
print()

# --- 1.3 Stars who played >100 games AND are heavier than Captain America ---
def played_more_than_100_and_heavier_than_cap(players: List[Player]):
    cap = next(p for p in players if p.name == "Captain America")
    return [p for p in players if p.games > 100 and p.weight > cap.weight]

res_1_3 = played_more_than_100_and_heavier_than_cap(all_players)
print("1.3) Stars with >100 games and heavier than Captain America:")
for p in res_1_3:
    print(f"    - {p.name} ({p.team}): games={p.games}, weight={p.weight}")
print()

# --- 1.4 Stars whose (height + weight + games) > 350 ---
def metaverse_candidates(players: List[Player], threshold=350):
    return [p for p in players if p.total_stats() > threshold]

res_1_4 = metaverse_candidates(all_players, 350)
print("1.4) Stars with (height + weight + games) > 350:")
for p in res_1_4:
    print(f"    - {p.name} ({p.team}): total = {p.total_stats()} (h={p.height}, w={p.weight}, g={p.games})")
print()
