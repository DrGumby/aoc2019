#!/usr/bin/env python3
from math import floor

class Ex1():
    def __init__(self):
        self.name = "D1E1"
        with open("./tasks/day1/input", "r") as f:
            self.lines = f.readlines()

    def fn(self,val):
        return floor(val/3)-2

    def run(self):
        retval = 0
        for line in self.lines:
            retval+= self.fn(int(line))
        return retval

class Ex2(Ex1):
    def __init__(self):
        self.name = "D1E2"
        super().__init__()

    def fn_iter(self,val):
        tmp_val = self.fn(val)
        retval = 0
        while tmp_val >= 0:
            retval += tmp_val
            tmp_val = self.fn(tmp_val)
        return retval

    def run(self):
        retval = 0
        for line in self.lines:
            retval += self.fn_iter(int(line))

        return retval
    