
while True:
     phonebook()  
     phonearr=[]
     dict_phonebook={}
     print("1. Look up an entry\n2. Set an entry \n3. Delete an entry \n4. List all entries \n5. Quit " )
     num=int(input("What do you want to do (1-5)? "))
     if(num==2):
        def setEntry(): 
        name=input("Name:") 
        dict_phonebook['Name']=name
        phnum=input("Phone Number:")
        dict_phonebook['Phone Number']=phnum
        phonearr.append(dict_phonebook)
    return dict_phonebook()
     print(phonearr)
     print("Entery stored for %s."%(name))
     elif(num==3):
        name=input("Name:")
        phonearr.remove(dict_phonebook[name]) 
        
     elif(num==4):  
         print(dict_phonebook)   
         break 
print(dict_phonebook)    