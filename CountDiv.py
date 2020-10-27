def smallestDiv(A,B,K):
    for i in range(A, A+K+1):
        if i%K == 0:
            return K
    return None

def solution(A, B, K):
    a = smallestDiv(A,B,K)
    if a == None:
        return 0
    else:
        total_div = B//K
        min_div = (a-1)//K
        return total_div-min_div

print(solution(10,54,1))