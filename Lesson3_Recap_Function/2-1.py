height = 1.63 #公尺
weight = 50 #公斤
calculate = weight / (height*height)
if calculate < 18.5:
    result = '過輕'
elif 18.5 < calculate and calculate < 24:
    result = '正常'
else:
    result='過重'
print("result1: ", result)

height = 1.80 #公尺
weight = 88 #公斤
calculate = weight / (height*height)
if calculate < 18.5:
    result = '過輕'
elif 18.5 < calculate and calculate < 24:
    result = '正常'
else:
    result='過重'
print("result2: ", result)


###以上全是global scope###