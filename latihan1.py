import math

a = lambda x: x**2

b = lambda x, y: math.sqrt(x**2 + y**2)

c = lambda *args: sum(args) / len(args)

d = lambda s: "".join(set(s))

print(a(5))        # 25
print(b(3, 4))     # 5.0
print(c(1, 2, 3))  # 2.0
print(d("hello"))  # 'helo' (urutan acak karena set)
