from RunningMedian import RunningMedian
'''
Fully Functional Driver code for Project4

WILL NOT BE REQUIRED FOR TURN IN SO CHANGE AS DESIRED
'''



def main():
    
    Median_Finder = RunningMedian()
    
    fp_in = open(input("Enter file to be used:"), 'r')
    
    n = int(fp_in.readline())
    for i in range(n):
        print(Median_Finder.find_median(fp_in.readline()))
            
if __name__ == "__main__":
    main()
