#!/usr/bin/python3
import sys
import random, copy, operator, json
import os.path
import sgp
from memetic import SGP_solver

def solution_filename(groups, size, weeks):
  return './solutions/done/{}_{}_{}.json'.format(groups, size, weeks)

def state_filename(groups, size, weeks):
  return './solutions/todo/{}_{}_{}.json'.format(groups, size, weeks)

def already_solved(groups, size, weeks):
  return os.path.isfile(solution_filename(groups, size, weeks))

def save_state(solver):
  json.dump(solver.solution, open(solution_filename(solver.groups, solver.size, solver.weeks), 'w'))
  json.dump(solver.pool, open(state_filename(solver.groups, solver.size, solver.weeks), 'w'))

def load_state(groups, size, weeks):
  if os.path.isfile(state_filename(groups, size, weeks)):
    return json.load(open(state_filename(groups, size, weeks), 'r'))
  else:
    return None

def get_solution(groups, size, weeks):
  if already_solved(groups, size, weeks):
    return json.load(open(solution_filename(groups, size, weeks), 'r'))
  else:
    pool = load_state(groups, size, weeks)
    solver = SGP_solver(groups, size, weeks, pool=pool)
    solution = solver.solve()
    save_state(solver)
    return solution

def main():
  if len(sys.argv) >= 4:
    groups = int(sys.argv[1])
    size = int(sys.argv[2])
    weeks = int(sys.argv[3])

    solution = get_solution(groups, size, weeks)
    print(repr_solution(normalize_solution(solution)))

  else:
    max_groups = 9
    max_size = 9
    max_weeks = 9

    # eigentlich sollte man hier gucken, ob alles gelöst wurde, allerdings wird das zu meinen Lebzeiten wohl nicht mehr fertig werden
    while True:
      for size in range(2, max_size):
        for groups in range(2, max_groups):
          for weeks in range(2, min(groups * size - 2, max_weeks)):
            print('SGP({}, {}, {}): '.format(groups, size, weeks), end='')
            # wurde schon eine Lösung gefunden?
            if already_solved(groups, size, weeks):
              print('already solved')
            else:
              solution = get_solution(groups, size, weeks)
              # brich ab, wenn keine Lösung gefunden ist, ansonsten Versuch es mit mehr wochen
              if sgp.violations(solution)[0] > 0:
                print('Failed!')
                break
              else:
                print('Done')

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt as e:
    ...
