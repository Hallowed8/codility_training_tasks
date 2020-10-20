def solution1(S):
    #greedy algorithm
    number = int(S, 2)
    operation_counter = 0
    while number != 0:
        if number%2==0:
            number //=2
        else:
            number -= 1
        operation_counter +=1
    return operation_counter



def solution2(S):
    for i in S:
       if i==1:
           S = S[i:]
           break
    ones_counter = 0
    for x in S:
        if x =='1':
            ones_counter += 1
    return (len(S)-1 +ones_counter)

print(solution1('11110001101'))
print(solution2('11110001101'))