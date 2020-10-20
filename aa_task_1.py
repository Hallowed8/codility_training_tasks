def solution(N):
    digit_list = sorted([int(x) for x in str(N)])
    result = 0
    for i in range(len(digit_list)):
        result += digit_list[i]*(10**i)
    return result
