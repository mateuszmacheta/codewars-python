def stock_list(L, M):
    print(f"L {L}")
    print(f"M {M}")
    if not L or not M: return ''
    counts = {}
    for e in L:
        category = e[0]
        if category in M:
            if category in counts:
                counts[category] += int(e.split()[1])
            else:
                counts[category] = int(e.split()[1])
    return ' - '.join(['({} : {})'.format(e, counts.get(e, 0)) for e in M])


b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]
d = ['BBAR 150', 'CDXE 515', 'BKWR 250', 'BTSQ 890', 'DRTY 600']
e = ['A', 'B', 'C', 'D']

print(stock_list(d, e))