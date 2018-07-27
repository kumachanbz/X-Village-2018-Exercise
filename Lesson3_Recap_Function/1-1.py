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