number_grade = int(input("Enter how many grades are you entering here:"))
l=[]
for i in range(number_grade):
    g1=int(input("Enter grade #"+str(i+1)+": "))
    l.append(g1)
student=(sum(l)/(len(l)*100))*100
letter_grade=""
if student > 93:
    letter_grade = "A"
    print("You Got an A")
elif student > 79 and student <= 92.99:
    letter_grade="B"
elif student > 73 and student  <= 78.99:
    letter_grade="C"
elif student > 61.99 and student <= 72.99:
    letter_grade="D"
elif student < 61.99:
    letter_grade = "F"
if letter_grade != "A":
    print("not an A")

print("Grade of 90 should be A: " + score_to_letter_grade(90))
print("Grade of 87 should be B+: " + score_to_letter_grade(87))
print("Grade of 81 should be B: " + score_to_letter_grade(81))
print("Grade of 77 should be C+: " + score_to_letter_grade(77))
print("Grade of 70 should be C: " + score_to_letter_grade(70))
print("Grade of 67 should be D+: " + score_to_letter_grade(67))
print("Grade of 60 should be D: " + score_to_letter_grade(60))
print("Grade of 59 should be F: " + score_to_letter_grade(59))
