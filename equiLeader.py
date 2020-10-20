def findDomi(A):
    if len(A) == 1:
        return A[0]
    A=sorted(A)
    counter = 1
    for i in range(len(A)-1):
        if A[i+1]==A[i]:
            counter +=1
            if counter > len(A)//2:
                return A[i]
        else:
            counter == 1
    return None

def solution(A):
    num_equi = 0
    for i in range(1,len(A)):
        if findDomi(A[:i])== findDomi(A[i:]):
            num_equi +=1
    return num_equi

print(solution([4, 3, 4, 4, 4, 2]))