def solution(N):
    num_of_divisors = 0
    i=1
    while i*i<N:
        if N%i ==0:
            num_of_divisors +=2
        i +=1
    if i*i ==N:
        num_of_divisors+=1
    return num_of_divisors

print(solution(64))