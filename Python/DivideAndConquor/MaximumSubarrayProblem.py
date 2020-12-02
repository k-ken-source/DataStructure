import sys 
#Find the subarray with maximum sum using divide and conquer technique??
#Problem is based on given stock, we need to earn maximum profit by buying a stock and selling it once.

def MaxCross(L,low,high,mid):
    lsum = -(sys.maxsize)
    rsum = -(sys.maxsize)
    sum = 0
    i = mid 
    while i>=low:
        sum += L[i]
        if sum > lsum:
            lsum = sum
        i-=1
    
    i = mid+1
    sum = 0 
    while i<high:
        sum += L[i]
        if sum > rsum:
            rsum  = sum 
        i+=1

    return lsum+rsum 

def SubArrayMaxSum(L,low, high):
    print("Low, High",low,high)
    #Base Conditions 
    if low == high:
        try:
            return L[low]
        except:
            return 0
    
    mid = (low+high)//2
    left  = SubArrayMaxSum(L,low,mid)
    right = SubArrayMaxSum(L,mid+1,high)
    cross = MaxCross(L,low,high,mid)

    return max(max(left,right),cross)

if __name__ == "__main__":
    n = int(input("number of elements"))

    #Input in form of stock rates 

    StockRates = list(map(int,input().split()))
    arr=[]
    
    #Convert it into the change in stock price and find the max profit i.e subarray with maximum sum
    for i in range(1,n):
        arr.append(StockRates[i] - StockRates[i-1])
    print("Arr",arr)

    print(SubArrayMaxSum(arr,0,len(arr)))

