from math import ceil, log2
from random import randint

def swap(collection, a, b):
    c = collection[a] 
    collection[a] = collection[b]
    collection[b] = c





class Heap ( object ):

    def __init__(self ,lst = ["x"], greaterThan = True ):
        self.__mList = lst

        self.__mCount = len(self.__mList) -1
        self.__max = greaterThan
    
    def __repr__(self ) :
        return self.__str__()


    def __str__(self ) :
        printMe = "Heap contains: {} nodes\n".format(self.__mCount)
        i = 1
        max_len = ( 2 ** (ceil(log2(self.__mCount))  ) * 2 )
        for k in range(ceil(log2(self.__mCount + 1 )) ):
            for n in range(2**k ) :
                if i <= self.__mCount:
                    wid = ceil(max_len/ (2 **k))
                    num = "{0:{1}>2d}".format(self.__mList[ i ], "0")
                    printMe += "{0:{1}^{width}}".format(num, "-", width = wid )
                    i += 1
                else:  # in case where last level has less then 2^current level nodes
                    break


            printMe += "\n\n"


        return printMe + "\n" + str(self.__mList)


    def percolateDown(self):
        ''' accurately reheapifies array after element has been removed '''
        swap(self.__mList,1, -1 )
        i = 1 #index of current element to place 
        while 2* i < self.__mCount :
            if  2 * i +1 > self.__mCount:
                if self.__mList[i] > self.__mList[2* i]   :   # only left child 
                    swap(self.__mList, 2*i, i)
                    i *= 2
            else:
                if self.__mList[2* i] > self.__mList[2* i +1]: # break ties w/ 2 children
                    if self.__mList[i] > self.__mList[2* i]: 
                        swap(self.__mList, 2*i, i)
                        i *= 2
                    elif self.__mList[i] > self.__mList[2* i + 1 ]:
                        swap(self.__mList, 2*i+1, i)
                        i *= (2 + 1 )
                    
                else:
                    if self.__mList[i] > self.__mList[2* i + 1 ]:
                        swap(self.__mList, 2*i+1, i)
                        i *= (2 + 1 )
                    elif self.__mList[i] > self.__mList[2* i]: 
                        swap(self.__mList, 2*i, i)
                        i *= 2



    def percolateUp(self):
        '''accurately maintains heap after element has been added '''
        i = self.__mCount 
        while i//2 != 0:
            if self.__mList[i] > self.__mList[i // 2] :
                swap(self.__mList, i//2, i)
                i //= 2
            else:
                break # if we dont ever swap, that means we are in the correct location




    def remove(self):
        self.__mCount -= 1
        self.percolateDown()
        self.__mList = self.__mList[:-1]

    def add(self, element):
        self.__mList.append(element)
        self.__mCount +=1
        self.percolateUp()




def main():
    max_heap = Heap()
    hold  = []
    for i in range(randint(10,40)):
            x = randint(1, 99)
            max_heap.add(x)
            hold.append(x)
    '''
    for i in range(randint(1,13)):
        if i % 2:
            x = randint(1, 99)
            max_heap.add(x)
            hold.append(x)
        else:
            max_heap.remove()
    '''
    print(max_heap)
    print(len(hold) )
main()