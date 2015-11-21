#!/usr/bin/python3
"""
Folgende Pakete werden benötigt:
    pip3 install sortedcontainers
"""
from sortedcontainers import SortedList, SortedSet, SortedDict
from functools import reduce
from random import randrange, sample

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
  def as_list(self):
    # returns as list datastructure
    return reduce(lambda a,b: a + b, map(list, self.groups))

  def __eq__(self, other):
    # Vergleiche zwei Wochen, das funktioniert, weil wir vorher alle Symmetrien ausgeschlossen haben
    return self.groups == other.groups

  def __repr__(self):
    return "Week({})".format(", ".join(map(lambda g: str(list(g)), self.groups)))

  def __str__(self):
    return str(list(map(list, self.groups)))

class Schedule(object):
  def __init__(self, *weeks):
    self.weeks = list(weeks)

  def __repr__(self):
    return "Schedule(" + ", ".join(map(str, self.weeks)) + ")"
  
  @property
  def as_list(self):
    return list(map(lambda w: w.as_list, self.weeks))

  def __str__(self):
    return str(self.as_list)

  def together(self, p1, p2):
    count = 0
    for week in self.weeks:
      for group in week.groups:
        if p1 in group:
          if p2 in group:
            count += 1
          break
    return count

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

#def conflict(p1, p2, weeks):
#  for p 

if __name__ == '__main__':
  ...
  
