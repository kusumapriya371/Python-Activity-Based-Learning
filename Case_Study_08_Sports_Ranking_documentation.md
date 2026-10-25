# Case Study 08: Sports Tournament Ranking System

## 1. Problem Statement
Store match outcomes for several teams, calculate points and goal difference, and rank teams using points, goal difference, and goals scored as tie-breakers.

## 2. Objectives
- Represent match data with tuples.
- Calculate points from match results.
- Rank teams using clear tie-breaking rules.

## 3. Assumptions
- A win earns 3 points, a draw earns 1 point, and a loss earns 0 points.
- Match tuples contain home team, away team, home score, and away score.
- All scores are non-negative integers.

## 4. Algorithm
1. Define teams and match tuples.
2. Initialize points, goal difference, and goals scored for every team.
3. For each match, update goals scored and goal difference.
4. Award points based on result.
5. Sort teams by points, goal difference, and goals scored, all descending.
6. Display ranking.

## 5. Flowchart
```text
START
  |
LOAD INPUT / SAMPLE DATA
  |
VALIDATE INPUTS
  |
PROCESS USING CONDITIONS AND LOOPS
  |
DISPLAY RESULTS AND ERRORS
  |
END
```

## 6. Pseudocode
```text
INITIALIZE statistics for each team
FOR each match tuple
  UPDATE goals scored and goal difference for both teams
  IF home score > away score, award 3 points to home
  ELSE IF scores equal, award 1 point to each
  ELSE award 3 points to away
SORT by points descending, goal difference descending, goals scored descending
DISPLAY ranking
```

## 7. Python Source Code
```python
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
```

## 8. Test Cases
| Test | Input / Condition | Expected result |
|---|---|---|
| Win | Home score 2, away score 1 | Home team gets 3 points |
| Draw | Score 1–1 | Both teams get 1 point |
| Tie-break | Equal points | Goal difference, then goals scored determine order |

## 9. Output Screenshot
![Sample output](output_screenshots/sample_output.png)

The PNG is generated from the program's captured sample run. `sample_output.txt` contains the same output as text.

## 10. Conclusion
The program uses tuples, parallel lists, nested loops, and conditional statements to create a deterministic tournament table without relying on dictionaries.
