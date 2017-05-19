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
        return str(self.__mList) + "\nCount: " + str(self.__mCount)

    def percolateDown(self):
        ''' accurately reheapifies array after element has been removed '''

        swap(self.__mList,1, -1 )
        i = 1 #index of current element to place 
        while 2* i < self.__mCount :
            print(i)
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



    def remove(self):
        self.percolateDown()
        self.__mList = self.__mList[:-1]

    def add(self, element):
        self.__mList.append(element)
        self.__mCount +=1 
        if self.__mCount:
            pass
            
                        
    







def main():
     heap = Heap(["x", 20,10,11,7,2,4,5,3])
     print(heap)
     heap.remove()
     print(heap)
     heap.remove()
     print(heap)

main()