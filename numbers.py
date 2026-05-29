'''5 numbers from the user
● Stores them in a list
● Prints:
○ Largest number
○ Smallest number
○ Sum of numbers
○ Count of even and odd numbers'''

numbers=[]
count=0
count2=0
for i in range(5):
  number=int(input("enter five numbers"))
  numbers.append(number)
print("largest number is:",max(numbers))
print("small number is:",min(numbers))
print("sum of numbers is:",sum(numbers))
for i in numbers:
  z=i%2
  if z==0:
    count +=1  
  elif z!=0:
    count2 +=1

print("Count of even numbers:",count)
print("Count of even numbers:",count2)    
