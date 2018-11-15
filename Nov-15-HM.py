# 1. Hello

# def hello(x):
#     print("Hello {x}".format(x=x))
# hello("Igor") 

# 2. y = x + 1

#import matplotlib.pyplot as plot
# def f(x):
#     return x+1
# xs=list(range(-3,4))
# print(xs)  
# ys=[]

# for x in xs:
#     ys.append(f(x)) 
#     print(ys)
# plot.plot(xs,ys)
# plot.savefig('myplot1.png')
# plot.show()  

# # 3. Square of x

import matplotlib.pyplot as plot
# def f(x):
#     return x*x
# xs=list(range(-100,100))
# ys=[]

# for x in xs:
#   ys.append(f(x))
# plot.plot(xs,ys)
# plot.savefig('myplot.png')
# plot.show()  


# 4. Odd or Even

# def f(x):
#    if(x % 2!= 0):
#      return 1
#    else:
#      return -1
# xs=list(range(-5,5))
# ys=[]

# for x in xs:
#    ys.append(f(x))
# plot.bar(xs,ys)
# plot.savefig('myplot.png')
# plot.show()  

# 5. Sine 2

# import  math
# def f(x):
#     return math.sin(x)
# xs= list(range(-5,5))
# ys=[]
# for x in xs:
#     ys.append(f(x))
# plot.plot(xs,ys)   
# plot.savefig('myplot.png') 
# plot.show()    

# 6. Sine 2

# from numpy import arange
# import  math
# def f(x):
#     return math.sin(x)
# xs= list(arange(-5,5,0.1))
# ys=[]
# for x in xs:
#     ys.append(f(x))
# plot.plot(xs,ys)   
# plot.savefig('myplot.png') 
# plot.show()  

# 7. Degree Conversion
# from numpy import arange
# def x(t):
#     ft=(t*9/8)+36
#     return ft
# xs= list(arange(-5,5,0.1))
# ys=[]
# for t in xs:
#     ys.append(x(t))    
# plot.plot(xs,ys)
# plot.savefig('myplot.png') 
# plot.show()

# 8. Play again?

# def prompt():
#     x=input("Do you want to play again (Y on N)?")
#     if(x=="y"):
#       return True
#     else:
#        return False
# print(prompt())

#9. Play again? Again.

# def prompt():
#     while True:
#       x=input("Do you want to play again (Y on N)?")  
#       if(x=="y"):
#         return True
#       elif(x=="n"):
#          return False
       
# print(prompt())

