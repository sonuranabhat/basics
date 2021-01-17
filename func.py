def percent(marks):
    p=((marks[0]+marks[1]+marks[2]+marks[3]+marks[4])/400)*100
    return p

marks1=[45,67,88,90,56]
percentage1=percent(marks1)
marks2=[89,97,88,90,86]
percentage2=percent(marks2)
print(percentage1,percentage2)

'''average=(sum(marks)/400)*100
x=len(marks)
print(x)'''


