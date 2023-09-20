def main():
	#print("Nhap ten hoc sinh thu nhat:/n")
	#student_A_name = str(input())
	#print("Nhap ten hoc sinh thu 2: ")
	#student_B_name = str(input())
	student_A_name="Nguyen"
	studenrt_A_math_score = 9
	student_A_literature_score = 8
	student_B_name= "Dung"
	studenrt_B_math_score= 9
	student_B_literature_score=9

	print_student(student_A_name, studenrt_A_math_score, student_A_literature_score) # tham so
	print_student(student_B_name, studenrt_B_math_score, student_B_literature_score)

def print_student(name, math_score, literature_score):
	print("Student name: "+ name)
	print("math_score: "+str(math_score))
	print("literature_score: "+ str(literature_score))

	print

main()