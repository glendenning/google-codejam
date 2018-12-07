def toMinutes(t):
    # HH:MM to minutes
    h, m = t.split(":")
    return int(h)*60 + int(m)

def solve(T, NA, NB, NA_trips, NB_trips):
    
    # Sort the trips
    trips = []
    for trip in NA_trips:
        (d, a) = trip.split(" ") # departure and arrival times
        trips.append([toMinutes(d), toMinutes(a), 0])
    
    for trip in NB_trips:
        (d, a) = trip.split() # departure and arrival times
        trips.append([toMinutes(d), toMinutes(a), 1])
    trips.sort()

    num_trains = [0, 0]
    trains = [[], []]
    for (d, a, t) in trips:
        if len(trains[t]) == 0 or d < trains[t][0]:
            # if there is no train or departure time is less than lowest train
            # we need a new train to leave platform
            num_trains[t] += 1
        else:
            # there's a train that can do the trip
            del trains[t][0]
        trains[1 - t].append(a + T) # append time it arrives at opposite platform
        trains[1 - t].sort()        # sort by 

    return num_trains


N = input()
for case in range(N):
    T = input() # Turn around time
    NA, NB = map(int, raw_input().split(" "))
    NA_trips = [ raw_input() for i in range(NA) ]
    NB_trips = [ raw_input() for i in range(NB) ]

    num_trains = solve(T, NA, NB, NA_trips, NB_trips)

    print "Case #%i: %i %i" % (case+1, num_trains[0], num_trains[1])
 