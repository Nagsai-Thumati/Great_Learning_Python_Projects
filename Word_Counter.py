#Accessing the word file from dropbox in colab website

!wget https://www.dropbox.com/s/5vbyxqzj5xjkc3k/harpers_ASCII.txt
  
#Reading the text file 

file = open('/content/harpers_ASCII.txt','r')

# Creating an empty list to save all the words to it
c = []      

# using for loop to append all the words from text file to list 'c'
for x in file:          
  print(x)
  c.append(x.split())

print(c)

# Initializing d to count the number of words in list 'c'
d = 0

# iterating through c to find number of words in c
for i in range(len(c)):
  d = d+1

#printing number of words in text file
print(d)
