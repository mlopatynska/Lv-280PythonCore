def equat(a, b, c, x, y, z):
    start = 0
    for numa in range(a, 30 + a):
        for root in range(30, 0, -1):
            sol1 = numa * x ** root
            start = start + sol1
    sol1 = start ** 2
    print (sol1)

    start = 0
    for numb in range(b, 30 + b):
        for root in range(30, 0, -1):
            sol2 = numb * y ** root
            start = start + sol2
    sol2 = start
    print (sol2)

    solnum = sol1 - sol2
    print (solnum)

    start = 0
    for numc in range(c, 30 + c):
        for root in range(30, 0, -1):
            solden = numc * (x + z) ** root
            start = start + solden
    solden = start
    print (solden)

    finsol = float(solnum / solden)
    print (finsol)


equat(1, 2, 2, 2, 3, 2)