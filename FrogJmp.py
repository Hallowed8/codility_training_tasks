# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def solution(X, Y, D):
    to_travel = Y-X
    num_of_jumps = to_travel/D
    if not num_of_jumps.is_integer():
        num_of_jumps = int(num_of_jumps) + 1
    return num_of_jumps

print(solution(0,80,20))
