import random

answer = random.randint(1,100)
print(answer)
num = int(input("num: "))

while num != answer:
    if num > answer:
        print("too big")
        num = int(input("num: "))
    if num < answer:
        print("too small")
        num = int(input("num: "))
else:
    print("correct")