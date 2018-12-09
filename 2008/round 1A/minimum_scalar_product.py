
def solve(X, Y):
    # prepare so big numbers multiply with small
    X.sort()
    Y.sort()
    Y.reverse()

    # scalar element wise product
    total = 0
    for i, number in enumerate(X):
        total += number * Y[i]
    return total


T = int(raw_input())
for case in range(T):
    n = int(raw_input())
    v1 = list(map(int, raw_input().split(" ")))
    v2 = list(map(int, raw_input().split(" ")))

    solution = solve(v1, v2)

    print("Case #%i: %i" % (case+1, solution))

