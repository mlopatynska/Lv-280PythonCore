import collections
print collections.Counter("collaboration")



word = 'constitution'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print d

