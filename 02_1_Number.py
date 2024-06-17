a = 123
b = -178
c = 0

print(a, b, c)  # 123 -178 0

a = 1.2
b = -3.45

print(a, b)
print(type(a), type(b))

a = 4.24E10     # 4.24 * 10^10
b = 4.24e-10    # 4.24 * 10^(-10)
print(a, b)
print(type(a), type(b))

a = 0o177       # 1*8^2 + 7*8 + 7 = 127
print(a)
print(type(a))  # 8진수 = int

a = 0x8ff       # 8*16^2 + f(15)*16 + f(15) = 2303
b = 0xABC       # A(10)*16^2 + B(11)*16 + C(12) = 2748
print(a, b)
print(type(a), type(b)) # 16진수 = int

# 제곱 연산자
print(2**3)     # 2^3 = 8
print(16**0.5)  # 16의 제곱근

# 나머지 연산자
print(7 % 3)    # 1



