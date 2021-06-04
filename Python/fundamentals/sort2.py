arr=[8,5,2,6,3,1,9,4,0,7]

def bubblesort(arr):
    count=0
    for j in range (len(arr)-1):
        # print("\n\n","-"*20, "Iteration", j)
        for i in range (len(arr)-1-j):
            count+=1
            # print("\n","*"*80,"\nindex",i,"value", arr[i])
            # print("\n","*"*80,"\ncomparamos",arr[i],arr[i+1])
            if arr[i]>arr[i+1]:
                arr[i], arr[i+1] =arr[i+1], arr[i]
            #     print("intercambiamos", arr[i],arr[i+1])
            #     print("el array es",arr)
            # else:
            #     print("no necesita intercambirse")
    print("# de interacciones:",count)
    return arr

print(bubblesort(arr))