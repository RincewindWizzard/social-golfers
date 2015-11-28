#!/usr/bin/python3
import sys
import random, copy, operator
from dotgraph import graph, showGraph
from sgp import *


def SGP_solver(groups, size, weeks, poolsize = 100, max_iter = 100):
  tabu   = [ [] for w in range(weeks) ]
  pool = []

  for i in range(poolsize):
    solution = generateSolution(groups, size, weeks)
    pool.append((violations(solution), solution))
    

  for iteration in range(max_iter):
    violats, solution = copy.deepcopy(select(pool))

    enhance(solution, iteration, tabu)

    # schlechteste Lösung rausschmeißen
    max_index, max_value = max(enumerate(pool), key=operator.itemgetter(1))
    pool[max_index] = (violations(solution), solution)
    if pool[max_index][0] == 0: # es wurde eine korrekte Lösung gefunden
      break

  violats, solution = min(pool)
  return solution, violats

# hier wird die lokale Tabu suche angewendet
def learning(solution, iteration, tabu):
  ...

# wählt eine Lösung aus dem Pool aus
def select(pool):
  return random.choice(pool)

# hier wird eine gegebene Lösung verbessert
def enhance(solution, iteration, tabu):
  mutate(solution)
  learning(solution, iteration, tabu)
  


if __name__ == '__main__':
  if len(sys.argv) == 4:
    groups = int(sys.argv[1])
    size = int(sys.argv[2])
    weeks = int(sys.argv[3])
  else: 
    groups = 5
    size = 4
    weeks = 5

  solution, violats = SGP_solver(groups, size, weeks)
  
  print(repr_solution(solution), violats)
  #showGraph(solution)
