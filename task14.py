data = []
for x in range(37):
    for y in range(37):
        n = 1*37**7+2*37**6+x*37**5+6*37**4+4*37**3+3*37**2+y*37**1+7*37**0
        if n % 36 == 0:
            data.append(y*37**1+x)
print(max(data))