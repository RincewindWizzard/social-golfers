#!/usr/bin/python3
import random
import itertools


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

# bildet 2-er tuple aus einer Liste von Zahlen
def combinations(l):
  for i, p1 in enumerate(l):
    for j in range(i + 1, len(l)):
      p2 = l[j]
      yield (min(p1, p2), max(p1, p2))

# Gib Spieler Paarungen zurück
def pairs(solution):
  for w, week in enumerate(solution):
    for group in week:
      for p1, p2 in combinations(group):
        yield (p1, p2)

# wie oft wurde das Lösungskriterium verletzt?
def violations(solution):
  paired = {}
  for pair in pairs(solution):
    if pair in paired: 
      paired[pair] += 1
    else:
      paired[pair] = 0

  return sum(paired.values()), paired

def indexof(week, player):
  for i, group in enumerate(week):
    if player in group:
      return i * len(group) + group.index(player)

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

# gibt Spieler zurück, die innerhalb ihrer Gruppe im Konflikt stehen

"""
def preferred_swaps(solution, violats=None, tabu = None, iteration = 0, violation_threshold = 0):
  pairing_sum, pairing = violats if violats else violations(solution)
  results = []

  for w, week in enumerate(solution):
    week_results = []
    results.append(week_results)
    for group in week:
      group_results = []
      week_results.append(group_results)
      for p1, p2 in combinations(group):
        if (p1, p2) in pairing and pairing[p1, p2] > 0: # hier stehen zwei im konflikt

          # wie viel würde dieser taushc verbessern
          a = indexof(week, p1)
          b = indexof(week, p2)
          swap(solution, w, a, b) # test
          new_violations = violations(solution)
          swap(solution, w, a, b) # rollback

          if (not tabu or not (p1, p2) in tabu[w] or tabu[w][p1, p2] < iteration) or new_violations < violation_threshold:   # nur wenn dieser Schritt gerade nicht Tabu ist oder er verdammt gut ist
            if not (w, p1) in group_results:
              group_results.append((w, p1))
            if not (w, p2) in group_results:
              group_results.append((w, p2))
  return results
"""



def swaps(solution, violats=None):
  pairing_sum, pairing = violats if violats else violations(solution)
  for w, week in enumerate(solution):
    swapable_groups = []
    for group in week:
      swapable_players = []
      swapable_groups.append(swapable_players)
      for p1, p2 in combinations(group):
        swapable_players.append(p1)
        swapable_players.append(p2)

    for g1, g2 in combinations(swapable_groups):
      for p1 in g1:
        for p2 in g2:
          yield w, indexof(week, p1), indexof(week, p2)

def evaluate_swap(solution, swapper):
  swap(solution, *swapper) # test
  violation_sum, pairing = violations(solution)
  swap(solution, *swapper) # rollback
  return violation_sum
    


