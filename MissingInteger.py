def solution(A, B, K):
    num_of_div = 0
    for i in range(A, B+1):
        if i%K == 0:
            num_of_div +=1
    return num_of_div

print(solution(6, 11, 2))