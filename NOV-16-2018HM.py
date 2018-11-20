# phonebook_dict ={
# 'Alice':'703-493-1834',
# 'Bob':'857-384-1234',
# 'Elizabeth': '484-584-2923'
# }

# print(phonebook_dict['Elizabeth'])
# phonebook_dict['Elizabeth']='938-489-1234'
# del phonebook_dict['Alice']
# phonebook_dict['Bob']='968-345-2345'
# print(phonebook_dict)



# ramit = { 
#   'name': 'Ramit', 
#   'email': 'ramit@gmail.com', 
#   'interests': ['movies', 'tennis'], 
#   'friends': [ 
#      { 
#        'name': 'Jasmine', 
#        'email': 'jasmine@yahoo.com', 
#        'interests': ['photography', 'tennis']
#      }, 
#      { 
#         'name': 'Jan', 
#         'email': 'jan@hotmail.com', 
#         'interests': ['movies', 'tv'] 
#      } 
#     ] 
# }

# # Write a python expression that gets the email address of Ramit.
# print(ramit['email'])
# print(ramit.get('email'))

# # Write a python expression that gets the first of Ramit's interests.
# print(ramit['interests'][0])
# print(ramit.get('interests[0]'))

# # Write a python expression that gets the email address of Jasmine.
# print(ramit['friends'][0]['email'])
# #print(ramit.get('friends'[0]['email']))
# print(ramit.get('email'))
# # Write a python expression that gets the second of Jan's two interests.
# print(ramit['friends'][1]['interests'][1])

# Letter Summary
# Write a letter_histogram function that takes a word as its input, and returns a dictionary containing the tally of how many times each letter in the alphabet was used in the paragraph. For example:

# def letter_histogram(word):
#       l1=list(word)
#       size=len(l1)
#       totalletters={}
#       countB=0
#       countN=0
#       countA=0
#       for i in range(size):
#           if (l1[i] =='a'):
#               countA+=1   
#           elif(l1[i]=='b'):
#                countB+=1
#           elif(l1[i]=='n'):
#               countN+=1
#       totalletters['a']=countA
#       totalletters['b']=countB
#       totalletters['n']=countN        
#       return totalletters
      
# lettercount=letter_histogram("banana")  
# print(lettercount)  


# def letter_histogram(word):
#     a=word.count('a')
#     b=word.count('b')
#     n=word.count('n')
#     totalletters={}
#     totalletters['a']=a
#     totalletters['b']=b
#     totalletters['n']=n
#     return totalletters

# lettercount=letter_histogram("banana")
# print(lettercount)  

# def letter_histogram(word):
    
#     counts = {}

#     for char in word:
#         if char not in counts:
#             counts[char] = 1
#         else:
#             counts[char] += 1
#     return counts    
# lettercount=letter_histogram('bananas')
# print(lettercount)


# def paragraph_histogram(paragraphstr):
#     paragraph=paragraphstr.casefold()
#     to=paragraph.count('to')
#     be=paragraph.count('be')
#     Or=paragraph.count('or')
#     Not=paragraph.count('not')
#     totalwords={}
#     totalwords['to']=to
#     totalwords['be']=be
#     totalwords['or']=Or
#     totalwords['not']=Not
#     return totalwords

# num=paragraph_histogram('To be or not to be')
# print(num)  

def paragraph_histogram(paragraphstr):
    wordcase=paragraphstr.casefold()
    wordlist=wordcase.split()
    wordscount={}

    for word in wordlist:
       if word  not in wordscount:
          wordscount[word] =1
       else:
          wordscount[word]+=1   
    return wordscount 
wordcount=paragraph_histogram('To be or not to be')
print(wordcount)          