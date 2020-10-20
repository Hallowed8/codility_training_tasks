def solution(S, P, Q):
    A_prefix = prefixSum(S, 'A')
    C_prefix = prefixSum(S, 'C')
    G_prefix = prefixSum(S, 'G')
    min_impact_factor = []
    for i in range(len(P)):
        inner_sum_A =A_prefix[Q[i]+1] -  A_prefix[P[i]]
        if inner_sum_A != 0:
            min_impact_factor.append(1)
            continue
        inner_sum_C = C_prefix[Q[i]+1] - C_prefix[P[i]]
        if inner_sum_C != 0:
            min_impact_factor.append(2)
            continue
        inner_sum_G = G_prefix[Q[i]+1] - G_prefix[P[i]]
        if inner_sum_G != 0:
            min_impact_factor.append(3)
            continue
        else:
            min_impact_factor.append(4)
    return min_impact_factor

def prefixSum(S, char):
    prefix_sum = [0]
    current_sum = 0
    for character in S:
        if character == char:
            current_sum +=  1
        prefix_sum.append(tmp_sum)
    return prefix_sum

print(solution('CAGCCTA', [2, 5, 0], [4, 5, 6]))