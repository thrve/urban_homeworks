#!/usr/bin/env python


def password(n):

    pairs = []
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                pairs.append(str(i) + str(j))
    return "".join(pairs)


for num in range(3, 21):
    print(password(num))
