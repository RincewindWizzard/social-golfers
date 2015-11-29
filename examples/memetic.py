#!/usr/bin/python3
import sys
import random, copy, operator, json
import os.path
#from dotgraph import graph, showGraph
from time import time
import sgp

class SGP_solver(object):
  def __init__(self, groups, size, weeks, poolsize = 25, pool = None, timeout = 600, max_learning = 30):
    self.groups = groups
    self.size = size
    self.weeks = weeks

    self.stop_time = time() + timeout
    if pool:
      # check if pool is okay
      for v, solution in pool:
        assert len(solution) == weeks
        for week in solution:
          assert len(week) == groups
          for group in week:
            assert len(group) == size
      self.pool = pool
    else:
      self.pool = [ (lambda sigma: (sgp.violations(sigma)[0], sigma))(sgp.generateSolution(groups, size, weeks)) for i in range(poolsize) ]
    self.max_learning = max_learning
    self.solution = None
    self.done = False
  
  def solve(self):
    while not self.timeout:
      violats, solution = copy.deepcopy(random.choice(self.pool))

      if violats == 0:
        self.solution = solution
        return solution

      # Evolution
      sgp.mutate(solution)
 
      # lokale tabu suche
      solution = self.learning(solution)

      # schlechteste Lösung rausschmeißen
      max_index, max_value = max(enumerate(self.pool), key=lambda t: t[1][0])
      self.pool[max_index] = (sgp.violations(solution)[0], solution)

      if self.pool[max_index][0] == 0: # es wurde eine korrekte Lösung gefunden
        break

    best = min(self.pool, key=lambda t: t[0])
    self.solution = best[1]
    self.done = best[0] == 0
    return best[1]

  def learning(self, solution):
    tabu = [ {} for week in solution ]
    best_solution = copy.deepcopy(solution)
    best_violations = sgp.violations(solution)[0]

    # wie lange wird weiter gesucht, obwohl keine verbesserung eintritt
    #learning_semaphore = self.max_learning
    for iteration in range(self.groups * self.weeks):
      if best_violations == 0 or self.timeout: # were done
        break 

      try:
        # von allen Täuschen, den besten finden
        nex_viol, w, a, b = min(
          filter(
            # entweder verbessert dieser Tausch diese Lösung zur Besten
            # oder er ist nicht tabu
            lambda t: t[0] < best_violations or not tuple(sorted((t[2], t[3]))) in tabu[t[1]] or tabu[t[1]][tuple(sorted((t[2], t[3])))] < iteration,
            map(
              lambda t: (sgp.evaluate_swap(solution, t), t[0], t[1], t[2]), 
              sgp.swaps(solution)
            )
          )
        )
        sgp.swap(solution, w, a, b)

        tabu[w][tuple(sorted((a, b)))] = iteration + random.randint(4, 100)


        if nex_viol < best_violations:
          best_solution = solution
          best_violations = nex_viol
          print(best_violations, end=' ')
          sys.stdout.flush()


      except ValueError as e:
        break
    return best_solution

  @property
  def timeout(self):
    return self.stop_time < time()


 
