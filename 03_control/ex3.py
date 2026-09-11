# for문

# for (int i = 0; i < 10; i++)
# for i in iterable 객체:

for i in range(5):  # 0 ~ 4
    print(i, end=" ")
print()


a = range(5)
print(a.start, a.stop, a.step)

# 1 ~ 5
for i in range(1, 6):
    print(i, end=" ")
print()

# 1 ~ 10, 2씩
for i in range(1, 11, 2):
    print(i, end=" ")
print()

# 5, 4, 3, 2, 1
for i in range(5, 0, -1):
    print(i, end=" ")
print()

# 1 ~ 10까지의 합
tot = 0
for i in range(1, 11):
    tot += i
print(f"tot = {tot}")

print(sum(range(1, 11)))

s = "hi12!@한글漢子"


for c in s:
    print(c, end=" ")
print()

print(len(s))

# 구구단 출력
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i*j:<2d}", end=" ")
    print()
else:
    print("End")
