number_grade = int(input("Enter how many grades are you entering here:"))
l=[]
for i in range(number_grade):
    g1=int(input("Enter grade #"+str(i+1)+": "))
    l.append(g1)
student=(sum(l)/(len(l)*100))*100
letter_grade=""
if student > 93:
    letter_grade="A"
elif student > 79 and student <= 92.99:
    letter_grade="B"
elif student > 73 and student  <= 78.99:
    letter_grade="C"
elif student > 61.99 and student <= 72.99:
    letter_grade="D"
elif student < 61.99:
    letter_grade = "F"
    print("You Got a "+letter_grade+" ")
if letter_grade != "A":
    print("not an A")
