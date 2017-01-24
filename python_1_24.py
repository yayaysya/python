# hannuo problem
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def hannuo(n, a, b, c):
    if n is 1:
        print(a,'--->',c)
    else:
        hannuo(n-1, a, c, b)
        hannuo(1, a, b, c)
        hannuo(n-1, b, a, c)

hannuo(4,'A','B','C')

