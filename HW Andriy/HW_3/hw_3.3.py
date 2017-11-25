variable1 = raw_input("Please input a\n")
variable2 = raw_input("Please input b\n")

variable1 = variable2 + "*" + variable1

variable2 = variable1[variable1.find("*")+1:]
variable1 = variable1[:variable1.find("*")]

print "a =", variable1
print "b =", variable2
