#problem 10.1 Sorted Merge


def sortme(a ,b ):
    for i in b:
        insertIndex = binSearch(a,i)
        a.insert( insertIndex, i)
        print("Element passed: ", i, "Index to go to: ", insertIndex)
        print(a)

    

def binSearch(a, element):
    start = 0
    mid = len(a) //2
    end = len(a) 
    insertFlag = False
    insertindex = 0
    if a[0] >= element:
        insertindex = 0
    elif a[-1] < element:
        insertindex = end
    else:
        while not insertFlag:
            if a[mid] < element:
                if a[mid + 1] >= element:
                    insertFlag = True
                    insertindex = mid+1
                else:   # log behavior 
                    start = mid
                    mid = (start+end) //2 

            else:
                if a[mid -1 ] <= element:
                    insertFlag = True
                    insertindex = mid
                else:
                    end = mid
                    mid = (start + end) //2
    return insertindex






A = [1,2,3,7,10,13]
B = [1.2, -22]
sortme(A,B)
print(A)




