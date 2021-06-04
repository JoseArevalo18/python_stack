arr=[8,5,2,6,3,1,9,4,0,7]

def bubblesort(arr):
    count=0
    for j in range (len(arr)-1):
        for i in range (len(arr)-1-j):
            count+=1
            if arr[i]>arr[i+1]:
                arr[i], arr[i+1] =arr[i+1], arr[i]
    print("# de interacciones:",count)
    return arr

print(bubblesort(arr))