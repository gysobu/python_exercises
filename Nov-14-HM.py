import random 
my_random_number = random.randint(1, 10)
num=int(input("Enter a num "))
while(num!=my_random_number):
  if(num<my_random_number):
    print("Nope, its too low.you have %d guesses\n")     
    num=int(input("Enter a num again \n"))
  elif(num>my_random_number):
    print("Nope, its too high.you have %d guesses\n")
    num=int(input("Enter a num again \n"))
  elif(num==my_random_number): 
    break
print("You Win!")



