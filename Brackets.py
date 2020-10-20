def checkIfCont(char, char_list):
    for c in char_list:
        if c==char:
            return True
    return False

def solution(S):
    if len(S) == 0 or not S:
        return 1
    if len(S)%2 ==1:
        return 0
    left_brackets = ['{','[','(']
    right_brackets = ['}',']',')']
    if checkIfCont(S[0], right_brackets):
        return 0
    if checkIfCont(S[-1], left_brackets):
        return 0
    
    tmp_bra_list = []
    for i in range(len(S)):
        if checkIfCont(S[i],left_brackets):
            tmp_bra_list.append(S[i])
        elif checkIfCont(S[i], right_brackets):
            bra_idx = right_brackets.index(S[i])
            if len(tmp_bra_list) == 0:
                return 0
            if tmp_bra_list[-1] == left_brackets[bra_idx]:
                tmp_bra_list.pop()
            else:
                return 0
    if len(tmp_bra_list) > 0:
        return 0
    return 1