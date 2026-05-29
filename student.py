"""Write a program that:
● Takes marks of 5 students using a loop
● Stores marks in a list
● Prints:
○ Highest mark
○ Lowest mark
○ Average mark
○ Number of students passed (marks >= 40)"""

marks=[]
count=0
count2=0
for i in range(5):
    
    mark=int((input(f"enter five marks{i+1}:")))
    marks.append(mark)

    print(marks)

print("max value:",max(marks))    
print(" min value:",min(marks))
print(" sum of mark: ",sum(marks))
avg=sum(marks)/5
print("average of marks",avg)
for mark in marks:
  if mark>=40:
     count+=1
  else:
     count2+=1   
  
print("count of pass ",count)
print("count of fail ",count2)


  