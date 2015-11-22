#!/usr/bin/python3
"""
Folgende Pakete werden benötigt:
    pip3 install sortedcontainers
"""
from sortedcontainers import SortedList, SortedSet, SortedDict
from functools import reduce
from random import randrange, sample, expovariate

# -------------------------------------------------------
# Datenstrukturen

class Week(object):
  def __init__(self, club, groupcount):
    self._groupcount = groupcount
    # in einzelne Gruppen zerteilen
    self._groupsize = len(club) // groupcount
    assert len(club) == groupcount * self._groupsize
    i = 0
    groups = []
    while i < len(club):
      groups.append(club[i:i+self.groupsize])
      i += self.groupsize
   
    # Ordne die Gruppen innerhalb einer Woche anhand des kleinsten enthaltenen Golfer
    self.groups = sorted(map(lambda g: g if isinstance(g, SortedSet) else SortedSet(g), groups), key=lambda s: s[0])

  @property
  def groupsize(self):
    return self._groupsize

  @property
  def groupcount(self):
    return self._groupcount

  @property
  def playercount(self):
    return self._groupsize * self._groupcount 

  @property
  def as_list(self):
    # returns as list datastructure
    return reduce(lambda a,b: a + b, map(list, self.groups))

  def __getitem__(self, key):
    return self.groups[key]

  def __eq__(self, other):
    # Vergleiche zwei Wochen, das funktioniert, weil wir vorher alle Symmetrien ausgeschlossen haben
    return self.groups == other.groups

  def __repr__(self):
    return str(list(map(list, self.groups)))


def as_matrix(schedule):
  weeks = []
  for week in schedule:
    week_m = []
    for group in week.groups:
      week_m.append(list(group))
    weeks.append(week_m)
  return weeks

# -----------------------------------------
# Hier beginnen die Funktionen, die für den Algorithmus gebraucht werden
def swap(week, a, b):
  club = week.as_list
  p_a = club[a]
  p_b = club[b]

  club[a] = p_b
  club[b] = p_a
  return Week(club, week._groupcount)

def mutate(week):
  g1, g2 = sample(range(week.groupcount), 2)
  p1 = randrange(0, week.groupsize)
  p2 = randrange(0, week.groupsize)

  return swap(week, g1 * week.groupsize + p1, g2 * week.groupsize + p2)

def possible_mutations(week):
  return int(week.groupsize ** 2 * (week.groupcount ** 2 - week.groupcount) // 2)

def mutations(week):
  for g1 in range(week.groupcount):
    for g2 in range(g1 + 1, week.groupcount):
      for p1 in range(week.groupsize):
        for p2 in range(week.groupsize):
          yield swap(week, g1 * p1, g2 * p2)

def together(p1, p2, weeks):
  # Wie oft spielen p1 und p2 zusammen
  count = 0
  for week in weeks:
    for group in week.groups:
      if p1 in group:
        if p2 in group:
          count += 1
        break
  return count

def conflicts(weeks, week=None):
  # Wie viele Konflikte gibt es? (Zwei Golfer mehr als einmal)
  cons = []
  for i, p1 in enumerate(weeks[0].as_list):
    for j, p2 in enumerate(weeks[0].as_list):
      if i < j and together(p1, p2, weeks) > 1:
        cons.append(p1)
        cons.append(p2)
  return cons

def long_jump(week):
  # Mutiert eine Woche mehrere Male (Poisson Distributed)
  for i in range(int(expovariate(1 / week.groupcount * week.groupsize))):
    week = mutate(week)
  return week

def conflicting(club, weeks, p1):
  for p2 in club:
    if not p1 == p2:
      if together(p1, p2, weeks) > 1:
        return True
  return False



if __name__ == '__main__':
  ...
  
