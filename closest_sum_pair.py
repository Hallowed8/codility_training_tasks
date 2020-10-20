# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def seqToMinImpFac(Seq_str):
    Seq_list = []
    for s in Seq_str:
        if s =='A':
            Seq_list.append(1)
        elif s == 'C':
            Seq_list.append(2)
        elif s == 'G':
            Seq_list.append(3)
        elif s == 'T':
            Seq_list.append(4)
    return Seq_list

def getSmallestImp(S_list, min_idx, max_idx):
    min_imp = 5
    for i in range(min_idx, max_idx+1):
        if S_list[i] < min_imp:
            min_imp = S_list[i]
        if min_imp == 1:
            return min_imp
    return min_imp

def solution(S, P, Q):
    S_list = seqToMinImpFac(S)
    min_impact_fac = []
    for m in range(len(P)):
        min_impact_fac.append(getSmallestImp(S_list, P[m], Q[m]))
    return min_impact_fac