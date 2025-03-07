"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    foo = []
    baz = 0

    while baz < len(result):
        foo.append(result[baz])
        foo.append('@')
        baz += 1
    return foo 