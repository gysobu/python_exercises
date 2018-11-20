# myShoppingList=["apples","celery","grapes","spinach"]
# print(len(myShoppingList))
# print (myShoppingList[0:2])
# newList=myShoppingList[0:2]
# print(newList[1]) 
# myShoppingList.insert(0,"mangoes")
# print(myShoppingList)
# myTuple=(1,"Sobha","Ganga")
# print(myTuple)
# print(myTuple[1])
# print(range(10))
# for index  in range(10):
#   print("index:",index)
#   for innerindex in range(10):
#     print("innerined:",innerindex) 
# for outerindex  in range(1,11): 
#    print("outerindex:",outerindex)
#    for innerindex in range(1,11):
#      print("innerined:",innerindex)    
# president =["george","w","bush"]
# print(president)
# for name in president:
#   print(president.index(name))
#   print("pop:"president.pop())
# 


# def sampleFunction():
#     print("Hello World")
# sampleFunction()    

# def f(x):
#     return 2*x+1
# for x in range(-3,5):
#     print("{0}".format(f(x)))
#     print("f({x})={y}".format(x=x,y=f(x)))  

# list1 =[1,2,3]
# list2 =list1.copy()
# print(list1)
# print(list2) 
# def f(x):
#   return 2 * x + 1
# def g(x):
#   return x + 1
# import matplotlib
# matplotlib.use("Agg")
# from matplotlib import pyplot
# f_output = []
# g_output = []
# x_list = list(range(-3, 5))
# for x in x_list:
#   f_output.append(f(x))
#   g_output.append(g(x))
# pyplot.plot(x_list, f_output, x_list, g_output)
# pyplot.savefig('myplot.png')
# pyplot.close() 


# from turtle import *
# forward(100)
# right(90)
# forward(100)
# right(90)
# forward(100)
# right(90)
# forward(100)
# mainloop()
# move into position
# up()
# forward(50)
# left(90)
# forward(50)
# left(90)
# down()
# # draw the square
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# mainloop()

# from turtle import *
# pencolor('orange')
# width(10)
# circle(180)

# contact = [
#     {
#         'first_name': 'Phillip',
#         'last_name': 'Guo',
#         'email': 'phillip.guo@gmail.com',
#         'phone':{
#             'work':'837-494-3948',
#             'cell': '234-897-4933'
#         }
#     },
#     {
#         'first_name': 'Mark',
#         'last_name': 'Guzdial',
#         'email': 'mark.guzdial@gatech.edu',
#         'phone':{
#             'work':'484-569-3466',
#             'cell': '493-485-9845'
#              'numbers':[1,2,3,4]
#         }
#     }
# ]

# result=contact[1]["phone"]["numbers"]
# print(result)

# class student:
#     def _init(self,firstN,lastN):
#         self.firstName=firstN
#         self.lastName=lastN
#     def GreetStudent(self):
#         print(f"Hello{self.firstName}{self.lastName}")

#    

class Car:
    greeting="hello world"
    def __init__(self,make,model,color):
        self.make=make
        self.model=model
        self.color=color           
    def Changecolor(self,toColor):
        print(f"changing from {self.color} to {toColor}")
        self.color=toColor
        print(f"New clor from {self.color}")
car=Car("Toyota","Tundra","Red")
car.Changecolor("green")
print(car.color)   

# class ElectricCar(Car):
#     def _init(self,make,model,range,autopilot):
#        super()._init(make,model)
#        self.range=range
#        self.autopilot=autopilot
#     def batteryLife()   


# tesla=ElectricCar("tesla","model s","3 hours","yes")
# print()








        






