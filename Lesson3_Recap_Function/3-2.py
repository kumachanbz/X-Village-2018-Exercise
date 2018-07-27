###------此範圍內是golbal scope------###
x = 99
m = 11

def f(y, w):
###˙˙˙˙˙˙此範圍內是local scope˙˙˙˙˙### 
    z = x + y
    w = w + 1
    m = 12
    return z
###˙˙˙˙˙˙此範圍內是local scope˙˙˙˙˙###

value = f(1, 2)
###------此範圍內是golbal scope------###