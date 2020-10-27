def prefixSum(A):
    prefix_sum = [0]
    current_sum = 0
    for a in A:
        current_sum +=a
        prefix_sum.append(current_sum)
    return prefix_sum

def minimalSliceSum(prefix_sum, slice_length):
    minimal_sum = prefix_sum[slice_length]
    min_idx = 0
    for i in range(len(prefix_sum)-slice_length):
        curr_slice_sum = prefix_sum[i+slice_length] - prefix_sum[i]
        if curr_slice_sum < minimal_sum:
            minimal_sum = curr_slice_sum
            min_idx = i
    return minimal_sum, min_idx
        
    
def solution(A):
    prefix_A = prefixSum(A)
    min_two_slice, two_slice_idx = minimalSliceSum(prefix_A, 2)
    if len(A)>=3:
        min_three_slice, three_slice_idx = minimalSliceSum(prefix_A, 3)
        if min_two_slice*3 > min_three_slice*2:
            return three_slice_idx
        elif min_two_slice*3 == min_three_slice*2:
            return min([two_slice_idx, three_slice_idx])
    return two_slice_idx

print(solution([0,0,0,0]))