

def fact(x):
    if x == 1: 
        return 1
    return x * fact(x-1)

print(fact(5))


def test(x, y):
    a = x * 4 + y
    print(a)
    
test(1, 2)




data =[]
for x in range (7):
    for y in range (7):
        n1 = 0 + 2*7 + 3*7*7 + x*7*7*7 + y*7*7*7*7
        n2 = 3 + y*9 + 3*9*9 + x*9*9*9 + 1*9*9*9*9
        if (n1 + n2) % 181 == 0:
            data.append(n1+n2)
if data:
    print(min(data) // 181)
