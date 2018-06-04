def pairsum(arr,n,s):
    for i in range(0,n-1):
        if arr[i]>arr[i+1]:
            break
    l=(i+1)%n
    r=i

    while l!=r:
        if arr[l]+arr[r]==s:
            print('%d and %d' %(arr[l],arr[r]))
            return True
        elif arr[l]+arr[r]<s:
            l=(l+1)%n
        else:
            r=(n+r-1)%n
    return False
    



arr=[11,15,26,38,9,10]
s=35
n=len(arr)
if pairsum(arr,n,s):
    print "Pair found"
else:
    print "Pair not found"
