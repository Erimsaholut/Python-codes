# π¨ Don't change the code below π
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
# π¨ Don't change the code above π

#Write your code below this row π
buyuk = student_scores[0]

for i in student_scores:
  if i >= buyuk:
    buyuk = i
print(f"En yΓΌksek not {buyuk} Tebrik ederiz !!!")
  




