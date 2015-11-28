#!/usr/bin/python3
import sys
import random, copy, operator
from dotgraph import graph, showGraph
from sgp import *

POOLSIZE = 100
MAX_ITER = 100

def SGP_solver(groups, size, weeks):
  pool = []
  for i in range(POOLSIZE):
    solution = generateSolution(groups, size, weeks)
    pool.append((violations(solution), solution))

  for j in range(MAX_ITER):
    violats, solution = copy.deepcopy(select(pool))
    mutate(solution)
    learning(solution)
    max_index, max_value = max(enumerate(pool), key=operator.itemgetter(1))
    pool[max_index] = (violations(solution), solution)
    if pool[max_index][0] == 0: # es wurde eine korrekte Lösung gefunden
      break

  return min(pool)

# wählt eine Lösung aus dem Pool aus
def select(pool):
  return random.choice(pool)

# hier wird die lokale Tabu suche angewendet
def learning(solution):
  ...

if __name__ == '__main__':
  if len(sys.argv) == 4:
    groups = int(sys.argv[1])
    size = int(sys.argv[2])
    weeks = int(sys.argv[3])
  else: 
    groups = 5
    size = 4
    weeks = 5

  violats, solution = SGP_solver(groups, size, weeks)
  print(repr_solution(solution), violats)
  #showGraph(solution)
