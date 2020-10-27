'''
This task is to calculate the number of identicals.
identical is a pair of indexes of input A array which contain the same value
'''

def solution(A):
    A = sorted(A)
    counter = 1
    identicals = 0
    for i in range(len(A)-1):
        if A[i] == A[i+1]:
            counter +=1
        elif counter >= 2:
            identicals  += sum(range(counter))
            counter = 1
    return identicals

print(solution([3, 5, 6, 3, 3, 5]))
