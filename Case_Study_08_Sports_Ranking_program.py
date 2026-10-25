# Sports Tournament Ranking System
teams = ["Falcons", "Tigers", "Eagles", "Sharks"]
matches = [
    ("Falcons", "Tigers", 2, 1),
    ("Eagles", "Sharks", 1, 1),
    ("Falcons", "Eagles", 0, 1),
    ("Tigers", "Sharks", 3, 0),
    ("Falcons", "Sharks", 2, 2),
    ("Tigers", "Eagles", 1, 2),
]

# Parallel lists: points, goal difference, and goals scored
points = [0] * len(teams)
goal_difference = [0] * len(teams)
goals_scored = [0] * len(teams)

for home, away, home_score, away_score in matches:
    if home_score < 0 or away_score < 0:
        print("Invalid score in match:", home, away)
        continue
    h = teams.index(home)
    a = teams.index(away)
    goals_scored[h] += home_score
    goals_scored[a] += away_score
    goal_difference[h] += home_score - away_score
    goal_difference[a] += away_score - home_score

    if home_score > away_score:
        points[h] += 3
    elif home_score == away_score:
        points[h] += 1
        points[a] += 1
    else:
        points[a] += 3

# Rank team indices by points, goal difference, then goals scored.
ranking = list(range(len(teams)))
for i in range(len(ranking)):
    for j in range(i + 1, len(ranking)):
        left = ranking[i]
        right = ranking[j]
        if (points[right] > points[left] or
            (points[right] == points[left] and goal_difference[right] > goal_difference[left]) or
            (points[right] == points[left] and goal_difference[right] == goal_difference[left]
             and goals_scored[right] > goals_scored[left])):
            ranking[i], ranking[j] = ranking[j], ranking[i]

print("TOURNAMENT RANKING")
for position, index in enumerate(ranking, start=1):
    print(position, teams[index], "Points:", points[index],
          "Goal difference:", goal_difference[index],
          "Goals scored:", goals_scored[index])
