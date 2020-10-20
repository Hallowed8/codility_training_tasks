# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def prefixSum(A):
    prefix_sum = [0]
    current_sum = 0
    for a in A:
        current_sum +=a
        prefix_sum.append(current_sum)
    return prefix_sum

def suffixSum(A):
    prefix_sum = prefixSum(A)
    suffix_sum = []
    for i in range(len(prefix_sum)):
        suffix_sum.append(prefix_sum[-1]-prefix_sum[i])
    return suffix_sum



def solution(A):
    car_trav_west = suffixSum(A)
    total_car_passed = 0
    for i in range(len(A)):
        if A[i]==0:
            total_car_passed += car_trav_west[i]
            if(total_car_passed > 10**9):
                return -1
    return total_car_passed

print(solution([0, 1, 0, 1, 1]))