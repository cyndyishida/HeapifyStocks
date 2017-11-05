import heapq
class RunningMedian:

    def __init__(self):
        self.minH = []
        self.maxH = []


    def heapq_remove(self, heap,index):
        while index > 0:
            up = (index +1) / 2 - 1
            heap[int(index)] = heap[int(up)]
            index = up

        heapq.heappop(heap)
    

    def get_median(self):
        if len(self.maxH) == len(self.minH):
            return_val = (-self.maxH[0] + self.minH[0]) /2
            if return_val %1 == 0:
                return int(return_val)
            else:
                return return_val
        else:
            if len(self.maxH) > len(self.minH):
                return -self.maxH[0]
            else:
                return self.minH[0]

    def balance_heaps(self):
        max_len = len(self.maxH)
        min_len = len(self.minH)
        
        if max_len - min_len > 1:
            move = -heapq.heappop(self.maxH)
            heapq.heappush(self.minH, move)
        elif min_len - max_len > 1:
            move = heapq.heappop(self.minH)
            heapq.heappush(self.maxH, -move)

    def find_median(self, command):
        command, val = command.strip().split()
        val = int(val)
        if command == 'a':
            if len(self.maxH) == 0 or val < -self.maxH[0]:
                heapq.heappush(self.maxH, -val)
            else:
                heapq.heappush(self.minH, val)
            self.balance_heaps()
        elif command == 'r': 
            if len(self.maxH) > 0 and val <= -self.maxH[0]:
                ind = self.maxH.index(-val)
                self.heapq_remove(self.maxH, ind)
                self.balance_heaps()
            else:
                ind = self.minH.index(val)
                self.heapq_remove(self.minH, ind)
                self.balance_heaps()

        return self.get_median()   
