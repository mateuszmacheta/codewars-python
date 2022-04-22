def barista(c):
    c = sorted(c)
    total = 0
    cleaning = 2
    for i in range(0, len(c)):
        first = c[0]
        rest = (len(c)-1)*(first+cleaning)
        print(f'adding {first} for first and {rest} for rest')
        total += first + rest
        c.pop(0)
    return total - (cleaning if c else 0)

print(barista([4,3,2]))