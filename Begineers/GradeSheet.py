print("\n *** Display a Grade For Average of Marks *** \n")

getNum_subjects = int(input(" How Many Subjects : "))
total_marks, grade = [], ""

for i in range(0,getNum_subjects):
	subjects = int(input(" Enter Subject {} Marks : ".format(i+1)))
	total_marks.append(subjects)

average = int(sum(total_marks)/getNum_subjects)

if(average >= 90):
	grade = "A"
elif(average >= 80 & average < 90):
	grade = "B"
elif(average >= 70 & average < 80):
	grade = "C"
elif(average >= 60 & average < 70):
	grade = "D"
else:
	grade = "F"

print("\n Total Marks is {}, Average is {} and Grade is {}.".format(sum(total_marks), average, grade))