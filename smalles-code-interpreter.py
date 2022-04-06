# 5 kyu My smallest code interpreter (aka Brainf**k)
# https://www.codewars.com/kata/526156943dfe7ce06200063e

import numpy as np


class Interpreter:
    def __init__(self, code, program_input):
        REGISTER_SIZE = 9000
        self.code = code
        self.input = program_input
        self.code_pointer = 0
        self.input_pointer = 0
        self.register_pointer = 0
        self.register = np.zeros(REGISTER_SIZE, dtype='uint8')

    def compute(self):
        output = ''
        while self.code_pointer < len(self.code):
            command = self.code[self.code_pointer]
            if command == '+':
                self.register[self.register_pointer] += 1
                self.code_pointer += 1
            elif command == '-':
                self.register[self.register_pointer] -= 1
                self.code_pointer += 1
            elif command == '>':
                self.register_pointer += 1
                self.code_pointer += 1
            elif command == '<':
                self.register_pointer -= 1
                self.code_pointer += 1
            elif command == '.':
                output += chr(self.register[self.register_pointer])
                self.code_pointer += 1
            elif command == ',':
                self.register[self.register_pointer] = ord(self.input[self.input_pointer])
                self.input_pointer += 1
                self.code_pointer += 1
            elif command == '[':
                if not self.register[self.register_pointer] == 0:
                    self.code_pointer += 1
                else:
                    self.end_loop()
            elif command == ']':
                if self.register[self.register_pointer] == 0:
                    self.code_pointer += 1
                else:
                    self.repeat_loop()
        return output

    def end_loop(self):
        matching = 0
        while True:
            self.code_pointer += 1
            if self.code[self.code_pointer] == '[':
                matching += 1
            elif self.code[self.code_pointer] == ']' and matching != 0:
                matching -= 1
            elif self.code[self.code_pointer] == ']':
                self.code_pointer += 1
                break
        return 1

    def repeat_loop(self):
        matching = 0
        while True:
            self.code_pointer -= 1
            if self.code[self.code_pointer] == ']':
                matching += 1
            elif self.code[self.code_pointer] == '[' and matching != 0:
                matching -= 1
            elif self.code[self.code_pointer] == '[':
                self.code_pointer += 1
                break
        return 1


def brain_luck(code, program_input):
    brainfuck = Interpreter(code, program_input)
    return brainfuck.compute()


#print(brain_luck(',+[-.,+]', 'Codewars' + chr(255)))
#print(brain_luck(',[.[-],]', 'Codewars' + chr(0)))
print(brain_luck(',>+>>>>++++++++++++++++++++++++++++++++++++++++++++>++++++++++++++++++++++++++++++++<<<<<<[>[>>>>>>+>+<<<<<<<-]>>>>>>>[<<<<<<<+>>>>>>>-]<[>++++++++++[-<-[>>+>+<<<-]>>>[<<<+>>>-]+<[>[-]<[-]]>[<<[>>>+<<<-]>>[-]]<<]>>>[>>+>+<<<-]>>>[<<<+>>>-]+<[>[-]<[-]]>[<<+>>[-]]<<<<<<<]>>>>>[++++++++++++++++++++++++++++++++++++++++++++++++.[-]]++++++++++<[->-<]>++++++++++++++++++++++++++++++++++++++++++++++++.[-]<<<<<<<<<<<<[>>>+>+<<<<-]>>>>[<<<<+>>>>-]<-[>>.>.<<<[-]]<<[>>+>+<<<-]>>>[<<<+>>>-]<<[<+>-]>[<+>-]<<<-]', chr(10)))