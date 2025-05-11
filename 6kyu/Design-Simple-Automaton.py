# 6 kyu Design a Simple Automaton (Finite State Machine)
# https://www.codewars.com/kata/5268acac0d3f019add000203

class Automaton(object):

    def __init__(self):
        self.states = {'q1': False, 'q2': True, 'q3': False}
        self.state = 'q1'

    def read_commands(self, commands):
        for command in commands:
            if self.state == 'q1':
                if command == '1':
                    self.state = 'q2'
            elif self.state == 'q2':
                if command == '0':
                    self.state = 'q3'
            elif self.state == 'q3':
                self.state = 'q2'
            print(f'current state {self.state} after command {command}')

        return self.states[self.state]


if __name__ == '__main__':
    my_automaton = Automaton()
    print(my_automaton.read_commands(["1"]))
    print(my_automaton.read_commands(["1", "0", "0", "1"]))