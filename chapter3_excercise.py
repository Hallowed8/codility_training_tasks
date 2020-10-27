def getPos(A):
        #this function returns a list containing only ascending positive integers of the input list 
        A = sorted(A)
        Pos_int = []
        for i in A:
            if i>=0:
                Pos_int.append(i)
        return Pos_int

def solution(A):
    Pos_A = getPos(A)
    if len(Pos_A)==0:
        return 1

    if min(Pos_A)>1:
        return 1
    
    for i in range(len(Pos_A)-1):
        if Pos_A[i+1]-Pos_A[i]>1:
            return Pos_A[i]+1
    
    if max(Pos_A)>0:
        return max(Pos_A)+1
pass
print(solution([0]))