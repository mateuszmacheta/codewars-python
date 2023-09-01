# 6 kyu #02 - Music Theory - Validate rhythm
# https://www.codewars.com/kata/57091b473f1008c03f001a2a/train/python
from math import log2, floor

def validate_bar(meter_float: float, bar: str) -> bool:
    bar_float = sum(map(lambda c: 1 / int(c), bar))
    return meter_float == bar_float


def validate_rhythm(meter, score):
    log_meter_base = log2(meter[1])
    if not floor(log_meter_base) == log_meter_base:
        return 'Invalid rhythm'
    m_float = meter[0] / meter[1]
    score_list = score.split('|')
    score_valid = [False] * len(score_list)
    for i, bar in enumerate(score_list):
        score_valid[i] = validate_bar(m_float, bar)
        # case when we have any invalid bar that is not first or last
        if not score_valid[i] and i != 0 and i != len(score_list) - 1:
            return 'Invalid rhythm'
    
    # case where all bars are valid
    if all(score_valid): return 'Valid rhythm'

    # case for Anacrusis
    # # if first or last is valid then we cannot have Anacrusis as their combination will be invalid for sure
    if (score_valid[0] or score_valid[-1]):
        return 'Invalid rhythm'
    if validate_bar(m_float, score_list[0] + score_list[-1]):
        return 'Valid rhythm with anacrusis'
    return 'Invalid rhythm'

# print(validate_rhythm([4, 4], '4444|88888888|22|2488|1'), 'Valid rhythm')
# # print(validate_rhythm([5, 2], '22222|2244244|8888244888844|112'), 'Valid rhythm')
# # print(validate_rhythm([3, 8], '888|48|84'), 'Valid rhythm')

print(validate_rhythm([4, 4], '44|4444|884884|22|1|44'), 'Valid rhythm with anacrusis')
print(validate_rhythm([5, 2], '222|1144|41188|22'), 'Valid rhythm with anacrusis')
print(validate_rhythm([3, 8], '88|48|84|8'), 'Valid rhythm with anacrusis')