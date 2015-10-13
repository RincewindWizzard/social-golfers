#!/usr/bin/python3
"""
Folgende Pakete werden benötigt:
    pip3 install sympy
"""
from sympy import Symbol, symbols

# Jede Woche spielen $n = groups * size$ Golfer in ´groups´ Gruppen a ´size´ zusammen
def SGP(groups, size, weeks):
    golfers = [ Symbol(x) for x in ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:groups*size]) ]
    solution = []
    print(golfers)

if __name__ == "__main__":
    SGP(3, 4, 10)
