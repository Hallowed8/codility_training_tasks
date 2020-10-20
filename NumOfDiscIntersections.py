def getBounds(A):
    left_bounds = [i-A[i] for i in range(len(A))]
    right_bounds = [i+A[i] for i in range(len(A))]
    return left_bounds, right_bounds

def solution(A):
    if len(A) <= 1 or not A:
        return 0
    left_bounds, right_bounds = getBounds(A)
    left_bounds, right_bounds = zip(*sorted(zip(left_bounds, right_bounds)))
    num_of_crossings = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if num_of_crossings > 10**9:
                return -1
            if right_bounds[i] >= left_bounds[j] and left_bounds[j] >= left_bounds[i]:
                num_of_crossings += 1
            else:
                break
    return num_of_crossings


print(solution([1, 5, 2, 1, 4, 0 ]))