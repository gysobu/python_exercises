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
l1 = [1,5,3,6,7]
l2 =[3,6,9,10,2]
l3=[]
for var1 in l1:
    sum=0
    for var2 in l2:
        var=var1*var2
        sum+=var
    l3.append(sum)
    
print(l3)        


        






