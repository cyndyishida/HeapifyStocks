from math import ceil, log2

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
        return str(self.__mList)

    def __str__(self ) :
        printMe = "Heap contains: {} nodes\n".format(self.__mCount)
        i = 1
        for k in range(ceil(log2(self.__mCount)) ):
            for n in range(2**k) :
                if i <= self.__mCount:
                    printMe += " {:^d} ".format(self.__mList[ i])
                    i += 1
                else:
                    break
            printMe += "\n"

        
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
     heap = Heap(["x", 20,10,11,7,2,4,5,3])
     heap.add(15)
     heap.add(25)
     heap.add(12)
     heap.add(18)
     heap.add(8)
     print(heap)
main()