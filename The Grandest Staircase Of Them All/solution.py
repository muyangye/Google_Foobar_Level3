def solution(n):
    # Your code here
    # top-down approach runtime limit, add memoization
    mem = [[0] * (n+2) for i in range(n+2)]
    def getNumPartition(curStairHeight, bricksRemain):
        if (mem[curStairHeight][bricksRemain] != 0):
            return mem[curStairHeight][bricksRemain]
        # there is just enought bricks to build the last stair
        if (bricksRemain == 0):
            return 1
        # no two stairs are the same height, next stair must be higher
        # if there is not enough bricks to build the next stair
        if (bricksRemain < curStairHeight):
            return 0
        # either build the stair now or build the next one(height)
        # if build, remaining will be less, otherwise no change
        result = getNumPartition(curStairHeight+1, bricksRemain-curStairHeight) + getNumPartition(curStairHeight+1, bricksRemain)
        mem[curStairHeight][bricksRemain] = result
        return result
    return getNumPartition(1, n) - 1