#!/usr/bin/env python3
import pprint
class Day6():
    def __init__(self):
        self.name = "D6E1"
        with open("tasks/day6/input") as f:
            self.lines = f.readlines()

    def run(self):
        direct = {}
        indirect = {}
        sum = 0
        for line in self.lines:
            line = line.rstrip()
            orbit = tuple(line.split(")"))
            direct[orbit[1]] = orbit[0]
        for i in direct:
            val = self.calc_indirect(direct, i)
            #print("{0}:{1}".format(i,val))
            sum += val

        distance = self.calc_dist_to_santa(direct)
        return sum, distance

    def calc_indirect(self,direct:dict, key:str):
        if key not in direct:
            return 0
        else:
            key = direct[key]
            return 1 + self.calc_indirect(direct, key)

    def calc_indirect_path(self,direct:dict, key:str, lst:list):
        #import pdb; pdb.set_trace()
        if key not in direct:
            return None
        else:
            key = direct[key]
            lst.append(key)
            return self.calc_indirect_path(direct, key, lst)
    
    def calc_dist_to_santa(self, direct):
        santa_indirect_orbit = []
        you_indirect_orbit = []
        self.calc_indirect_path(direct, "SAN", santa_indirect_orbit)
        self.calc_indirect_path(direct, "YOU", you_indirect_orbit)

        you_set = frozenset(you_indirect_orbit)
        common_orbit = [x for x in santa_indirect_orbit if x in you_set]
        first_meet = common_orbit[0]
        return (you_indirect_orbit.index(first_meet) + santa_indirect_orbit.index(first_meet))