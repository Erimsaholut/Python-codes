# ð¨ Don't change the code below ð
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# ð¨ Don't change the code above ð


#Write your code below this row ð
top = 0
kiÅ = 0
for a in student_heights:
  top += a
  kiÅ += 1
ort = top/kiÅ
print(round(ort))

