import random 
my_random_number = random.randint(1, 10)
num=int(input("Enter a num "))
guesscount=4
while(guesscount>0):
  if(num==my_random_number):
      break
      guesscount-=1
      while(num!=my_random_number):
        if(num<my_random_number):
          print("Nope, its too low.you have %d guesses\n")
          print("you have {} guesses left".format(guesscount))     
          num=int(input("Enter a num again"))
        elif(num>my_random_number):
          print("Nope, its too high.you have %d guesses\n")
          num=int(input("Enter a num again"))
        elif(num==my_random_number): 
          break
        print("You Win!")
  print("you won")    
print("you loss game")      



