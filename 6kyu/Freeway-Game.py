# 6 kyu The Freeway Game
# https://www.codewars.com/kata/59279aea8270cc30080000df/train/python

def freeway_game(km, mspeed, o):
    print(km, mspeed, o)
    t = km / mspeed
    score = 0
    for t_relative, speed in o:
        position = -t_relative * speed / 60
        # if initially car was behind but overtook us
        if position < 0 and position + speed * t > km:
            score -= 1
        # if initially cas was ahead but we overook it
        elif position > 0 and position + speed * t < km:
            score += 1
    return score


if __name__ == '__main__':
    # cant overtake faster cars
    print(freeway_game(30.0, 100.0, [[-1.0, 110.0], [-0.7, 102.0], [-1.5, 108.0]]))