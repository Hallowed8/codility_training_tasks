def solution(X, A):
    leaves = [False]*(X+1) # list cotaining information about presention of leaves on positions corresponing to indexes
    leaves[0] = True
    counter = 0
    for idx, a in enumerate(A):
        if a < X+1:
            if leaves[a] == False:
                leaves[a] = True
                counter +=1
                if counter == X:
                    return idx
                
    return -1
