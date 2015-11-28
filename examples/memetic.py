#!/usr/bin/python3
import sys
import random
from dotgraph import graph, showGraph

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


def normalize_week(week):
  for group in week:
    group.sort()
  return week

def normalize_solution(solution):
  for week in solution:
    for group in week:
      group.sort()
    week.sort(key=lambda g: g[0])
  solution.sort(key=lambda w: w[0][1])
  return solution

def repr_solution(solution):
  s = '[\n'
  for week in solution:
      s += '\t['
      for group in week:
        s += '\n\t\t' + str(group) + ','
      s += '\n\t],\n'
  s += '\n]'
  return s

if __name__ == '__main__':
  if len(sys.argv) == 4:
    groups = int(sys.argv[1])
    size = int(sys.argv[2])
    weeks = int(sys.argv[3])
  else: 
    groups = 3
    size = 2
    weeks = 3

  solution = generateSolution(groups, size, weeks)
  print(solution)
  print(repr_solution(normalize_solution(solution)))
  showGraph(solution)

