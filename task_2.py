""" 
Task:
you are given string S which denotes a binary number such that it may contain trailing zeros
You must return number of operations needed to reduce its base10 form to zero. Two operations are allowed:
1. if the number is odd: subtract 1
2. if the number is even: divide by 2 
"""

def solution1(S):
    #greedy algorithm
    #simply do allowed operations till
    #the given number equals 0
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
    # More efficient solution:
    # It turns out that number of required operations equals:
    # the lenght of the number in binary form(without trailing zeros) + number of ones in it -1
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