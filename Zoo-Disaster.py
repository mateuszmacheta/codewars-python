# 5 kyu The Hunger Games - Zoo Disaster!
# https://www.codewars.com/kata/5902bc7aba39542b4a00003d/train/python

rules = {
    'antelope': 'grass',
    'big-fish': 'little-fish',
    'bug': 'leaves',
    'bear': 'big-fish;bug;chicken;cow;leaves;sheep',
    'chicken': 'bug',
    'cow': 'grass',
    'fox': 'chicken;sheep',
    'giraffe': 'leaves',
    'lion': 'antelope;cow',
    'panda': 'leaves',
    'sheep': 'grass'}


class Eating:
    def __init__(self, zoo: list, rules: dict):
        self.zoo = zoo
        self.rules = rules
        self.alive = [True]*len(zoo)
        self.messages = []

    def __str__(self):
        return ','.join(animal for i, animal in enumerate(self.zoo) if self.alive[i])

    def get_left(self, i):
        shift = 1
        while -1 < i - shift < len(self.zoo):
            if not self.alive[i - shift]:
                shift += 1
            else:
                return i - shift
        return None

    def get_right(self, i):
        shift = 1
        while -1 < i + shift < len(self.zoo):
            if not self.alive[i + shift]:
                shift += 1
            else:
                return i + shift
        return None

    def cycle(self):
        eaten = False
        for i, animal in enumerate(self.zoo):
            if not self.alive[i]:
                continue
            print(f'{animal} looking left')
            left_i = self.get_left(i)
            if left_i is not None and animal in self.rules and self.zoo[left_i] in self.rules[animal]:
                # EATING
                eaten = True
                self.alive[left_i] = False
                message = f'{animal} eats {self.zoo[left_i]}'
                print(message)
                self.messages.append(message)
                return eaten
            print(f'{animal} looking right')
            right_i = self.get_right(i)
            if right_i is not None and animal in self.rules and self.zoo[right_i] in self.rules[animal]:
                # EATING
                eaten = True
                self.alive[right_i] = False
                message = f'{animal} eats {self.zoo[right_i]}'
                print(message)
                self.messages.append(message)
                return eaten

        return eaten


def who_eats_who(zoo):
    e = Eating(zoo.split(','), rules)
    i = 0
    while e.cycle():
        print(i)
        i += 1
    return [zoo, *e.messages, str(e)]


if __name__ == '__main__':
    # input = "fox,bug,chicken,grass,sheep"
    # expected = ["fox,bug,chicken,grass,sheep",
    #             "chicken eats bug",
    #             "fox eats chicken",
    #             "sheep eats grass",
    #             "fox eats sheep",
    #             "fox"]
    # print(who_eats_who(input))
    print(who_eats_who('chicken,fox,leaves,bug,grass,sheep'))