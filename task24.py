f = open('zadanie24_1.txt').readline()
k = mx = i = 0
while i<len(f):
    if f[i] == 'A' and f[i+1] == 'B':
        k = k + 2
        i = i + 2
        if f[i] == 'B' and f[i-1] == 'A':
            k = k + 1
            i = i + 1
    else:
        if k > mx:
            mx = k
        k = 0
        i = i + 1
print(mx)