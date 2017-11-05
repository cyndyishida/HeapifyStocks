from RunningMedian import RunningMedian


def main():
    
    Median_Finder = RunningMedian()
    n = int(input())
    for i in range(n):
        print(Median_Finder.find_median(input()))
            
if __name__ == "__main__":
    main()
