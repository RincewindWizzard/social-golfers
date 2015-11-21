#!/usr/bin/python3
import sys
from golfer import *
from queue import Queue
if __name__ == '__main__':
  club_size = int(sys.argv[1]) if 1 in sys.argv else 20
  groups = int(sys.argv[2]) if 2 in sys.argv else 4
  mutations = 10
  club = [ i for i in range(club_size) ]

  q = Queue()
  first_week = Week(club, groups)
  q.put(first_week)

  for i in range(10):
    week = q.get_nowait()
    for i in range(mutations):
      new_week = mutate(first_week)
      print(new_week)
      q.put(new_week)
  
  
