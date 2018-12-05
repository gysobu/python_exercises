import math
import random


def square(a,b,c):
    value=a*a+b*b
    cValue=c*c
    # if(value==cValue):
    #     return cValue 
          
         

# def triplet(a,b,c):
#      if(a<b):
#          if(b<c):
#              return square(a,b,c)


def addtriplet():
    while True:
       value=0 
       a=random.randint(1,1000)
       b=random.randint(1,1000)
       c=random.randint(1,1000)
       if(a < b):
         if(b < c):
            value+=a+b+c
            if(value==1000): 
              product=a*a+b*b
              if(product==c*c):
                break
               
            #   retvalue=square(a,b,c)
            #   if (retvalue==1000):
            #      break                             
addtriplet()                