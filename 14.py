x = 9**8 + 3**5 - 9
y = ''
while x != 0: 
    y += str(x % 3)
    x //= 3
print(y.count("2"))


