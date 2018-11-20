class Person: 
    
    def __init__(self, name, email, phone): 
       self.name = name 
       self.email = email 
       self.phone = phone 
       self.friends=[] 
       self.greeting_count=0
       self.greet_list=[]

    def greet(self, other_person): 
        print('Hello {}, I am {}!'.format(other_person, self.name))
        self.greeting_count+=1
        if other_person in self.greet_list:
           pass

        else:
            self.greet_list.append(other_person)   

    def print_contact_info(self):
        print("{}\'s Email : {} ,{}\'s Phone : {}".format(self.name, self.email, self.name, self.phone))

    def add_friend(self,friend):
        self.friends.append(friend)  
    def num_friends(self): 
        print(len(self.friends))
    
    def __str__(self):
        return 'Person:{} Email:{} Phone:{}'.format(self.name,self.email,self.phone)
       # f"Person:{self.name} {self.email} {self.phone"}

    def num_unique_people_greeted(self):
        print(len(self.greet_list))     

       


         


    #  Instantiate an instance object of Person with name of 'Sonny', 
    #  email of 'sonny@hotmail.com', and phone of '483-485-4948', 
    #  store it in the variable sonny.
sonny = Person('Sonny','sonny@hotmail.com','483-485-4948')

# Instantiate another person with the name of 'Jordan', 
# email of 'jordan@aol.com', and phone of '495-586-3456', 
# store it in the variable 'jordan'.
jordan = Person("Jordan",'jordan@aol.com','495-586-3456')

# Have jordan greet sonny using the greet method.

jordan.greet(sonny)
jordan.print_contact_info()
# Have sonny greet Jordan using the greet method.

sonny.greet(jordan)
sonny.print_contact_info()
# jordan.friends.append(sonny)
# sonny.friends.append(jordan)
# print(len(jordan.friends))
# print(len(sonny.friends))
jordan.add_friend("sonny")
sonny.add_friend("jordan")
jordan.greet(sonny)
jordan.num_friends()
sonny.greet(jordan)
sonny.greet(jordan)
print(sonny.greeting_count)
sonny.num_unique_people_greeted()
jordan.num_unique_people_greeted()
print(jordan)



# Write a print statement to print the contact info (email and phone) of Sonny.
# print("contact information of Sonny \nEmail: {}\nPhone: {}".format(sonny.email,sonny.phone))

# print("contact information of sonny {} , {}".format(sonny.email,sonny.phone))

# print("contact information of Jordan \nEmail: {}\nPhone: {}".format(jordan.email,jordan.phone))

# 2. Make your own class

# class Vehicle:
#     def __init__(self,make,model,year):
#         self.make=make
#         self.model=model
#         self.year=year
     
#     def print_info(self):
#         print("{} {} {}".format(self.year,self.make,self.model))
# car=Vehicle("Nissan","Leaf",2015) 
# print(car.make,car.model,car.year) 