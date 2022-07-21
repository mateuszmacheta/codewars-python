# 6 kyu Pokemon Damage Calculator
# https://www.codewars.com/kata/536e9a7973130a06eb000e9f

BASE_DAMAGE = 50


def calculate_damage(your_type, opponent_type, attack, defense):
    multipliers = {'very': 2, 'normal': 1, 'low': 0.5}
    effectiveness = ''

    def get_effectiveness(your_type, opponent_type):
        if your_type == opponent_type:
            return 'low'
        table = '''fire > grass
fire < water
fire = electric
water < grass
water < electric
grass = electric'''
        table = [line.split() for line in table.split('\n')]
        for line in table:
            if your_type in line and opponent_type in line:
                if line[1] == '=': return 'normal'
                if line[1] == '>':
                    if line[0] == your_type: return 'high'
                    return 'low'
                if line[0] == your_type: return 'low'
                return 'high'

    effectiveness = get_effectiveness(your_type, opponent_type)
    return BASE_DAMAGE * (attack / defense) * multipliers[effectiveness]


if __name__ == '__main__':
    print(calculate_damage("fire", "water", 100, 100), 25)