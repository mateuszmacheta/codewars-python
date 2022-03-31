def good_vs_evil(good, evil):
    good_power = [1, 2, 3, 3, 4, 10]
    evil_power = [1, 2, 2, 2, 3, 5, 10]
    result = 0
    i = 0
    for unit in good.split():
        result += int(unit) * good_power[i]
        i += 1
    i = 0
    for unit in evil.split():
        result -= int(unit) * evil_power[i]
        i += 1
    message = 'Battle Result: '
    if result > 0:
        message += 'Good triumphs over Evil'
    elif result == 0:
        message += 'No victor on this battle field'
    else:
        message += 'Evil eradicates all trace of Good'
    return message


print(good_vs_evil('0 0 0 0 0 10', '0 1 1 1 1 0 0'))