a=None
if(a is None):
    print("yes")
else:
    print("no")
b=[45,56,6]
print(45 in b) 
marks=int(input("enter your marks"))
if(marks>=90):
    grade="Ex"
elif(marks>=80):
    grade="A"
elif(marks>=70):
    grade="B"
elif(marks>=60):
    grade="C"
elif(marks>=50):
    grade="D"
else:
    grade="F"
print("your grade is "+grade)