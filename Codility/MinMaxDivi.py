# You are given integers K, M and a non-empty array A consisting of N integers. Every element of the array is not greater than M.
# You should divide this array into K blocks of consecutive elements. The size of the block is any integer between 0 and N. Every element of the array should belong to some block.
# The sum of the block from X to Y equals A[X] + A[X + 1] + ... + A[Y]. The sum of empty block equals 0.
# The large sum is the maximal sum of any block.
# Write a function:
# def solution(K, M, A)
# that, given integers K, M and a non-empty array A consisting of N integers, returns the minimal large sum.

# %100 correct, %100 performance
def solution(K, M, A):
    low = max(A)
    high = sum(A)

    lastValidVal = high
    while low <= high:
        mid = (low + high) // 2

        isMidValidSum = True
        currBlock = 1
        currBlockSum = 0
        # There has to be a group with a sum of mid since the only difference between mid-1 and mid is
        # accepting blocks with sums mid. Towards the end of the binary search search space will be confined to
        # one or two values and that's why we come to comparing mid-1/mid or mid/mid+1 eventually.
        for a in A:
            if currBlockSum + a > mid:
                currBlockSum = a
                currBlock += 1
            else:
                currBlockSum += a
            if currBlock > K:
                isMidValidSum = False

        if isMidValidSum:
            lastValidVal = mid
            high = mid - 1
        else:
            low = mid + 1

    return lastValidVal