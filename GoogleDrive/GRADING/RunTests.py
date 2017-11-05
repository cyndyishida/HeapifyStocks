import RunningMedian as student
import RunningMedian_Solution as answer

SCALE_FACTOR = 8.5
TESTCASE_NUM = 10

def run_testcase(fp):
    correct_count = 0
    stu_Median= student.RunningMedian()
    ans_Median= answer.RunningMedian()
    N = int(fp.readline())
    
    
    for i in range(N):
        instruction = fp.readline()
        stu_Result = stu_Median.find_median( instruction)
        ans_Result = ans_Median.find_median( instruction)
        if abs(stu_Result - ans_Result) < 0.0001:
            correct_count +=1 

    return (correct_count/N)   








for i in range(TESTCASE_NUM):
    fp = open("testcase0{}.txt".format(i), 'r')
    score = run_testcase(fp) * SCALE_FACTOR    
    print( "Testcase# 0{}: {:.2f}".format(i, score))

