def reverse_lookup(d,v):
    l = list()
    for c in d:
        if d[c] == v:
            l.append(c)
    return l