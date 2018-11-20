
# 1. 1 to 10

# for i in range(1,11):
#     print(i)

# 2. n to m

# start =int(input("enter num to start from "))
# end =int(input("enter num to start from "))
# for i in range(start,end+1):
#     print(i)

# 3. Odd Numbers

# for i in range(1,10):
#     if(i%2!=0):
#       print(i)

# 4. Print a Square
# Print a 5x5 square of * characters. Example output:
# for i in range(0,5):
#   print('* '*5)

# 5. Print a Square II
# Print a NxN square of * characters. Prompt the user for N. Example output:
# n=int(input("enter the value for N \n "))
# for i in range(0,n):
#   print('* '*n)

#  6. Print a Box
# Given a height and width, input by the user, print a box consisting of * characters as its border. Example session: 

# width = int(input('Width? '))
# height = int(input('Height? '))
# # draw the top border
# print('*' * width)
# # draw the middle
# num_spaces = width - 2
# spaces = ' ' * num_spaces
# for i in range(height -2):
#     print('*' + spaces + '*')

# # draw the bottom border
# print('*' * width)

# 7. Print a Triangle
# Print a triangle consisting of * characters like this:

# height=int(input('Height? '))
# num_spaces=height-1
# spaces=' ' * num_spaces
# for i in range(height):
#    print(spaces + '*' * (2*i+1))
#    num_spaces-=1
#    spaces=' ' * num_spaces

#  8. Print a Triangle II
# Given a number as the height, print a triangle as in "Print a Triangle" but with the given height.  

# height=int(input('Height?enter 0-9 '))
# num_spaces=height-1
# heightstr=str(height)
# spaces=' ' * num_spaces
# for i in range(height):
#    print(spaces + heightstr * (2*i+1))
#    num_spaces-=1
#    spaces=' ' * num_spaces


# 9. Multiplication Table
# Print the multiplication table for numbers from 1 up to 10. Example output:
# result=0
# for i in range(1,11):
#     for j in range(1,11):
#         result=0
#         result+=i*j
#         print("%d*%d=%d" %(i,j,result))

#  Bonus: Print a Banner
