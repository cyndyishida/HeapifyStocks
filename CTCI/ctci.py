def pprint(col):
    for i in col:
        print(i)

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



'''
'''
edit distance
operations 
1. insert
2. delete
3. replace

def editDistance(a, b):
    # a = rows = i
    # b = cols = j
    eD = [[i for i in range(len(b) + 1 )] ]


    #intializing table
    for k in range(1, len(a) + 1):
        eD.append([k] + [0 for i in range( len( b )  )])
    
    



    for i in range( 1, len(a ) +1 ):
        for j in range ( 1 , len(b) + 1):
            if a[ i- 1 ] == b[j - 1 ]: # if there are the same value just take the diagonal
                eD[i][j] = eD[i-1][j-1]
            else:   # take the smallest operation and add 1 because we must change the current 
                eD[i][j] = min(eD[i-1][j] , eD[i][j-1] , eD[i -1][j-1 ]) + 1

    pprint(eD)



editDistance([j for j in "cart"], [i for i in "march" ] )
'''






    def sum_check(val1, val2, target):
        dont_increase = False
        val = 0
        if val1 > target: # case where val 1 is larger but val 2 isnt 
            if val2 > target:
                dont_increase = True
            else:
                val = val2
        elif val2 > target: # case where val2 is larger but val1 isnt 
            val = val1
        elif val1 > val2: # val1 is a greater value 
            val= val1
        else:   # val2 is the greater valid option 
            val = val2

        return dont_increase, val




    fp = open('test.txt')
    for x in range(int(fp.readline())):
        n, k_sum = [int(i) for i in fp.readline().split()]
        ks = [int(i) for i in fp.readline().split()]
        knap = [[0 for i in range(len(ks) + 1) ] for j in range(len(ks) +1 )]



        
        for i in range( 1,len(ks) + 1 ):
            for j in range(1, len(ks)+1 ):
                l_val = knap[i][j-1]
                up_val = knap[i-1][j]
                di_val = knap[i-1][j-1]
                current = ks[i-1]
                best_current =  max(l_val, up_val, di_val)

                outcome = sum_check(l_val + current, di_val + current, k_sum )
                if not outcome[0]:
                    knap[i][j] = outcome[1]
                else:
                    knap[i][j] = best_current



        if knap[i][j] <  best_current:
            knap[i][j] = best_current




    print("Outcome: ", end=' ')
    print(knap[-1][-1]  if knap[-1][-1] <= k_sum else 0 )
    print (" ")


    
    pprint(knap)
    print(" ")














