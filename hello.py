 # 1. Hello, you!
name=input('what is your name?')
print("%s Hello,%s" %(name,name))

# 2. HELLO, YOU!
name =input('What is your name?')
upper= name.upper()
print("Hello {} ".format(upper))

# 3. Madlib 
name=input("What is your name ? ")
subject=input("what is your favorite subject ? ")
sentence = '%s\'s favorite subject in school is %s'%(name,subject)
print(sentence)

# 4. Day of the Week
day =int(input('Day (0-6)? '))
while(day!=-1):
    day =int(input('Day (0-6)? '))
    if(day>6||day<-1):
     print("not valid")
    elif day == 0:
       print("Sunday") 
    elif day == 1:
       print("Monday") 
    elif day == 2:
       print("Tuesday")
    elif day == 3:        
       print("Wednesday") 
    elif day == 4:    
        print("Thursday")
    elif day == 5: 
        print("Friday")
    elif day == 6: 
        print("Saturday")
    else:
        print("not avalid number")
print("not a day")        

# 5. Work or Sleep In?

day =int(input('Day (0-6)? '))
if day <= 4 :
 print("Go to work")
elif day == 5 or 6:
   print("Sleep")   

# 6. Celsius to Fahrenheit
temp = int(input("Temperature in C ?" ))
Fahrenheittemp = (temp * 9/5)+32
print(Fahrenheittemp)

# 7. Tip Calculator

amount = int(input("The total bill amount:"))
service_level=input("The level of service, which can be one of the following: good, fair, or bad ?\n")
if(service_level =="good"):
 tip=amount*(20/100)
 amount+=tip
 print("Tip amount : ${:.2f}" .format(tip))
 print("Total amount: ${:.2f}" .format(amount))
elif(service_level == "fair"):
   tip =amount*(15/100)
   amount+=tip
   print("Tip amount : ${:.2f}".format(tip))
   print("Total amount: ${:.2f}".format(amount))
elif(service_level == "bad"):    
   tip = amount*(10/100) 
   amount+=tip 
   print("Tip amount : ${:.2f}" .format(tip))
   print("Total amount: ${:.2f}" .format(amount))

# 8. Tip Calculator 2

amount = int(input("The total bill amount:"))
service_level=input("The level of service, which can be one of the following: good, fair, or bad ?\n")
split=int(input("split how many ways ? \n"))
if(service_level =="good"):
 tip=amount*(20/100)
 amount+=tip
 perperson=amount/split
 print("Tip amount : ${:.2f}" .format(tip))
 print("Total amount: ${:.2f}" .format(amount))
 print("Amount per person:{:.2f}".format(perperson))
elif(service_level == "fair"):
   tip =amount*(15/100)
   amount+=tip
   perperson=amount/split
   print("Tip amount : ${:.2f}".format(tip))
   print("Total amount: ${:.2f}".format(amount))
   print("Amount per person:{:.2f}".format(perperson))
elif(service_level == "bad"):    
   tip = amount*(10/100) 
   amount+=tip 
   perperson=amount/split
   print("Tip amount : ${:.2f}" .format(tip))
   print("Total amount: ${:.2f}" .format(amount))
   print("Amount per person:{:.2f}".format(perperson))

 # 9. 1 to 10
num=1
while(num <= 10):
    print(num)
    num+=1  
num = 0  
print("You have %d coins."%(num))

# 10. How many coins ?

num=0
while True: 
    coin = input("Do you want another?")
    num+=1 
    print("you have %d coins"%(num))
    if(coin=="no"):
      break 
print("bye")     