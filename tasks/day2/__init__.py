#!/usr/bin/env python3

class Ex3():
    def __init__(self):
        self.name = "D2E1"
        with open("./tasks/day2/input") as f:
            self.lines = f.read().split(',')

    class computer():
        def __init__(self, program):
            self.pc = 0
            self.program = program


        def add(self):
            # Store the operand values
            operand1 = int(self.program[self.pc+1])
            operand2 = int(self.program[self.pc+2])
            # Store the result address
            result_address = int(self.program[self.pc+3])
            self.program[result_address] = int(self.program[operand1]) + int(self.program[operand2])
            # Move the program counter
            self.pc += 4
        
        def mult(self):
            # Store the operand values
            operand1 = int(self.program[self.pc+1])
            operand2 = int(self.program[self.pc+2])
            # Store the result address
            result_address = int(self.program[self.pc+3])
            self.program[result_address] = int(self.program[operand1]) * int(self.program[operand2])
            # Move the program counter
            self.pc += 4
        
        def halt(self):
            return

        def run(self):
            while int(self.program[self.pc]) != 99:
                if int(self.program[self.pc]) == 1:
                    self.add()
                elif int(self.program[self.pc]) == 2:
                    self.mult()
                else:
                     self.halt()

    def run(self):
        comp = self.computer(self.lines)
        comp.run()
        return comp.program[0]

class Ex4(Ex3):
    def __init__(self):
        self.name = "D2E2"
        self.expected_value = 19690720
        super().__init__()

    def run(self):
        for noun in range(0,99):
            for verb in range(0,99):
                self.lines[1] = noun
                self.lines[2] = verb
                comp = self.computer(self.lines.copy())
                comp.run()
                if (comp.program[0] == self.expected_value):
                    return 100 * noun + verb