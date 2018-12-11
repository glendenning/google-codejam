import math

def solve(n):

    result = (3 + math.sqrt(5)) ** n

    result = str(result).split('.')[0]

    result = result[-3:].zfill(3)

    return result


T = int(raw_input())
for case in range(T):

    n = int(raw_input())

    solution = solve(n)

    print("Case #%i: %s" % (case+1, solution))