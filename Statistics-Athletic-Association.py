# 6 kyu Statistics for an Athletic Association
# https://www.codewars.com/kata/55b3425df71c1201a800009c/train/python
from statistics import median


def stat(s):
    if not s: return s
    times = s.replace(' ', '').split(',')
    seconds = [to_seconds(e) for e in times]
    range = max(seconds) - min(seconds)
    average = sum(seconds)/len(seconds)
    med = median(seconds)
    return 'Range: {} Average: {} Median: {}'.format(format_seconds(range),
                                                     format_seconds(average),
                                                     format_seconds(med))


def to_seconds(e):
    e = e.split('|')
    hours, minutes, seconds = int(e[0]), int(e[1]), int(e[2])
    return hours * 3600 + minutes * 60 + seconds


def format_seconds(s):
    return "{:02.0f}|{:02.0f}|{:02.0f}".format(s // 3600, (s // 60) % 60, s % 60 // 1)


if __name__ == '__main__':
    print(stat("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17"))