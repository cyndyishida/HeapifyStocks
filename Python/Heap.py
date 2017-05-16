def swap(collection, a, b):
    c = collection[a] 
    collection[a] = collection[b]
    collection[b] = c





class Heap ( object ):

    def __init__(self , greaterThan = True ):
        self.__mList = ["x" ]
        self.__mCount = 0
        self.__max = greaterThan
        

    def remove(self, element):
        pass

    def add(self, element):
        self.__mList.append(element)
        self.__mCount +=1 
        if self.__mCount:
            pass
            
                        
    def percolateDown(self, element):
        ''' accurately reheapifies array after element has been removed '''
        swap(self.__mList,0, -1 )
        i = 0 #index of current element to place 
        while 2* i < self.__mCount :
            if  2 * i +1 > self.__mCount:
                if self.__mList[2* i] < element:
                    swap(self.__mList, 2*i, i)
                    i *= 2
            else:
                if self.__mList[2* i] > self.__mList[2* i +1]:
                    swap(self.__mList, 2*i, i)
                    i *= 2
                else:
                    swap(self.__mList, 2*i+1, i)
                    i *= (2 + 1 )

         #def percolate







def main():
    pass


main()