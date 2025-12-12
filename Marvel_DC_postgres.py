import psycopg2
from math import comb

# ---- CONNECT TO POSTGRES ----
conn = psycopg2.connect(
    host="localhost",
    database="superheroes_db",
    user="postgres",
    password="admin"
)
cur = conn.cursor()

# ---- CREATE TABLE ----
cur.execute("""
CREATE TABLE IF NOT EXISTS players (
    team VARCHAR(20),
    s_no INT,
    name VARCHAR(50) PRIMARY KEY,
    height INT,
    weight INT,
    games INT
);
""")
conn.commit()

# ---- INSERT DATA ----
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

cur.executemany("""
INSERT INTO players(team, s_no, name, height, weight, games)
VALUES (%s, %s, %s, %s, %s, %s)
ON CONFLICT (name) DO NOTHING;
""", players_data)
conn.commit()

# ---- 1.1 Probability calculation ----
favorable = comb(5,2) * comb(5,3)
total = comb(10,5)
print("1.1 Probability:", favorable, "/", total, "=", favorable/total)

# ---- 1.2 ----
cur.execute("""
SELECT name, team, height, weight
FROM players
WHERE weight > (SELECT weight FROM players WHERE name='SpiderMan')
  AND height > (SELECT height FROM players WHERE name='Henery');
""")
print("\n1.2 Heavier than SpiderMan & taller than Henery:")
for row in cur.fetchall():
    print(row)

# ---- 1.3 ----
cur.execute("""
SELECT name, team, games, weight
FROM players
WHERE games > 100
  AND weight > (SELECT weight FROM players WHERE name='Captain America');
""")
print("\n1.3 >100 games & heavier than Captain America:")
for row in cur.fetchall():
    print(row)

# ---- 1.4 ----
cur.execute("""
SELECT name, team, (height + weight + games) AS total
FROM players
WHERE (height + weight + games) > 350
ORDER BY total DESC;
""")
print("\n1.4 Total stats > 350:")
for row in cur.fetchall():
    print(row)

# ---- CLOSE ----
cur.close()
conn.close()
