# Incorrect
def solve(N, M, customers):

    result = [0] * N
    changed = [False] * N

    for customer in customers:
        T = customer[0] # number of milkshakes customer likes
        satisfied = False
        for i in range(T):          # 0 1 2
            X = customer[i*2 + 1]   # milkshake number from 1 to N
            Y = customer[i*2 + 2]   # unmalted or malted (0 or 1)


            # if they a milkshake and can change it
            if (not changed[X - 1]):
                result[X - 1] = Y
                changed[X - 1] = True
                satisfied = True 
            elif(result[X - 1] == Y and not satisfied):
                satisfied = True

        if not satisfied:
            return "IMPOSSIBLE"

    return " ".join(str(x) for x in result)


C = int(raw_input())
for case in range(C):
    N = int(raw_input()) # num milkshake flavours
    M = int(raw_input()) # num of customers

    customers = []
    for i in range(M):
        customer = map(int, raw_input().split(" "))
        customers.append(customer)
    
    solution = solve(N, M, customers)

    print("Case #%i: %s" % (case+1, solution))