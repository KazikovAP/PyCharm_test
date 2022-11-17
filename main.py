# put your python code here
n = int(input())
b = []

while n:
    if n % 2 == 0:
        b.insert(0, 0)
    else:
        b.insert(0, 1)
    n //= 2

b1 = ''.join(map(str, b))
b2 = int(b1)

print(b2)