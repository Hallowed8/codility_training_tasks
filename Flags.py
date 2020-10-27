# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def getPeaks(A):
    peaks = []
    for i in range(1,len(A)-1):
        if A[i-1]< A[i] and A[i] > A[i+1]:
            peaks.append(i)
    return peaks

def getMaxFlags(peaks):
    max_flags = 0
    current_max_flags = 0
    last_peak = 0
    for K_flags in range(1,len(peaks)+1):
        flags = 1
        dis = 0
        last_peak = peaks[0]
        for peak in peaks:
            dis = peak - last_peak
            if dis >= K_flags:
                flags +=1
                dis =0
                last_peak = peak
                if flags >= K_flags:
                    max_flags = K_flags
                    break
        
        current_max_flags = max(flags, max_flags)
        if current_max_flags >= max_flags:
            max_flags = current_max_flags
        else:
            return max_flags

    return max_flags

        
def solution(A):
    peaks = getPeaks(A)
    if len(peaks) == 1:
        return 1 
    max_flags = getMaxFlags(peaks)
    return max_flags

print(solution([1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]))