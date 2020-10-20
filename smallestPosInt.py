def solution(A, B, K):
    num_of_div = 0
    for i in range(A, B+1):
        if i%K == 0:
            K +=1
    return K

print(solution(6, 11, 2))