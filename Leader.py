def findDomi(A):
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
    if len(A) ==0 or not A:
        return -1
    if len(A) == 2:
        return -1
    if len(A)==1:
        return 0
    dom = findDomi(A)
    if dom == None:
        return -1
    dom_idx = [i for i, a in enumerate(A) if a ==dom]
    return dom_idx

print(solution([3, 4, 3, 2, 3, -1, 3, 3]))