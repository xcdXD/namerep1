for n in range(1,10000):
    n2 = bin(n)[2:]
    if n % 2 == 0:
        n2 = "11" + n2 + "11"
    else:
        n2 = "1" + n2 + "00"

    res = []
    r = int(n2,2)
    if r <= 113:
        res.append(r)
        print(max(res))