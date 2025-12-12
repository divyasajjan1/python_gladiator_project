""" There are two teams namely ‘Marvel’ and ‘DC’ having 5 players each. Their individual data has to be stored in the following manner: - 
Level 1: - Store these data without using any Database through classes and resolve the Following queries: - 
1.1) Implement a python code that finds the probability of selection of 2 from Marvel and 3 from DC teams. 
1.2) List all those stars who are heavier than SpiderMan and taller than Henery. 
1.3) List all those stars who have played more than 100 games and are heavier than Captain America. 
1.4) For the given dataset representing stars from the Marvel and DC teams, if a metaverse is to be formed where the summation of the stats (height, weight, and games played) of any star is greater than 350 units, then display the names of all the stars meeting this criterion. 
>1.5) If all these have to be stored in a database implementation then perform the necessary code. """

import sqlite3
from math import comb

# Connect to SQLite (file 'marvel_dc.db' created in current folder)
conn = sqlite3.connect("marvel_dc.db")
cur = conn.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS players (
    team TEXT,
    s_no INTEGER,
    name TEXT PRIMARY KEY,
    height INTEGER,
    weight INTEGER,
    games INTEGER
);
""")

# Insert rows (use REPLACE to avoid duplicates if re-running)
players_data = [
    ("Marvel",1,"IronMan",182,90,105),
    ("Marvel",2,"Thor",187,120,75),
    ("Marvel",3,"Captain America",184,85,205),
    ("Marvel",4,"SpiderMan",175,75,45),
    ("Marvel",5,"Hulk",179,290,210),
    ("DC",1,"BatMan",180,85,105),
    ("DC",2,"SuperMan",189,95,305),
    ("DC",3,"Harvedent",181,75,55),
    ("DC",4,"Henery",176,87,125),
    ("DC",5,"Heralt",184,100,145),
]

cur.executemany("REPLACE INTO players(team, s_no, name, height, weight, games) VALUES (?, ?, ?, ?, ?, ?);", players_data)
conn.commit()

# 1.1 Probability (same math as before; DB not necessary here)
favorable = comb(5,2) * comb(5,3)
total = comb(10,5)
print("1.1) Probability (DB):", f"{favorable}/{total} = {favorable/total:.6f}")

# 1.2 SQL: heavier than SpiderMan and taller than Henery
cur.execute("""
SELECT p.name, p.team, p.height, p.weight
FROM players p
WHERE p.weight > (SELECT weight FROM players WHERE name='SpiderMan')
  AND p.height > (SELECT height FROM players WHERE name='Henery');
""")
print("\n1.2) Heavier than SpiderMan and taller than Henery (SQL):")
for row in cur.fetchall():
    print("   ", row)

# 1.3 SQL: games > 100 and heavier than Captain America
cur.execute("""
SELECT name, team, games, weight FROM players
WHERE games > 100
  AND weight > (SELECT weight FROM players WHERE name='Captain America');
""")
print("\n1.3) >100 games AND heavier than Captain America (SQL):")
for row in cur.fetchall():
    print("   ", row)

# 1.4 SQL: total stats > 350
cur.execute("""
SELECT name, team, (height + weight + games) AS total FROM players
WHERE (height + weight + games) > 350
ORDER BY total DESC;
""")
print("\n1.4) total(height+weight+games) > 350 (SQL):")
for row in cur.fetchall():
    print("   ", row)

conn.close()
