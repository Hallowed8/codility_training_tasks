def countEl(A,max):
    counted = [0]* (max+1)
    for i in range(len(A)):
        counted[A[i]] +=1
    return counted
def solution(A, B, m):
    diff = abs(sum(A) - sum(B))
    counted_A = countEl(A,m)
    counted_B = countEl(B,m)
    if diff % 2 ==1:
        return False
    for i in range(len(A)):
        if counted_A[i] == 0:
            continue
        if diff-i >= 0 and diff - i <= m and counted_B[diff-i] > 0:
            return True
        else:
            return False

print(solution([0,0,5,0,1,0,1], [1,2,2,3,1,0,0],5))