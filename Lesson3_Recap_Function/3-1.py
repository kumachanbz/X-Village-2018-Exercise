
###------此範圍內是golbal scope------###
x = 23

def f():
    print('x1:', x) ###此行是local scope###

y = 23
def g(y, w):
    ###˙˙˙˙˙˙此範圍內是local scope˙˙˙˙˙###
    y = 22
    print('y1:', y)
    print('w1:', w)
    ###˙˙˙˙˙˙此範圍內是local scope˙˙˙˙˙###
f()
print('x2:', x)
g(10, 12)
print('y2:', y)
###------此範圍內是golbal scope------###