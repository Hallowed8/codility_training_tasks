""" Task description:
you are given integer N, your task is to find the 
biggest number that can be made by changing the order
of digits of aforemtioned integer 
example:
123 -> 321
545 -> 554
"""

def solution(N):
    digit_list = sorted([int(x) for x in str(N)])
    result = 0
    for i in range(len(digit_list)):
        result += digit_list[i]*(10**i)
    return result

print(solution(154))
