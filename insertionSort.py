
def insertSort(array):
    for i in range(0,len(array)-1):
        if i != len(array)-1:
            j = i
            while array[j] > array[j+1] and j >= 0:
                tmp = array[j]
                array[j] = array[j+1]
                array[j+1] = tmp
                j -= 1   
    return array


array = insertSort([100,5,2,4,6,1,3,0,-1])
print(str(array))
#[-1, 0, 1, 2, 3, 4, 5, 6, 100]
#o(n square)