# 5 kyu The Hashtag Generator
# https://www.codewars.com/kata/52449b062fb80683ec000024

def generate_hashtag(s: str):
    if len(s) == 0:
        return False
    s = s.title()
    s = '#' + s.replace(' ', '')
    if len(s) > 140:
        return False
    return s

print(generate_hashtag('CodeWars is nice'))