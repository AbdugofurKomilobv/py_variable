# i = int(input('son: '))
# i2 = int(input('son2: '))


# print(i % i2)
def to_binary(n):
    if n == 0:
        return "0"
    sign = ""
    if n < 0:
        sign = "-"
        n = -n
    bits = []
    while n > 0:
        bits.append(str(n % 2))
        n //= 2
    return sign + ''.join(reversed(bits))

num = int(input("Son kiriting: "))
print(to_binary(num))
