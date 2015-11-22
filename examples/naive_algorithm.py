#!/usr/bin/python3
import sys
from golfer import *
from queue import Queue
from itertools import permutations
from time import time

def full_search(n, g):
  club = [ i for i in range(n) ]
  schedule = [ ]
  for perm in permutations(club):
    week = Week(perm, g)
    if conflicts(schedule + [week]) == 0:
      schedule.append(week)
      print(week)
  return schedule

def randomized_search(n, g):
  club = [ i for i in range(n) ]
  q = Queue()
  schedule = [ Week(club, g) ]
  print(schedule[0])
  q.put((0, schedule[0]))

  start = time()
  iterations = 0
  while not q.empty() and time() - start < 10:
    cons, week = q.get_nowait()

    iterations += 1
    next_week = long_jump(week)
    next_cons = conflicts(schedule + [next_week])
    if next_cons == 0:
      schedule.append(next_week)
      print(next_week)


    q.put((next_cons, next_week))
  print("{} Iterations in {:.2f} seconds".format(iterations, time() - start))
  return schedule

if __name__ == '__main__':
  if len(sys.argv) == 3:
    club_size = int(sys.argv[1])
    groups = int(sys.argv[2])
  else:
    club_size = 6
    groups = 3
  group_size = club_size // groups

  #full_search(club_size, groups)
  randomized_search(club_size, groups)

