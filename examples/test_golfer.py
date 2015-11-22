#!/usr/bin/python3
import unittest, random
from golfer import *
CLUB_SIZE  = 6
GROUPS = 2
GROUP_SIZE = CLUB_SIZE // GROUPS
assert GROUP_SIZE * GROUPS == CLUB_SIZE


class TestGolfer(unittest.TestCase):
  def setUp(self):
    self.golfclub = [ i for i in range(CLUB_SIZE)]
    self.week = Week(self.golfclub, GROUPS)
    self.schedule = [ self.week, swap(self.week, 0, -1) ]

  def test_mutate(self):
    schedule = [ mutate(self.week) for i in range(10) ]
    #for week in schedule:
    #  print(str(week))

  def test_together(self):
    self.assertEqual(together(3, 4, self.schedule), 2, msg=self.schedule)
    self.assertEqual(together(0, 3, self.schedule), 1, msg=self.schedule)
    self.assertEqual(together(2, 3, self.schedule), 0, msg=self.schedule)

  def test_conflicts(self):
    self.assertEqual(conflicts([self.week, self.week]), CLUB_SIZE)

  def test_conflictors(self):
    for p in self.golfclub:
      if conflicting(self.golfclub, self.schedule, p):
        print(p)

  def test_mutations(self):
    for i in range(1, 6):
      for j in range(1, 6):
        week = Week( list(range(i*j)), i )
        self.assertEqual(len(list(mutations(week))), possible_mutations(week))

  def test_weekEquals(self):
    club = self.golfclub

    # Golfer tauschen führt zu unterschiedlichen Wochen
    diff_week = Week([club[-1]] + club[1:-1] + [club[0]], GROUPS)
    diff_week1 = swap(self.week, 0, CLUB_SIZE - 1)
    self.assertNotEqual(self.week, diff_week)
    self.assertEqual(diff_week, diff_week1)

    # egal in welcher Reihenfolge die Golfer stehen, die Gruppe bleibt gleich
    g1 = club[:GROUP_SIZE]
    g2 = club[GROUP_SIZE:]

    random.shuffle(g1)
    random.shuffle(g2)

    shuffle_club = g1 + g2

    w1 = Week(club, GROUPS)
    w2 = Week(shuffle_club, GROUPS)
    self.assertEqual(w1, w2)

    club.reverse()
    w3 = Week(club, GROUPS)
    self.assertEqual(w1, w3)

  def test_weekcheck(self):
      club = self.golfclub
      self.assertTrue(self.checkWeek(self.week, self.golfclub))
      with self.assertRaises(AssertionError):
        for i in range(1, CLUB_SIZE):
          if not CLUB_SIZE % i == 0:
            self.assertRaises(self.checkWeek(Week(club, i), self.golfclub))

      smallest = []
      for group in self.week.groups:
        smallest.append(group[0])

      self.assertEqual(smallest, sorted(smallest))


  def checkWeek(self, week, golfclub):
    """ Überprüft alle Korrektheitsbedingungen """
    well_formed = True

    for golfer in golfclub:
      well_formed &= any(map(lambda group: golfer in group, week.groups))

    groupsize = len(golfclub) // len(week.groups)
    for group in week.groups:
      well_formed &= groupsize == len(group)
    return well_formed


if __name__ == '__main__':
    unittest.main()
