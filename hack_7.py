"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = []
    j=5
    while j>= 0:
        result.append(j)
        j -= 1
    return result  