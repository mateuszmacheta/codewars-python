def parse(data):
    output = []
    value = 0
    for char in data:
        if char == 'i':
            value += 1
        elif char == 'd':
            value -= 1
        elif char == 's':
            value *= value
        elif char == 'o':
            output.append(value)
    return output
