def bmi(height, weight):
    ### 以下是 local scope ###
    calculate = weight / (height*height)
    if calculate < 18.5:
        result = '過輕'
        return result
    elif 18.5 < calculate and calculate < 24:
        result = '正常'
        return result
    else:
        result='過重'
        return result
    ### 以上是 local scope ###

r = bmi(1.63, 48)
print("result1: ", r) 

def f(x, y):
    ###以下是 local scope ###
    if x == 'Hello':
        print('Hello World')
    ###以上是 local scope ###

f('Hello', 2)

def g():
    ###以下是 local scope ###
    j = 0
    for i in range(10):
        j = j + 1
    return j
    ###以上是 local scope ###