import random
list = [random.randint(0, 100) for i in range(30)]


def mysort(list):
    my_list = len(list)
    for i in range(0, my_list - 1):
        for i in range(0, my_list - i - 1):
            if list[i] < list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
    print(sorted(list)[::-1])
mysort(list)
