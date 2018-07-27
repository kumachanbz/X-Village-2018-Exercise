def f(score,time):
    if score > 90:
        bonus = 8000
    elif 90 > score > 70:
        bonus = 6000
    else:
        bonus = 4000
    money = bonus + time*200

    return money

print("A: ", f(91,20))
print("B: ", f(75,15))
print("C: ", f(60,25))
print("D: ", f(75,10))
print("E: ", f(80,12))
print("F: ", f(90,25))