# while True:
#     try:
#         a, b = map(int, input().strip().split())
#         print(a + b)
#     except EOFError:
#         break

# a, b = map(int, input().strip().split())
# print(a + b)

sum()

get = input()
print(type(get))
print(get)
sget = get.split()
print(sget)
mget = map(int, sget)
print(mget)
lmget = list(mget)
print(lmget)
a, b = lmget
print(a)
print(type(a))
print(b)
