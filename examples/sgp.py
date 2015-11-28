#!/usr/bin/python3
import random


# Erzeugt eine zufällige Lösung
def generateSolution(groups, size, weeks):
  players = list(range(groups * size))
  solution = []
  for w in range(weeks):
    permutation = random.sample(players, groups * size)
    week = []
    for g in range(groups):
      week.append(permutation[g * size : g * size + size])
    solution.append(week)

  return solution

# bringt eine Lösung in normalform
def normalize_solution(solution):
  for week in solution:
    for group in week:
      group.sort()
    week.sort(key=lambda g: g[0])
  solution.sort(key=lambda w: w[0][1])
  return solution

# Menschenlesbare Repräsentation einer Lösung
def repr_solution(solution):
  s = '[\n'
  for week in solution:
      s += '\t['
      for group in week:
        s += '\n\t\t' + str(group) + ','
      s += '\n\t],\n'
  s += '\n]'
  return s

# Gib Spieler Paarungen zurück
def pairs(solution):
  for week in solution:
    for group in week:
      for i, p1 in enumerate(group):
        for j in range(i + 1, len(group)):
          p2 = group[j]
          if p1 < p2:
            yield (p1, p2)
          else:
            yield (p2, p1)

# wie oft wurde das Lösungskriterium verletzt?
def violations(solution):
  paired = {}
  for pair in pairs(solution):
    if pair in paired: 
      paired[pair] += 1
    else:
      paired[pair] = 0

  return sum(paired.values())

# in-place swap of players inside a week
def swap(solution, w, a, b):
  week = solution[w]
  groupsize = len(week[0])
  p1 = week[a // groupsize][a % groupsize]
  p2 = week[b // groupsize][b % groupsize]

  week[a // groupsize][a % groupsize] = p2
  week[b // groupsize][b % groupsize] = p1


# ----------------------
def weeks(solution):
  return len(solution)

def groups(solution):
  return len(solution[0])

def group_size(solution):
  return len(solution[0][0])

def players(solution):
  return group_size(solution) * groups(solution)
# --------------------------

# Verändert eine Lösung zufällig durch eine zufällige Anzahl Täusche
def mutate(solution):
  for i in range(int(random.expovariate(1 / players(solution)))): # Poisson Verteilung
    w = random.randrange(0, len(solution))
    week = solution[w]
    a, b = random.sample(range(players(solution)), 2)
    swap(solution, w, a, b)


  
      
