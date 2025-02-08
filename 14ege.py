for x in range(2020+1):
    t = 3**100 - x
    count = 0
    while t!=0:
        if t%3 == 0:
            count += 1
        t = t//3
    if count == 2:
        print(x)
        break
    
    