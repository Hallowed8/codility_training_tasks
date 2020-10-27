# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def kandaneAlg(A, reverse= False):
    current_max = [0]*len(A)
    if reverse:
        for idx in range(len(A)-3,0,-1):
            current_max[idx] = max(0, current_max[idx+1]+A[idx+1])
    else:
        for idx in range(2,len(A)-1):
            current_max[idx] = max(0, current_max[idx-1]+A[idx-1])
    return current_max        

def solution(A):
    kadane_right = kandaneAlg(A)
    kadane_left = kandaneAlg(A, reverse = True)
    maximum = 0
    for i in range(1,len(A)):
        maximum = max(maximum, kadane_left[i]+kadane_right[i])
    return maximum
