a=int(raw_input("Enter number in range 1-365 please:"))

if a%7==1:
    print("It's Monday!")
elif a%7==2:
    print("It's Tuesday!")
elif a%7==3:
    print("It's Wednesday!")
elif a%7==4:
    print("It's Thursday!")
elif a%7==5:
    print("It's Friday!")
elif a%7==6:
    print("It's Saturday!")
elif a%7==0:
    print("It's Sunday!")