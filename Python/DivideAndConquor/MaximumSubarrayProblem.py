#Find the subarray with maximum sum using divide and conquer technique??

def MaxCross(L,low,high,mid):
    

def SubArrayMaxSum(L,low, high):
    #Base Conditions 
    if low == high:
        return L[low]
    
    m = (low+high)//2
    left  = SubArrayMaxSum(L,low,m)
    right = SubArrayMaxSum(L,m+1,high)

    cross = MaxCross(L,low,high,mid)

    return max(max(left,right),cross)


if if __name__ == "__main__":
    n = int(input("number of elements"))
    arr = list(map(int,input().split()))
    print(SubArrayMaxSum(arr,0,n))
