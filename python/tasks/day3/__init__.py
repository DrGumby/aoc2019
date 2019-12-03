#!/usr/bin/env python3

class Ex5():
    def __init__(self):
        self.name = "D3E1"
        self.wire_a = [(0,0)]
        self.wire_b = [(0,0)]
        with open("./tasks/day3/input", "r") as f:
            self.lines = f.readlines()

    def step(self, instr, lst):
        dir = instr[0]
        cnt = int(instr[1:])
        if (dir == 'U'):
            return [(lst[0], lst[1]+i) for i in range(1,cnt+1)]
        elif (dir == 'D'):
            return [(lst[0], lst[1]-i) for i in range(1,cnt+1)]
        elif (dir == 'L'):
            return [(lst[0]-i, lst[1]) for i in range(1,cnt+1)]
        elif (dir == 'R'):
            return [(lst[0]+i, lst[1]) for i in range(1,cnt+1)]

    def run(self):
        result_list = []
        list_a = self.lines[0].split(',')
        list_b = self.lines[1].split(',')
        for i in list_a:
            self.wire_a += (self.step(i, self.wire_a[-1]))

        for i in list_b:
            self.wire_b += (self.step(i, self.wire_b[-1]))


        intersection = set(self.wire_a) & set(self.wire_b)
        distances = list(map(lambda x: abs(x[0])+abs(x[1]), intersection))
        distances.remove(0)
        return min(distances)

class Ex6(Ex5):
    def __init__(self):
        super().__init__()
        self.name = "D3E2"
    
    def run(self):
        super().run()
        distances = []
        for idx_a, i in enumerate(self.wire_a):
            for idx_b, j in enumerate(self.wire_b):
                if i == j and i != (0,0) and j != (0,0):
                    distances.append(idx_a + idx_b)
        return min(distances)