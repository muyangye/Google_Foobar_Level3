def solution(start, length):
    # Your code here
    res = 0
    count = start
    for i in range(length):
        for j in range(length-i):
           res ^= count + j
        count += length
    return res