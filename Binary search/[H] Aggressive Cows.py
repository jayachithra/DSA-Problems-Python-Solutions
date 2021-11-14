# https://www.spoj.com/problems/AGGRCOW/

# Farmer John has built a new long barn, with N (2 <= N <= 100,000) stalls. The stalls are located along a straight line at positions x1,...,xN (0 <= xi <= 1,000,000,000).

# His C (2 <= C <= N) cows don't like this barn layout and become aggressive towards each other once put into a stall. To prevent the cows from hurting each other, FJ wants to assign the cows to the stalls, such that the minimum distance between any two of them is as large as possible. What is the largest minimum distance?
# Input
# t – the number of test cases, then t test cases follows.
# * Line 1: Two space-separated integers: N and C
# * Lines 2..N+1: Line i+1 contains an integer stall location, xi
# Output
# For each test case output one integer: the largest minimum distance.
# Example
# Input:

# 1
# 5 3
# 1
# 2
# 8
# 4
# 9
# Output:

# 3
# Output details:

# FJ can put his 3 cows in the stalls at positions 1, 4 and 8,
# resulting in a minimum distance of 3.


def aggCows(N, C, NLoc):
    # Search space is the number of minimum and maximum possible distances within the given slots
    start = 1
    end = max(NLoc) - min(NLoc)
    while start <= end:
        mid = start + (end - start)//2  
        cowsallocated, lastreachedstallidx = allocateCows(NLoc, mid, C)           
        # If not all cows are allocated then reduce mid
        if cowsallocated < C:
            end = mid-1
        # Else do an exhaustive binary search until you find the max distance
        else:
            lastallocated = mid
            start = mid + 1
        
    return lastallocated
            
def allocateCows(NLoc, mid, C):
    cowsallocated = 0
    prevallocatedspot = 0
    for spotidx, spot in enumerate(NLoc):
        if spotidx == 0: # ALways allocate the first cow to the first spot
            cowsallocated += 1
            prevallocatedspot = spot
        elif spot - prevallocatedspot >= mid: # Allocate next cow to the nearest spot after mid distance
                cowsallocated += 1
                prevallocatedspot = spot
        if cowsallocated == C: # If all the cows are allocated exit loop
            return cowsallocated, spotidx
        
    return cowsallocated, spotidx

    
# TEST CASES HERE
if __name__=="__main__":
    # print(aggCows(5, 3, [1, 2, 4, 8, 9]))
    print(aggCows(5, 3, [1, 2, 4, 5, 6]))
    