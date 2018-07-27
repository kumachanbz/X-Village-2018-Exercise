def f(score,time):
    if score > 90:
        bonus = 8000
    elif 90 > score > 70:
        bonus = 6000
    else:
        bonus = 4000
    money = bonus + time*200

    return money

print("A: ", f(45,14))
print("B: ", f(95,13))
print("C: ", f(88,22))