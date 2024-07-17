#!/usr/bin/env python


import argparse

parser = argparse.ArgumentParser(
    description="all numbers are equal, but there are some that are more equal than others"
)

parser.add_argument("-f", dest="f", type=int, help="firs number")
parser.add_argument("-s", dest="s", type=int, help="second number")
parser.add_argument("-t", dest="t", type=int, help="third number")

args = parser.parse_args()

first = args.f
second = args.s
third = args.t

if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)
