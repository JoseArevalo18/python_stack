arr=[8,5,2,6,3,1,9,4,0,7]

def bubbleinsort(arr):
    for indice in range (1,len(arr)):
        count=0
        valor = arr[indice]
        i = indice - 1
        while i >=0:
            count+=1
            if valor < arr[i]:
                arr[i+1]=arr[i]
                arr[i]=valor
                i=i-1
            else:
                break
    print("#de interacciones",count)
    return arr
print(bubbleinsort(arr))