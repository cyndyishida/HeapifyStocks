#problem 10.1 Sorted Merge
'''

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


'''


'''
#DP 

careful brute force 

text justification
longest common subsequence
'''
def lcs(x,y):
    # row - y len
    # col - x len
    LCS = [[0 for col in range(len(x) + 1 )] for row in range(len(y) +1 ) ]
    
    
     # iterate through one word 
     # iterate through the second, if theres a match take the diagonal & add 1
     # else take the max val between the left or up node
    for i in range(1,len(y)+1):
        for j in range(1,len(x)+1):
                if y[i-1] == x[j-1]:
                    LCS[i][j] = LCS[i-1][j-1] + 1
                else:
                    LCS[i][j] = max(LCS[i-1][j],LCS[i][j-1])
                
                
    # to find the longest common subsequence  start from the last corner 
    # if that number isn't the same as the left and up node add the adjcent character 
    # if the number is same as left move pointer there else move pointer to the above node
    word = []
    while (len(word) != LCS[-1][-1]):
        if LCS[i][j] != LCS[i][j-1] and LCS[i][j] != LCS[i-1][j]: 
            word.append(x[j-1])
            i -= 1
            j -= 1
        elif LCS[i][j] ==  LCS[i-1][j]: # matching char is one left
            i -= 1
        else:
            j -= 1   
            
            
    return " ".join(word[::-1])