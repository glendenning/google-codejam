import sys

def solve(S,Q):
    a = set(S) # List of unique search engine names
    count = 0
    for q in Q:
        if q in a:
            # If query is a search engine name
            # remove the search engine name from a
            a.remove(q)
            if len(a) == 0:
                # if the set of search engines is exausted
                count += 1
                a = set(S) # reset the search engine
                a.remove(q) # remove search engine from new a
    return count

for case in range(input()):
    S = [ raw_input() for i in range(input()) ]
    Q = [ raw_input() for i in range(input()) ]
    print "Case #%i: %i" % (case+1, solve(S,Q))