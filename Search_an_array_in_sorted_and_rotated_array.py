def search(arr,l,h,key):
    if l>h:                                                                         # If the low index is greater than high index
        return -1
    mid=(l+h)//2                                                                    # Get the middle index
    if key==arr[mid]:                                                               # check whether key matches for the middle number
        return mid
    if arr[l]<=arr[mid]:                                                            # check left half whether sorted or not
        if key>=arr[l] and key<=arr[mid]:
            return search(arr,l,mid-1,key)                                          # if key is present in the left sotred half recur from arr[l] to arr[mid-1]
        return search(arr,mid+1,h,key)                                              # else recur arr[mid+1] to arr[h]
    if key>=arr[mid] and key<=arr[h]:
        return search(arr,mid+1,h,key)
    return search(arr,l,mid-1,h,key)

arr=[1,2,7,4,3]
p = search(arr,0,len(arr)-1,2)
if p != -1:
    print(p)
else:
    print("OOPS! NOT FOUND")
