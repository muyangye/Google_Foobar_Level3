# I studied AI at high school and recognized this is similar to MDP
# But MDP has rewards all those stuffs. I got my solution from a youtube playlist:
# https://www.youtube.com/watch?v=uvYTGEZQTEs&list=PLANMHOrJaFxPMQCMYcYqwOCYlreFswAKP
# This is a Absorbing Markov Chain with a limiting matrix because
# we are guranteed that there's a path from non-absorbing(normal) states to terminal states
# I did nothing but simply learned and implemented it. We can view terminal states as absorbing states
# because when we enter a terminal state, the only state we can go is itself (probability 1).
# The transition matrix from normal states to absorbing states is FR where F = (I-Q)^-1
# The program doesn't make sense, please view the playlist. And then my program is self-explanatory

from __future__ import division # Because Foobar uses Python 2.7 and that version uses integer division
import fractions # I love Python :)
import numpy # I love Python *2
def solution(m):
    # Your code here
    # Find greatest common divisor
    def gcd(num, remainder):
        if (remainder == 0):
            return num
        else:
            return gcd(remainder, num % remainder)
            
    # Starting state is the terminal state
    if (sum(m[0]) == 0):
        return [1] + [0] * (len(m)-2) + [1]

    # Read the input, translate it to transition matrix and
    # record how many absorbing/normal states are there and both states' corresponding indices
    numStates = len(m)
    numAbsStates = 0
    transition = [[0] * numStates for i in range(numStates)]
    absIndices = []
    normalIndices = []
    for i in range(numStates):
        total = sum(m[i])
        if (total == 0):
            transition[i][i] = 1
            numAbsStates += 1
            absIndices.append(i)
            continue
        normalIndices.append(i)
        for j in range(len(m[i])):
            transition[i][j] = m[i][j] / total
    numNormalStates = numStates - numAbsStates

    # I is the identity matrix which is going to (I-Q)^-1
    # So the size of Q and I must be the same. Will explain the size of Q later
    I = [[0] * numNormalStates for i in range(numNormalStates)]
    for i in range(numNormalStates):
        I[i][i] = 1
    
    # Q's size is (#normal) * (#normal) because in the video,
    # Q is the transition matrix from normal states to normal states
    Q = [[0] * numNormalStates for i in range(numNormalStates)]
    QCount = 0
    for normalIndex in normalIndices:
        QQCount = 0
        for normalIndex2 in normalIndices:
            Q[QCount][QQCount] = transition[normalIndex][normalIndex2]
            QQCount += 1
        QCount += 1
    
    # R's size is (#normal) * (#absorbing) because in the video,
    # R is the transition matrix from normal states to absorbing states
    R = [[0] * numAbsStates for i in range(numNormalStates)]
    RCount = 0
    for normalIndex in normalIndices:
        RRCount = 0
        for absIndex in absIndices:
            R[RCount][RRCount] = transition[normalIndex][absIndex]
            RRCount += 1
        RCount += 1
            
    # Calculate the fundamental matrix
    F = numpy.linalg.inv(numpy.subtract(I, Q))
    probs = numpy.matmul(F, R)[0]
    
    # Find least common multiple
    lcm = 1
    for prob in probs:
        # Turn floating point numbers to nearest fraction
        fraction = fractions.Fraction(prob).limit_denominator()
        lcm =  lcm * fraction.denominator // gcd(lcm, fraction.denominator)
    
    res = []
    for prob in probs:
        fraction = fractions.Fraction(prob).limit_denominator()
        res.append(int(fraction.numerator * (lcm/fraction.denominator)))
    res.append(lcm)
    return res