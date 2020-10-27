def solution(N, A):
    counters = [0]*N
    max_counter = 0
    min_counter = 0
    for value in A:
        if value<=N:
            if counters[value-1] < min_counter:
                counters[value-1] = min_counter + 1
            else:
                counters[value-1] += 1
            if counters[value-1] > max_counter:
                max_counter += 1
        else:
            min_counter = max_counter
    counters = [min_counter if con < min_counter else con for con in counters]
    return counters

print(solution(5, [3, 4, 4, 6, 1, 4, 4]))
#expected :[3, 2, 2, 4, 2]