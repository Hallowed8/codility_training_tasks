def solution(N, A):
    counters = [0]*N
    max_counter = 0
    min_counter = 0
    for idx in range(1,len(A)):
        if idx <= N:
            if counters[idx-1] < min_counter:
                counters[idx-1] = min_counter + 1
            else:
                counters[idx-1] += 1
            
            if counters[idx-1] > max_counter:
                max_counter +=1
        else:
            min_counter = max_counter
    return counters

print(solution(5, [3, 4, 4, 6, 1, 4, 4]))
#expected :[3, 2, 2, 4, 2]