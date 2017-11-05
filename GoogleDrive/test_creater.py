import random



x = random.randint(5, 10)
# possible numbers
numbers = [random.randint(-100,-1) for v in range(x)]

added_vals = set()

print(x)
for i in range(x):
    index = random.randint(0,x-1)
    if i % 2:
        if numbers[index] in added_vals:
            print("r {}".format(numbers[index]))
            added_vals.remove(numbers[index])
        else:
            print("a {}".format(numbers[index]))
            added_vals.add(numbers[index])
    else:
        print("a {}".format(numbers[index]))
        added_vals.add(numbers[index])


