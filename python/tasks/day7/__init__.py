import itertools
class Day7():
    def __init__(self):
        self.name = "D5E1"
        with open("tasks/day7/debug") as f:
            self.file = f.read()

    def run(self):
        phases = [i for i in range(5,10)]
        perm = itertools.permutations(phases)
        maxlist = []

        for i in perm:
            intermediate = 0
            cnt = 0
            is_first = True
            while intermediate != -1:
                if is_first:
                    intermediate = Program(self.file.split(",")).run(intermediate, 0)
                    is_first = False
                else:
                    intermediate = Program(self.file.split(",")).run(intermediate, i[cnt%5])
                    cnt+=1

            maxlist.append(intermediate)

        return max(maxlist)


class Program():
    def __init__(self, program):
        self.program = list(map(int,program))
        self.pc = 0

    def run(self, intermediate, phase):
        first_input = True
        while self.program[self.pc] != 99:
            op = str(self.program[self.pc])
            opcode = int(op[-2:])
            modes = [0,0,0]
            for idx, i in enumerate(reversed(op[:-2])):
                modes[idx] = int(i)
            modes = tuple(modes)

            if opcode == 1:
                self.pc += Add(modes).run(self.program, self.pc)
            elif opcode == 2:
                self.pc += Mult(modes).run(self.program, self.pc)
            elif opcode == 3:
                if first_input:
                    val = phase
                    first_input = False
                else:
                    val = intermediate
                self.pc += Input(modes).run(self.program, self.pc, val)
            elif opcode == 4:
                return Output(modes).run(self.program, self.pc)[1]
            elif opcode == 5:
                self.pc = JumpTrue(modes).run(self.program, self.pc)
            elif opcode == 6:
                self.pc = JumpFalse(modes).run(self.program, self.pc)
            elif opcode == 7:
                self.pc += Less(modes).run(self.program, self.pc)
            elif opcode == 8:
                self.pc += Equal(modes).run(self.program, self.pc)
            else:
                Halt(modes).run(self.program, self.pc)
                return -1




class Instr():
    param_modes = (0,0,0)
    def run(self, program, pc):
        raise NotImplementedError

class Add(Instr):
    def __init__(self, modes):
        self.modes = modes
    
    def run(self, program, pc):
        if self.modes[0] == 0:
            val1 = program[program[pc+1]]
        else:
            val1 = program[pc+1]
        
        if self.modes[1] == 0:
            val2 = program[program[pc+2]]
        else:
            val2 = program[pc+2]
        
        sum = val1 + val2

        if self.modes[2] != 0:
            raise Exception
        else:
            program[program[pc+3]] = sum
        
        return 4

class Mult(Instr):
    def __init__(self, modes):
        self.modes = modes
    
    def run(self, program, pc):
        if self.modes[0] == 0:
            val1 = program[program[pc+1]]
        else:
            val1 = program[pc+1]
        
        if self.modes[1] == 0:
            val2 = program[program[pc+2]]
        else:
            val2 = program[pc+2]
        
        sum = val1 * val2

        if self.modes[2] != 0:
            raise Exception
        else:
            program[program[pc+3]] = sum
        
        return 4

class Input(Instr):
    def __init__(self,modes):
        self.modes = modes
    
    def run(self, program, pc, inval):
        val = int(inval)
        program[program[pc+1]] = val
        return 2

class Output(Instr):
    def __init__(self,modes):
        self.modes = modes
    
    def run(self, program, pc):
        if self.modes[0] == 0:
            val = program[program[pc+1]]
        else:
            val = program[pc+1]

        return 2, val

class JumpTrue(Instr):
    def __init__(self, modes):
        self.modes = modes

    def run(self, program, pc):
        if self.modes[0] == 0:
            val = program[program[pc+1]]
        else:
            val = program[pc+1]
        
        if self.modes[1] == 0:
            ptr = program[program[pc+2]]
        else:
            ptr = program[pc+2]

        return ptr if val != 0 else pc+3

class JumpFalse(Instr):
    def __init__(self, modes):
        self.modes = modes

    def run(self, program, pc):
        if self.modes[0] == 0:
            val = program[program[pc+1]]
        else:
            val = program[pc+1]
        
        if self.modes[1] == 0:
            ptr = program[program[pc+2]]
        else:
            ptr = program[pc+2]

        return ptr if val == 0 else pc+3

class Less(Instr):
    def __init__(self, modes):
        self.modes = modes

    def run(self, program, pc):
        if self.modes[0] == 0:
            val1 = program[program[pc+1]]
        else:
            val1 = program[pc+1]
        
        if self.modes[1] == 0:
            val2 = program[program[pc+2]]
        else:
            val2 = program[pc+2]

        result = 1 if val1 < val2 else 0

        if self.modes[2] != 0:
            raise Exception
        else:
            program[program[pc+3]] = result
        
        return 4

class Equal(Instr):
    def __init__(self, modes):
        self.modes = modes

    def run(self, program, pc):
        if self.modes[0] == 0:
            val1 = program[program[pc+1]]
        else:
            val1 = program[pc+1]
        
        if self.modes[1] == 0:
            val2 = program[program[pc+2]]
        else:
            val2 = program[pc+2]

        result = 1 if val1 == val2 else 0

        if self.modes[2] != 0:
            raise Exception
        else:
            program[program[pc+3]] = result
        
        return 4

class Halt(Instr):
    def __init__(self, modes):
        pass

    def run(self, program, pc):
        return