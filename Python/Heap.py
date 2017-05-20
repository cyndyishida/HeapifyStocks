from math import ceil, log2
import random

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
        max_len = ( 2 ** (ceil(log2(self.__mCount)) ) * 2 )
        for k in range(ceil(log2(self.__mCount)) ):
            for n in range(2**k) :
                if i <= self.__mCount:
                    wid = ceil(max_len/ (2 **k))
                    num = "{0:{1}>2d}".format(self.__mList[ i ], "0")
                    printMe += "{0:{1}^{width}}".format(num, "-", width = wid )
                    i += 1
                else:
                    break
            if k != ceil(log2(self.__mCount)) -1:
                printMe += "\n\n"


        return printMe 


    def percolateDown(self):
        ''' accurately reheapifies array after element has been removed '''
        swap(self.__mList,1, -1 )
        i = 1 #index of current element to place 
        while 2* i < self.__mCount :
            if  2 * i +1 > self.__mCount:
                if self.__mList[2* i] < self.__mList[i] :
                    swap(self.__mList, 2*i, i)
                    i *= 2
            else:
                if self.__mList[2* i] > self.__mList[2* i +1]:
                    swap(self.__mList, 2*i, i)
                    i *= 2
                else:
                    swap(self.__mList, 2*i+1, i)
                    i *= (2 + 1 )




    def percolateUp(self):
        '''accurately maintains heap after element has been added '''
        i = self.__mCount 
        while i//2 != 0:
            if self.__mList[i // 2] < self.__mList[i]:
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
    heap = Heap()
    for i in range(32):
        heap.add(random.randint(1, 99))


    print(heap)
main()