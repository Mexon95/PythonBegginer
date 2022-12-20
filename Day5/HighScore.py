student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
maximum_score = 0
for scores in student_scores:
    if scores > maximum_score:
        maximum_score = scores
print(f"The highest score in the class is: {maximum_score}")