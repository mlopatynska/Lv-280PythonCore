num = input("Enter number please:")
for i in range(1000, 9999, 1):
    sum_ = 0
    count = 0
    result = i
    while i > 0:
        sum_ = sum_ + (i % 10)
        i = i // 10
    if sum_ == num:
        count += 1
        print("{} is equal sum of {} digits".format(num, result))
if count == 0:
    print ("{} is not equal to any sum of digits".format(num))