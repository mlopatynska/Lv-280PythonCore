given_number = input("Please input a number <= 36\n")
sum1 = 0
solutions = []

# Variant 1
# for i in range(1000, 10000):
#     for j in list(str(i)):
#         sum1 += int(j)
#     if sum1 == given_number:
#          solutions.append(i)
#     sum1 = 0

# Variant 2
for i in range(1000, 10000):
    if eval("+".join(list(str(i)))) == given_number:
        solutions.append(i)

print solutions

if solutions == []:
    print "These are no solutions"
else:
    print "Solutions are: {}".format(solutions)


