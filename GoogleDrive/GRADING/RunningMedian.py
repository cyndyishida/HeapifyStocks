import heapq
class RunningMedian:

    def __init__(self):
        self.minH = []
        self.maxH = []


    def heapq_remove(self, heap,index):
        '''
        @pre: takes in index of value to remove
        @post: removes that value from the given heap 
        Helper function to take in a given heap, and index of a desired remove value 
        and removes it with the help of heapq function
        *** completely optional to use, not required.
        '''
        while index > 0:
            up = (index +1) / 2 - 1
            heap[int(index)] = heap[int(up)]
            index = up

        heapq.heappop(heap)
    

    def get_median(self):
        '''
        @pre: there are 2 present heaps 
        @post: Known median post operation   
        returns the median value 
        '''
        return 0



    def find_median(self, command):
        '''
        @pre: string with valid command as first char and number as last chars 
        @post: returns a valid median value (AS A INTEGER)
        parses commands does proper ordering to find the median  
        '''
        command, val = command.strip().split()
        val = int(val)
        if command == 'a':
            # code logic for add commands 
            pass        
        else: 
            # code logic for remove commands             
            pass 


        return self.get_median()
