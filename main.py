from collections import defaultdict

def first_non_repeated(s):
    seen = defaultdict(int)
    for c in s:
        seen[c] += 1
    for key, value in seen.items():
        if value == 1:
            return key

print(first_non_repeated("test"),'e')
print(first_non_repeated("teeter"),'r')
print(first_non_repeated("1122321235121222"),'5')