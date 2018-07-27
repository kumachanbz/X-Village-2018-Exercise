
###------此範圍內是golbal scope------###

def f1(*args):     
    print(args)    ###此行是local scope###
    
f1(1, 2, 3, 4, 5, 6, 8, 'hello')
f1('how', 'do', 'you', 'do')

def f2(x, y, *args):
    ###˙˙˙˙˙˙此範圍內是local scope˙˙˙˙˙###
    print(x,y)
    print(args)
    ###˙˙˙˙˙˙此範圍內是local scope˙˙˙˙˙###
f2(1,2,3,4,5,6,8,'hello')

###------此範圍內是golbal scope------###
